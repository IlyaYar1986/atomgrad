#!/usr/bin/env python3
"""Собирает ZIP-шаблоны агентов для скачивания со страницы вебинара.

Берёт папки из корневой `agenty/` и кладёт архивы в `Agenty_dlya_biznesa/downloads/`.
В архив попадает только каркас: промпт, анкета, шаблоны знаний, пустые input/ и output/.
Данные — легенда из demo/, залитые демо-файлы, реальные прогоны в output/ — не попадают
никогда: список файлов собирается белым списком, а не вычитанием.

Запуск:  python3 tools/sobrat_shablony.py
"""

import io
import os
import zipfile

KOREN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AGENTY = os.path.join(KOREN, "agenty")
VYHOD = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "downloads")

# Одинаковая дата у всех записей — чтобы архив не пересобирался «по-новому» без изменений
DATA_V_ARHIVE = (2026, 1, 1, 0, 0, 0)

# Человеческие названия для КАК_ЗАПУСТИТЬ.md — в порядке карточек на странице
NAZVANIYA = {
    "01_razvedchik-konkurenta": "Разведчик конкурентов",
    "02_prodavec-kp": "Продавец: заявка → КП",
    "03_rassylshchik": "Рассыльщик персональных писем",
    "04_sekretar-planerki": "Секретарь планёрки",
    "05_agent-podderzhki": "Агент поддержки",
    "06_kadrovik-skriner": "Кадровик-скринер",
    "07_zakupshchik": "Закупщик",
    "08_finansovyy-analitik": "Финансовый аналитик",
    "09_kontent-fabrika": "Контент-фабрика",
    "10_trenazher-peregovorov": "Тренажёр переговоров",
}

# Страховка поверх правила «имя встречается в demo/ — значит данные»:
# файлы, которые не должны уехать участнику ни при каких условиях
ZAPRESHCHENO = {
    "profil_klienta.md",   # паспорт чужого бизнеса
    "prays.md",            # цены легенды
    "slovar.md",
    "vakansiya.md",
    "nashe_predlozhenie.md",
    "chto_zakupaem.md",
    "menyu_i_ceny.md",
    "chastye_zhaloby.md",
    "reglament_kompensaciy.md",
    "otraslevye_orientiry.md",
}

# Точечные правки текста при упаковке: в исходниках агентов есть куски, адресованные
# ведущему, — участнику они непонятны и ссылаются на файлы, которых в шаблоне нет.
# Если строка не нашлась, сборка падает: значит исходник поменялся и правку надо пересмотреть.
PRAVKI = {
    "03_rassylshchik/AGENTS.md": [
        (
            "Готовые демо-версии лежат в `demo/knowledge/`; `demo/` в целом — "
            "заготовки для живого показа, а не рабочие данные.",
            "",
        ),
        (
            "- `ZAPUSK.md` — шпаргалка ведущего демо, а не инструкция для агента: "
            "там объяснено, зачем всё это и что показывать залу.\n",
            "",
        ),
    ],
}

# Всё, что идёт с этого заголовка и ниже, — инструкции ведущему, в шаблон не едут
GRANICA_EFIRA = "# Для эфира"

SHAPKA = """# {nazvanie}

Шаблон помощника с вебинара «ИИ как помощник предпринимателя: реальные сценарии применения».
Внутри — только каркас: роль, инструкция, анкета и шаблоны знаний. Данных нет: ни наших, ни чужих.

## Что нужно один раз

1. Установить **VS Code** и **OpenCode** — как на вебинаре.
2. Распаковать эту папку куда угодно на своём компьютере.

## Как запустить

Откройте терминал в этой папке и наберите:

```
opencode
```

OpenCode читает `AGENTS.md` из той папки, где запущен, — поэтому запускать нужно **изнутри
папки агента**, а не рядом с ней. Роль, цель, инструкция и ограничения у помощника уже есть.

## Первый запуск — это опрос

Помощник не привязан к какому-то бизнесу. В первый раз он сам расспросит про ваш: чем
занимаетесь, где, кто покупает, почему выбирают вас, как разговариваете с клиентами.
Ответы он запишет в `knowledge/` — это его память, второй раз спрашивать не будет.

Что отвечать и что делать, если данных под рукой нет, написано в `knowledge/anketa.md`.

## Что внутри

| Папка | Что это |
|---|---|
| `AGENTS.md` | Сам помощник: роль, цель, инструкция, знания, память, ограничения |
| `knowledge/` | Анкета и шаблоны знаний. Сюда же помощник запишет ответы про ваш бизнес |
| `input/` | Пустая. Сюда вы кладёте свои файлы: заявки, письма, резюме, записи |
| `output/` | Пустая. Сюда помощник кладёт результат |

## Если помощник придумывает

Значит, ему не дали нужный файл — прайс, регламент, список. Не спорьте с ним:
положите файл в `knowledge/` или `input/` и повторите запрос.
"""


def pochistit(kluch, tekst):
    """Убирает из текста куски, написанные для ведущего, а не для участника."""
    for chto, na_chto in PRAVKI.get(kluch, []):
        if chto not in tekst:
            raise SystemExit(f"правка не применилась, исходник изменился: {kluch}\n  {chto[:60]}…")
        tekst = tekst.replace(chto, na_chto)

    if GRANICA_EFIRA in tekst:
        tekst = tekst.split(GRANICA_EFIRA)[0].rstrip().rstrip("-").rstrip() + "\n"

    return tekst


def imena_demo(papka_agenta):
    """Имена всех файлов из demo/ — их тёзки в рабочих папках считаем данными."""
    demo = os.path.join(papka_agenta, "demo")
    imena = set()
    for koren, _, fayly in os.walk(demo):
        for f in fayly:
            imena.add(f)
    return imena


def sobrat_spisok(papka_agenta):
    """Белый список путей (относительно папки агента), которые едут в архив."""
    zapreshcheno = imena_demo(papka_agenta) | ZAPRESHCHENO
    puti = []

    if os.path.isfile(os.path.join(papka_agenta, "AGENTS.md")):
        puti.append("AGENTS.md")

    # knowledge/: анкета, шаблоны и методички — всё, кроме заполненных данных
    znaniya = os.path.join(papka_agenta, "knowledge")
    if os.path.isdir(znaniya):
        for f in sorted(os.listdir(znaniya)):
            if not f.endswith(".md") or f in zapreshcheno:
                continue
            puti.append("knowledge/" + f)

    # input/: только методички «как подготовить», сами данные — никогда
    vhod = os.path.join(papka_agenta, "input")
    if os.path.isdir(vhod):
        for koren, _, fayly in os.walk(vhod):
            for f in sorted(fayly):
                if not f.startswith("kak_") or not f.endswith(".md"):
                    continue
                otn = os.path.relpath(os.path.join(koren, f), papka_agenta)
                puti.append(otn)

    return puti


def pustye_papki(papka_agenta):
    """input/, output/ и их подпапки — едут пустыми, с .gitkeep внутри."""
    papki = []
    for korneva in ("input", "output"):
        put = os.path.join(papka_agenta, korneva)
        if not os.path.isdir(put):
            continue
        papki.append(korneva)
        for koren, katalogi, _ in os.walk(put):
            for k in sorted(katalogi):
                papki.append(os.path.relpath(os.path.join(koren, k), papka_agenta))
    return papki


def sobrat_agenta(imya):
    papka = os.path.join(AGENTY, imya)
    nazvanie = NAZVANIYA[imya]
    arhiv = os.path.join(VYHOD, imya + ".zip")

    with zipfile.ZipFile(arhiv, "w", zipfile.ZIP_DEFLATED) as z:
        def polozhit(otn_put, dannye):
            zapis = zipfile.ZipInfo(imya + "/" + otn_put, date_time=DATA_V_ARHIVE)
            zapis.external_attr = 0o644 << 16
            zapis.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(zapis, dannye)

        polozhit("КАК_ЗАПУСТИТЬ.md", SHAPKA.format(nazvanie=nazvanie).encode("utf-8"))

        fayly = sobrat_spisok(papka)
        for otn in fayly:
            with io.open(os.path.join(papka, otn), encoding="utf-8") as f:
                tekst = pochistit(imya + "/" + otn, f.read())
            polozhit(otn, tekst.encode("utf-8"))

        for p in pustye_papki(papka):
            polozhit(p + "/.gitkeep", b"")

    return arhiv, len(fayly)


def main():
    os.makedirs(VYHOD, exist_ok=True)
    for imya in sorted(NAZVANIYA):
        arhiv, skolko = sobrat_agenta(imya)
        razmer = os.path.getsize(arhiv)
        print(f"{imya}.zip — файлов: {skolko + 1}, размер: {razmer // 1024} КБ")


if __name__ == "__main__":
    main()
