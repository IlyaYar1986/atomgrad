"""Структурные проверки сайта-презентации «ИИ как помощник предпринимателя»."""

import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "index.html"
DEMOS = [
    ROOT / "web" / "chat_vs_agent.html",
    ROOT / "web" / "konstruktor_agenta.html",
    ROOT / "web" / "kalkulyator_ekonomii.html",
    ROOT / "web" / "matrica_processov.html",
    ROOT / "web" / "karta_servisov.html",
]
ASSETS = [
    ROOT / "assets" / "logo_atomgrad_znak.png",   # основной бренд — знак заказчика
    ROOT / "assets" / "logo_prosto_delay.svg",    # знак ведущего в подвале
]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.id_counts = {}
        self.iframe_srcs = []
        self.img_srcs = []
        self.imgs_without_alt = []
        self.links = []
        self.lang = None

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "html":
            self.lang = values.get("lang")
        if "id" in values:
            value = values["id"]
            self.ids.add(value)
            self.id_counts[value] = self.id_counts.get(value, 0) + 1
        if tag == "iframe" and "src" in values:
            self.iframe_srcs.append(values["src"])
        if tag == "img":
            src = values.get("src", "")
            self.img_srcs.append(src)
            # У картинки лайтбокса alt проставляется скриптом при открытии
            if not values.get("alt") and values.get("id") != "lightbox-img":
                self.imgs_without_alt.append(src or "(без src)")
        if tag == "a" and "href" in values:
            self.links.append(values["href"])


def parse(path):
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


class PrezentaciyaPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = PAGE.read_text(encoding="utf-8") if PAGE.exists() else ""
        cls.parser = parse(PAGE) if PAGE.exists() else PageParser()

    def test_page_exists(self):
        self.assertTrue(PAGE.is_file(), "index.html не найден")

    def test_required_sections(self):
        required = {
            "hero", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9",
            "agents", "checklist", "quiz", "final",
        }
        missing = required - self.parser.ids
        self.assertFalse(missing, f"нет обязательных секций: {sorted(missing)}")

    def test_no_duplicate_ids(self):
        duplicates = {key: count for key, count in self.parser.id_counts.items() if count > 1}
        self.assertFalse(duplicates, f"дубли id: {duplicates}")

    def test_lang_is_russian(self):
        self.assertEqual(self.parser.lang, "ru")

    def test_all_images_have_alt(self):
        self.assertFalse(
            self.parser.imgs_without_alt,
            f"картинки без alt: {self.parser.imgs_without_alt}",
        )

    def test_embedded_demos_exist(self):
        for src in self.parser.iframe_srcs:
            if not src:
                continue
            self.assertTrue((ROOT / src).is_file(), f"встроенное демо не найдено: {src}")

    def test_all_demos_are_embedded(self):
        embedded = {src for src in self.parser.iframe_srcs if src}
        for demo in DEMOS:
            relative = f"web/{demo.name}"
            self.assertIn(relative, embedded, f"демо не встроено в страницу: {relative}")

    def test_infographics_paths(self):
        png_srcs = [src for src in self.parser.img_srcs if src.startswith("png/")]
        self.assertEqual(len(png_srcs), 10, "ожидается 10 инфографик")
        for src in png_srcs:
            self.assertTrue(
                src.startswith("png/prezentaciya/"),
                f"инфографика лежит не в png/prezentaciya/: {src}",
            )
            self.assertTrue(
                (ROOT / src).is_file(),
                f"файла инфографики нет на диске: {src}",
            )

    def test_brand_assets_present(self):
        for asset in ASSETS:
            self.assertTrue(asset.is_file(), f"нет фирменного ассета: {asset.name}")
        # Основной бренд — заказчик: его знак в навбаре, в hero и в подвале
        self.assertGreaterEqual(
            self.html.count("assets/logo_atomgrad_znak.png"), 3,
            "знак заказчика должен стоять в навбаре, hero и подвале",
        )
        self.assertIn("Сделано в Атомграде", self.html)
        self.assertIn("assets/logo_prosto_delay.svg", self.html)

    def test_client_brand_palette(self):
        for token in ("#20599d", "Montserrat"):
            self.assertIn(token, self.html, f"нет фирменного токена: {token}")
        for stale in ("#1a3054", "#4ea634", "--navy"):
            self.assertNotIn(stale, self.html, f"осталась прежняя палитра: {stale}")

    def test_author_contacts_present(self):
        self.assertIn("churilovilya74@gmail.com", self.html, "нет контакта ведущего")
        self.assertIn("Просто делай", self.html, "нет названия проекта в подвале")

    def test_no_external_cdn(self):
        for marker in ("cdn.", "googleapis.com", "unpkg.com", "jsdelivr"):
            self.assertNotIn(marker, self.html, f"страница тянет внешний ресурс: {marker}")

    def test_checklist_has_unique_storage_key(self):
        self.assertIn("ii-pomoshchnik-prezentaciya-checklist", self.html)

    def test_quiz_questions_have_one_right_answer(self):
        # Обрезаем каждый блок по фидбэку: дальше идёт следующий вопрос или скрипт,
        # в котором тоже встречается value="right"
        blocks = [
            chunk.split("data-quiz-feedback")[0]
            for chunk in self.html.split('<div class="quiz-question"')[1:]
        ]
        self.assertGreaterEqual(len(blocks), 6, "ожидается не меньше 6 вопросов квиза")
        for index, block in enumerate(blocks, start=1):
            right = block.count('value="right"')
            self.assertEqual(right, 1, f"в вопросе {index} правильных вариантов: {right}")
            self.assertIn(f'data-quiz-check="{index}"', block, f"в вопросе {index} нет кнопки проверки")

    def test_quiz_has_explanation_for_every_question(self):
        blocks = self.html.split('<div class="quiz-question"')[1:]
        for index in range(1, len(blocks) + 1):
            self.assertIn(f"  {index}:", self.html, f"нет разбора для вопроса {index}")

    def test_key_content_markers(self):
        markers = [
            "Чат отвечает — помощник делает",
            "Из чего собран помощник",
            "генерация — ему, отправка — вам",
            "Персональные данные",
            "Выберите один процесс",
        ]
        for marker in markers:
            self.assertIn(marker.lower(), self.html.lower(), f"нет ключевого маркера: {marker}")


class DemoPagesTest(unittest.TestCase):
    def test_demos_exist_and_are_self_contained(self):
        for demo in DEMOS:
            with self.subTest(demo=demo.name):
                self.assertTrue(demo.is_file(), f"нет демо: {demo.name}")
                html = demo.read_text(encoding="utf-8")
                for marker in ("cdn.", "googleapis.com", "unpkg.com", "jsdelivr", "<link"):
                    self.assertNotIn(marker, html, f"{demo.name} тянет внешний ресурс: {marker}")

    def test_demos_have_lang_and_title(self):
        for demo in DEMOS:
            with self.subTest(demo=demo.name):
                parser = parse(demo)
                self.assertEqual(parser.lang, "ru", f"{demo.name}: нет lang=ru")
                self.assertIn("<title>", demo.read_text(encoding="utf-8"))

    def test_demos_have_no_duplicate_ids(self):
        for demo in DEMOS:
            with self.subTest(demo=demo.name):
                parser = parse(demo)
                duplicates = {key: count for key, count in parser.id_counts.items() if count > 1}
                self.assertFalse(duplicates, f"{demo.name}: дубли id {duplicates}")

    def test_service_links_are_absolute(self):
        parser = parse(ROOT / "web" / "karta_servisov.html")
        html = (ROOT / "web" / "karta_servisov.html").read_text(encoding="utf-8")
        import re

        urls = re.findall(r'url:\s*"([^"]+)"', html)
        self.assertGreaterEqual(len(urls), 10, "в карте сервисов слишком мало ссылок")
        for url in urls:
            self.assertTrue(url.startswith("https://"), f"ссылка не абсолютная: {url}")


class PlanTest(unittest.TestCase):
    def test_plan_and_konspekt_exist(self):
        self.assertTrue((ROOT / "Docs" / "konspekt_vebinara.md").is_file())
        self.assertTrue((ROOT / "Docs" / "prezentaciya_plan.md").is_file())

    def test_plan_has_all_ten_prompts(self):
        plan = (ROOT / "Docs" / "prezentaciya_plan.md").read_text(encoding="utf-8")
        for number in range(1, 11):
            self.assertIn(f"## {number:02d} ·", plan, f"нет промпта {number:02d} в плане")

    def test_every_prompt_carries_the_atomic_background(self):
        plan = (ROOT / "Docs" / "prezentaciya_plan.md").read_text(encoding="utf-8")
        self.assertEqual(
            plan.count("BACKGROUND LAYER"), 10,
            "сквозной атомный фон должен быть во всех десяти промптах — иначе серия распадётся",
        )

    def test_prompts_use_client_palette(self):
        plan = (ROOT / "Docs" / "prezentaciya_plan.md").read_text(encoding="utf-8")
        self.assertIn("#20599D", plan)
        for stale in ("lavender", "fresh green", "navy to green"):
            self.assertNotIn(stale, plan, f"в промптах осталась прежняя гамма: {stale}")


if __name__ == "__main__":
    unittest.main()
