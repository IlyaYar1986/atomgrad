# План сайта-презентации «ИИ как помощник предпринимателя»

Одна страница-лонгрид `index.html` + пять интерактивных демо в `web/`. Показывается с проектора во время вебинара и остаётся участникам после него.

**Брендирование — заказчика.** Основной бренд «Сделано в Атомграде»: знак `assets/logo_atomgrad_znak.png` в навбаре, в hero и в подвале. Знак ведущего «Просто делай» (`assets/logo_prosto_delay.svg`) — только в подвале, в блоке «Ведущий вебинара».

Палитра и типографика сняты с сайта проекта — сделановатомграде.рф: синий `#20599D` (основной), красный `#E31E24` (редкий акцент), текст `#111418`, приглушённый `#6B7380`, границы `#DDE6EE`, фон белый с чередованием полос `#F4F7FA`. Шрифт Montserrat с системным запасным. Карточки со скруглением 24px, кнопки и бейджи — пилюли, заголовки крупные и жирные с отрицательным межбуквенным.

## Секции страницы

| № | id | Заголовок | Инфографика | Интерактив |
|---|---|---|---|---|
| — | `hero` | ИИ как помощник предпринимателя | 01 | — |
| 1 | `s1` | Чат отвечает — помощник делает | 02 | `chat_vs_agent.html` |
| 2 | `s2` | Из чего собран помощник | 03 | `konstruktor_agenta.html` |
| 3 | `s3` | Знания: чтобы не выдумывал | 04 | — |
| 4 | `s4` | Инструменты: за пределами чата | 05 | — |
| 5 | `s5` | Skills: упакованное умение | 06 | — |
| 6 | `s6` | MCP: внутри ваших систем | 07 | — |
| 7 | `s7` | Контроль, риски и деньги | 08 | `kalkulyator_ekonomii.html` |
| 8 | `s8` | Ваш первый помощник | 09 | `matrica_processov.html` |
| 9 | `s9` | Где брать готовое | 10 | `karta_servisov.html` |
| — | `checklist` | Чек-лист готовности | — | localStorage |
| — | `quiz` | Проверьте себя | — | 6 вопросов |
| — | `final` | Что забрать с собой | — | — |

## Интерактивные демо

1. **`chat_vs_agent.html`** — переключатель «чат / помощник» на одной задаче. Слева запрос, справа — что происходит: у чата один шаг и текст на выходе, у помощника цепочка шагов и готовый документ.
2. **`konstruktor_agenta.html`** — шесть тумблеров (роль, цель, инструкция, знания, память, ограничения). Участник включает их и видит, как меняется ответ на жалобу клиента. Повторяет блок 2 вебинара, чтобы можно было переиграть дома.
3. **`kalkulyator_ekonomii.html`** — часы в неделю × ставка × число сотрудников против стоимости подписки. Показывает экономию в месяц, в год и срок окупаемости настройки.
4. **`matrica_processov.html`** — матрица «частота × рутинность». Участник расставляет свои процессы, правый верхний угол подсвечивается как кандидат на первый пилот.
5. **`karta_servisov.html`** — таблица сервисов с фильтром по доступности (без ограничений / нужна карта / нужен VPN) и по задаче.

---

# Промпты для генерации инфографики

Все — 16:9, не меньше 1672×941, белый фон в стиле сайта проекта, текст по-русски с буквой «ё». Файлы кладём в `png/prezentaciya/` под именами `01_...png` … `10_...png`.

**Важно про брендирование:** в промптах намеренно не просим рисовать логотип — генераторы искажают знаки. Логотип накладывается на странице средствами HTML, а не внутри картинки.

## 01 · Обзорная (hero)

```
16:9 dense professional Russian infographic in the style of a modern data-journalism explainer poster
(flat design with glossy 3D glass elements), clean white background with a subtle light-grey dotted grid pattern (#DDE6EE dots).

Bold near-black (#111418) title top center in a geometric sans-serif (Montserrat-like), tight letter-spacing: "ИИ как помощник предпринимателя"
Deep blue (#20599D) subtitle beneath: "От вопроса в чате — до сотрудника, который доводит дело до конца"

Central large glowing 3D glass motif: a hexagon containing a stylized human head silhouette with an
upward arrow inside it, symbolizing an assistant that acts. Deep blue (#20599D) and pale blue glass,
subtle inner glow.

Left column, deep blue (#20599D) pill-shaped section header "Что он уже делает": white panel with thin #DDE6EE border and 24px rounded corners, icon+label rows:
"Разбирает сайт конкурента" (магнифier glass icon), "Пишет КП по вашему прайсу" (document icon),
"Отвечает на жалобы" (chat bubble icon), "Готовит протокол планёрки" (microphone icon).

Right column, deep blue (#20599D) pill-shaped section header "Из чего он состоит": white panel with thin #DDE6EE border and 24px rounded corners, icon+label rows:
"Роль и цель" (badge icon), "Знания — ваши документы" (folder icon),
"Инструменты — почта, файлы, сайты" (wrench icon), "Ограничения — что нельзя" (shield icon).

Bottom horizontal stepper across the full width: four connected numbered circles with dotted line:
"1" lightning icon — "Сегодня" — "15 минут, первый результат";
"2" gear icon — "За неделю" — "процесс и документы";
"3" box icon — "За месяц" — "упакованное умение";
"4" plug icon — "Дальше" — "подключение к вашим системам".

No watermarks, no real company logos, all text in correct Russian.
```

## 02 · Чат против помощника

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements,
clean white background with a subtle light-grey dotted grid pattern (#DDE6EE dots).

Bold near-black (#111418) title top center in a geometric sans-serif (Montserrat-like), tight letter-spacing: "Чат отвечает — помощник делает"
Deep blue (#20599D) subtitle beneath: "Одна и та же задача, два разных результата"

Split composition, vertical dotted divider down the middle.

Left half, pill-shaped header "ЧАТ" in muted grey (#6B7380): a single glass speech bubble.
Below it one short arrow to a plain sheet of paper labelled "Текст, который вы дальше
доделываете руками". Small grey caption: "Один шаг · знает только общее · вы дорабатываете".

Right half, pill-shaped header "ПОМОЩНИК" in deep blue (#20599D): a glowing glass gear-and-network motif
with four sequential arrows forming a chain: "читает задачу" (eye icon) → "заходит на сайт"
(globe icon) → "считает по прайсу" (calculator icon) → "собирает документ" (document icon).
The chain ends in a finished document with a deep blue check mark, labelled "Готово — можно отправлять".
Small caption: "Столько шагов, сколько нужно · пользуется вашими данными · доводит до результата".

Bottom horizontal bar, pill header "Простой тест": one wide panel with large text:
"Надо доделывать руками — это был чат. Можно отправить клиенту — это был помощник."

No watermarks, no real company logos, all text in correct Russian.
```

## 03 · Шесть частей помощника

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements,
clean white background with a subtle light-grey dotted grid pattern (#DDE6EE dots).

Bold near-black (#111418) title top center in a geometric sans-serif (Montserrat-like), tight letter-spacing: "Из чего собран помощник"
Deep blue (#20599D) subtitle beneath: "Шесть частей. Настройка — час, польза — годы"

Central large glowing 3D glass motif: a hexagonal core (deep blue #20599D to pale blue gradient) with six
glass facets radiating outward, each connected by a thin glowing line to its own bordered card.

Six cards arranged radially around the core, each with a pill header, an icon and one line of text:
"РОЛЬ" (name badge icon) — "Кем он себя считает: управляющий кофейней, а не робот";
"ЦЕЛЬ" (target icon) — "Ради чего: вернуть клиента, а не закрыть обращение";
"ИНСТРУКЦИЯ" (numbered list icon) — "Порядок действий и формат ответа";
"ЗНАНИЯ" (folder icon) — "Ваш прайс и регламенты — иначе выдумает";
"ПАМЯТЬ" (notebook icon) — "Что помнит между обращениями";
"ОГРАНИЧЕНИЯ" (shield icon) — "Чего не делает никогда и когда зовёт человека".

Bottom horizontal bar with a before/after pair separated by a dotted arrow:
left side, red crossed-out speech bubble: "Приносим извинения за доставленные неудобства";
right side, blue-outlined document: "Иван, сырники правда были пересушены — повару указали.
Зайдите на этой неделе, кофе за наш счёт."

No watermarks, no real company logos, all text in correct Russian.
```

## 04 · Откуда берётся враньё

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements,
clean white background with a subtle light-grey dotted grid pattern (#DDE6EE dots).

Bold near-black (#111418) title top center in a geometric sans-serif (Montserrat-like), tight letter-spacing: "Почему он выдумывает цены — и как это лечится"
Deep blue (#20599D) subtitle beneath: "Нейросеть начитана, но в вашей компании не работала"

Left half, pill-shaped header "БЕЗ ВАШИХ ДОКУМЕНТОВ" in accent red (#E31E24): a glass human-head motif
surrounded by floating book icons and website icons, with a red question mark over the head.
An arrow points to a price tag showing "≈ 1 200 ₽/м" with a red crossed-out stamp
and caption "Цифра правдоподобная. И выдуманная."

Right half, pill-shaped header "С ВАШИМИ ДОКУМЕНТАМИ" in deep blue (#20599D): the same glass head motif,
now connected by a glowing line to a glass filing cabinet labelled "Прайс · Регламент · Договор".
An arrow points to a price tag "1 450 ₽/м" with a deep blue check mark and a small quote block
underneath: "источник: прайс, строка 14".

Bottom horizontal stepper across the full width: four connected numbered circles with dotted line:
"1" folder icon — "Соберите" — "прайс, регламенты, скрипты";
"2" upload icon — "Загрузите" — "прямо файлами, ничего не переписывая";
"3" quote icon — "Требуйте источник" — "«покажи, откуда взял»";
"4" refresh icon — "Обновляйте" — "поменялся прайс — поменяйте файл".

No watermarks, no real company logos, all text in correct Russian.
```

## 05 · Инструменты помощника

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements,
clean white background with a subtle light-grey dotted grid pattern (#DDE6EE dots).

Bold near-black (#111418) title top center in a geometric sans-serif (Montserrat-like), tight letter-spacing: "Инструменты: помощник выходит за пределы чата"
Deep blue (#20599D) subtitle beneath: "Консультант по телефону становится сотрудником с доступами"

Central large glowing 3D glass motif: a hexagonal assistant core with a tool-belt ring around it,
six glowing connectors reaching outward to service icons: envelope (почта), spreadsheet (таблицы),
calendar (календарь), folder (файлы), globe (сайты и поиск), microphone (запись встреч).

Left column, deep blue (#20599D) pill-shaped section header "Что он делает сам": white panel with thin #DDE6EE border and 24px rounded corners, icon+label rows:
"Читает входящие письма" (envelope icon), "Ищет и проверяет в интернете" (globe icon),
"Считает и сводит в таблицу" (calculator icon), "Расшифровывает планёрку" (microphone icon).

Right column, deep blue (#20599D) pill-shaped section header "Пример сквозной задачи": white panel with thin #DDE6EE border and 24px rounded corners, containing a vertical
numbered chain: "1 Найти письма поставщиков за неделю" → "2 Вытащить позиции и цены" →
"3 Свести в таблицу и отсортировать" → "4 Прислать готовый файл".

Bottom horizontal bar in warm amber, pill header "Граница": wide panel with text:
"Он ошибается: не так понял письмо, взял не тот прайс. Право отправлять письма и платить деньги
ему не дают."

No watermarks, no real company logos, all text in correct Russian.
```

## 06 · Skills

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements,
clean white background with a subtle light-grey dotted grid pattern (#DDE6EE dots).

Bold near-black (#111418) title top center in a geometric sans-serif (Montserrat-like), tight letter-spacing: "Skills: один раз описал — дальше в два слова"
Deep blue (#20599D) subtitle beneath: "Инструкция для нового сотрудника, только читает её помощник"

Left half, pill-shaped header "КАЖДЫЙ РАЗ ЗАНОВО" in muted grey (#6B7380): a glass sheet densely filled with
small grey text lines, a tired clock icon in the corner, caption "Полстраницы задания. Каждый раз."

Dotted arrow pointing right, labelled "упаковали".

Right half, pill-shaped header "ОДИН РАЗ И НАВСЕГДА" in deep blue (#20599D): a glowing glass box with a
label tag reading "рассылка по базе", and a tiny speech bubble next to it containing just
"сделай рассылку по этому файлу". Caption: "Процесс внутри. Снаружи — имя."

Bottom horizontal stepper across the full width: four connected numbered circles with dotted line:
"1" repeat icon — "Повторяется" — "чаще раза в неделю";
"2" document icon — "Один формат" — "результат всегда одинаковый";
"3" speech icon — "Объясняли дважды" — "сотруднику приходилось повторять";
"4" moon icon — "Делаете вечером" — "потому что днём некогда".
Caption under the stepper: "Сошлись три пункта из четырёх — это ваш первый skill."

No watermarks, no real company logos, all text in correct Russian.
```

## 07 · MCP — универсальная розетка

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements,
clean white background with a subtle light-grey dotted grid pattern (#DDE6EE dots).

Bold near-black (#111418) title top center in a geometric sans-serif (Montserrat-like), tight letter-spacing: "MCP: универсальная розетка для помощника"
Deep blue (#20599D) subtitle beneath: "Раньше под каждую программу — свой переходник. Теперь один стандарт"

Left half, pill-shaped header "БЫЛО" in accent red (#E31E24): a tangled mess of differently-shaped plugs and
mismatched sockets connected by chaotic crossing cables, each pair a different colour and shape,
caption "Каждое подключение — отдельная разработка".

Right half, pill-shaped header "СТАЛО" in deep blue (#20599D): one clean glowing glass socket strip with
identical plugs neatly connected, each plug labelled: "Почта", "Календарь", "Таблицы", "Telegram",
"CRM", "Файлы". Caption "Один разъём — любой помощник".

Bottom horizontal bar split into three pill-headed zones with traffic-light colours:
green "Работает" — "почта, календари, таблицы, файлы, Telegram";
amber "Работает с оговорками" — "CRM, отраслевые сервисы, часть коннекторов сырая";
red "Пока нет" — "глубокая интеграция с учётными системами без разработчика".

No watermarks, no real company logos, all text in correct Russian.
```

## 08 · Три зоны доступа

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements,
clean white background with a subtle light-grey dotted grid pattern (#DDE6EE dots).

Bold near-black (#111418) title top center in a geometric sans-serif (Montserrat-like), tight letter-spacing: "Что помощнику можно, а что нельзя"
Deep blue (#20599D) subtitle beneath: "Генерация — ему, отправка — вам. По крайней мере первые два месяца"

Central motif: a large glowing glass traffic light rendered in 3D, tilted slightly, with three
lit lenses — green, amber, red — each connected by a glowing line to its own bordered panel.

Green panel, pill header "ДЕЛАЕТ САМ": icon+label rows — "Черновики писем" (pencil icon),
"Расшифровки встреч" (microphone icon), "Разбор конкурентов" (magnifier icon),
"Поиск и аналитика" (chart icon).

Amber panel, pill header "ДЕЛАЕТ И ПОКАЗЫВАЕТ": icon+label rows — "Письма клиентам" (envelope icon),
"Ответы на отзывы" (star icon), "Документы и счета" (document icon).

Red panel, pill header "НЕ ТРОГАЕТ": icon+label rows — "Платежи" (banknote icon),
"Договоры" (stamp icon), "Персональные данные клиентов" (passport icon),
"Кадровые решения" (people icon), "Обещания скидок" (percent icon).

Bottom horizontal bar, pill header "Персональные данные": wide panel with text:
"Паспорта, телефоны и адреса клиентов в облако не загружаем. Чувствительное — на своём
компьютере. Сомневаетесь — обезличивайте: «Клиент А» вместо фамилии."

No watermarks, no real company logos, all text in correct Russian.
```

## 09 · Лестница внедрения

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements,
clean white background with a subtle light-grey dotted grid pattern (#DDE6EE dots).

Bold near-black (#111418) title top center in a geometric sans-serif (Montserrat-like), tight letter-spacing: "Ваш первый помощник: сегодня, за неделю, за месяц"
Deep blue (#20599D) subtitle beneath: "Порядок нарушать нельзя — девять из десяти провалов начинаются с третьей ступени"

Central motif: three ascending glass steps rendered in 3D, deep blue (#20599D) to pale blue gradient, with a small
glowing figure climbing them. Each step has its own bordered panel beside it.

Step 1 panel, pill header "СЕГОДНЯ · 15 МИНУТ": icon+label rows — "Дайте роль и цель" (badge icon),
"Приложите один документ" (folder icon), "Сделайте один рабочий текст" (document icon).
Caption: "Цель — не автоматизация, а первое «работает»".

Step 2 panel, pill header "ЗА НЕДЕЛЮ": icon+label rows — "Выберите процесс по матрице" (grid icon),
"Опишите шесть частей" (list icon), "Прогоните двадцать раз" (repeat icon),
"Замерьте время до и после" (stopwatch icon).

Step 3 panel, pill header "ЗА МЕСЯЦ": icon+label rows — "Упакуйте в skill" (box icon),
"Дайте инструменты" (wrench icon), "Поставьте подтверждение" (check icon),
"Назначьте ответственного и метрику" (person icon).

Bottom horizontal bar, pill header "Выбор процесса": a small 2x2 matrix diagram with axes
"как часто" and "насколько рутинно", the top-right cell highlighted deep blue and labelled
"ваш первый пилот".

No watermarks, no real company logos, all text in correct Russian.
```

## 10 · Карта сервисов

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements,
clean white background with a subtle light-grey dotted grid pattern (#DDE6EE dots).

Bold near-black (#111418) title top center in a geometric sans-serif (Montserrat-like), tight letter-spacing: "Где брать помощников и готовые решения"
Deep blue (#20599D) subtitle beneath: "Три полки: начать без вложений, вырасти, взять готовое"

Three vertical bordered columns, each with a pill-shaped header and a glass 3D icon on top.

Column 1, green pill "БЕЗ ВЛОЖЕНИЙ И БЕЗ КАРТЫ", glass rocket icon: icon+label rows for
Russian-accessible assistants, each row a plain text service name with a short use-case caption
underneath, e.g. "чат-помощник в браузере", "помощник в поиске", "помощник в мессенджере".

Column 2, blue pill "КОГДА НУЖНО БОЛЬШЕ", glass gear icon: rows for international services with a
small warning tag on each: "нужна зарубежная карта", "нужен доступ". Captions describe what they
add: длинные документы, работа с файлами, длинные цепочки шагов.

Column 3, purple pill "ГОТОВЫЕ РЕШЕНИЯ", glass box icon: rows — "Каталоги агентов",
"Библиотеки готовых умений", "Каталоги коннекторов", "Сообщества и разборы".

Bottom horizontal bar, pill header "Правило выбора": wide panel with text:
"Начните с того, что открывается в браузере без карты. Переходите дальше, только когда упрётесь
в конкретное ограничение."

No watermarks, no real company logos, all text in correct Russian.
```

---

# Что нужно от заказчика перед публикацией

- **Ссылки на ведущего** для подвала: Telegram-канал, сайт, любые другие. Сейчас в `index.html` стоят плейсхолдеры, помеченные комментарием `TODO: контакты`. Email `churilovilya74@gmail.com` уже проставлен.
- **Подтверждение имени** в подвале: сейчас указан «Илья Чурилов» — выведено из адреса почты.
- **Инфографика** — десять PNG по промптам выше в `png/prezentaciya/`. До их появления страница показывает подписи-заглушки и выглядит целой.
