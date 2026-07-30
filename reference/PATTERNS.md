# Кодовые паттерны страниц-лонгридов

Готовые к копированию блоки. Полный рабочий пример — `reference/etalon_lekciya.html`, чистый скелет — `web/TEMPLATE_stranica.html`.

---

## 1. Палитра и переменные

```css
:root{
  --bg:#f0f2f7; --card:#ffffff; --border:#e2e8f0;
  --indigo:#6366f1; --indigo-dk:#4338ca; --indigo-lt:#eef2ff;
  --cyan:#0ea5e9;   --cyan-lt:#e0f2fe;
  --amber:#f59e0b;  --amber-lt:#fffbeb;
  --green:#16a34a;  --green-lt:#f0fdf4;
  --red:#dc2626;    --red-lt:#fef2f2;
  --text:#0f172a;   --muted:#64748b;
  --nav-h:56px;
}
```

Фон страницы — три слоя: два радиальных «свечения» индиго и cyan в верхних углах плюс вертикальный градиент.

```css
body{
  font-family:'Segoe UI',system-ui,-apple-system,sans-serif;
  background:
    radial-gradient(circle at 12% 0%,rgba(99,102,241,.14),transparent 32%),
    radial-gradient(circle at 85% 6%,rgba(14,165,233,.13),transparent 34%),
    linear-gradient(180deg,#f8fafc 0%,#eef2ff 30%,#f8fafc 100%);
  color:var(--text); line-height:1.65; overflow-x:hidden;
}
```

## 2. Номерные бейджи блоков

Порядок градиентов фиксирован — не менять от страницы к странице.

```css
.num-badge{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border-radius:13px;font-size:1.1rem;font-weight:900;color:#fff;margin-bottom:14px}
.n1{background:linear-gradient(135deg,#6366f1,#818cf8)}  /* индиго */
.n2{background:linear-gradient(135deg,#0ea5e9,#38bdf8)}  /* sky */
.n3{background:linear-gradient(135deg,#8b5cf6,#a78bfa)}  /* violet */
.n4{background:linear-gradient(135deg,#16a34a,#4ade80)}  /* emerald */
.n5{background:linear-gradient(135deg,#f59e0b,#fbbf24)}  /* amber */
.n6{background:linear-gradient(135deg,#ec4899,#f472b6)}  /* pink */
.n7{background:linear-gradient(135deg,#dc2626,#f87171)}  /* red */
.n8{background:linear-gradient(135deg,#0891b2,#22d3ee)}  /* cyan */
.n9{background:linear-gradient(135deg,#4338ca,#6366f1)}  /* indigo-dark */
```

## 3. Фиксированный навбар + подсветка активной секции

```html
<nav class="top" aria-label="Навигация по странице">
  <a class="nav-link" href="../oglavlenie.html">← Оглавление</a>
  <span class="nav-sep"></span>
  <span class="nav-logo">Название блока</span>
  <span class="nav-sep"></span>
  <a class="nav-link" href="#s1">Первый блок</a>
  <!-- … -->
</nav>
```

```js
const navLinks = [...document.querySelectorAll(".nav-link")];
const sections = [...document.querySelectorAll("main section[id]")];
if ("IntersectionObserver" in window) {
  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      navLinks.forEach((link) => {
        link.classList.toggle("active", link.getAttribute("href") === `#${entry.target.id}`);
      });
    });
  }, {rootMargin: "-35% 0px -55%", threshold: 0});
  sections.forEach((section) => sectionObserver.observe(section));
}
```

## 4. Появление секций при скролле

Класс `.fade` вешается на каждый визуальный блок; при пересечении добавляется `.in`.

```js
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
if (!reduceMotion && "IntersectionObserver" in window) {
  const reveal = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) { entry.target.classList.add("in"); reveal.unobserve(entry.target); }
    });
  }, {threshold: 0.06, rootMargin: "0px 0px -24px"});
  document.querySelectorAll(".fade").forEach((el) => reveal.observe(el));
} else {
  document.querySelectorAll(".fade").forEach((el) => el.classList.add("in"));
}
```

## 5. Картинка с лайтбоксом, заглушкой и брендированным скачиванием

Заглушка через `onerror` обязательна: страница должна выглядеть целой до того, как человек сгенерирует PNG.

```html
<figure class="img-card fade" data-lightbox>
  <img src="../png/<страница>/02_nazvanie.png"
       alt="Осмысленное описание того, что на инфографике"
       loading="lazy"
       onerror="this.closest('.img-card').classList.add('img-missing')">
  <figcaption class="img-missing-caption">Что здесь будет (промпт 02 из плана)</figcaption>
</figure>
```

```js
const BRAND = "ii-agenty";   // префикс имени файла при скачивании
function brandedFilename(url) {
  const name = url.split("/").pop().split("?")[0];
  return `${BRAND}_${name}`;
}
document.querySelectorAll(".img-card[data-lightbox]").forEach((card) => {
  card.addEventListener("click", () => {
    if (card.classList.contains("img-missing")) return;
    const img = card.querySelector("img");
    lightboxImg.src = img.src; lightboxImg.alt = img.alt;
    lightboxDownload.href = img.src;
    lightboxDownload.download = brandedFilename(img.src);
    lightbox.classList.add("open");
    lightbox.setAttribute("aria-hidden", "false");
  });
});
function closeLightbox() {
  if (lightbox.contains(document.activeElement)) document.activeElement.blur();  // иначе фокус остаётся в aria-hidden
  lightbox.classList.remove("open");
  lightbox.setAttribute("aria-hidden", "true");
  lightboxImg.src = "";
}
```

## 6. iframe-карточка «окно macOS» + фуллскрин

```html
<div class="viz fade">
  <div class="viz-bar">
    <div class="dots"><span class="dot dr"></span><span class="dot dy"></span><span class="dot dg"></span></div>
    <span class="viz-lbl">Калькулятор экономии</span>
    <button type="button" class="viz-fs" data-fs-src="kalkulyator.html" data-fs-title="Калькулятор экономии">⛶ На весь экран</button>
  </div>
  <iframe src="kalkulyator.html" height="560" loading="lazy" title="Калькулятор экономии"></iframe>
</div>
```

```js
document.querySelectorAll(".viz-fs").forEach((button) => {
  button.addEventListener("click", () => {
    fsFrame.src = button.dataset.fsSrc;
    fsTitle.textContent = button.dataset.fsTitle;
    fsOverlay.classList.add("open");
    fsOverlay.setAttribute("aria-hidden", "false");
  });
});
document.addEventListener("keydown", (event) => {
  if (event.key !== "Escape") return;
  if (fsOverlay.classList.contains("open")) { closeFs(); } else { closeLightbox(); }
});
```

## 7. Промпт-бокс с копированием

```html
<div class="prompt-box fade">
  <div class="prompt-head">
    <span>Промпт: описание роли агента</span>
    <button type="button" class="copy-btn" data-copy="prompt-1">Копировать</button>
  </div>
  <pre id="prompt-1">Ты — ассистент отдела продаж компании …</pre>
</div>
```

```js
document.querySelectorAll("[data-copy]").forEach((button) => {
  button.addEventListener("click", async () => {
    const code = document.getElementById(button.dataset.copy);
    if (!code) return;
    const original = button.textContent;
    try { await navigator.clipboard.writeText(code.innerText); button.textContent = "Скопировано"; }
    catch { button.textContent = "Выделите текст"; }
    window.setTimeout(() => { button.textContent = original; }, 1600);
  });
});
```

## 8. Чек-лист с прогрессом в localStorage

```html
<li><label><input type="checkbox" data-checklist-item="c1"> Выбрал процесс с понятной метрикой</label></li>
```

```js
const CHECKLIST_KEY = "<имя-страницы>-checklist";   // уникальный ключ на страницу
const checklistInputs = [...document.querySelectorAll("[data-checklist-item]")];
function loadChecklistState() {
  try { return JSON.parse(localStorage.getItem(CHECKLIST_KEY) || "{}"); } catch { return {}; }
}
function saveChecklistState(state) {
  try { localStorage.setItem(CHECKLIST_KEY, JSON.stringify(state)); } catch { /* приватный режим */ }
}
function renderChecklistProgress() {
  const checked = checklistInputs.filter((i) => i.checked).length;
  checklistProgress.style.width = `${Math.round((checked / checklistInputs.length) * 100)}%`;
  checklistDone.hidden = checked !== checklistInputs.length;
}
```

## 9. Квиз с разбором

Правильный вариант помечается `value="right"`, остальные — `value="wrong"`. После ответа варианты блокируются и правильный подсвечивается — даже если участник ошибся.

```html
<div class="quiz-question" data-quiz="1">
  <p class="quiz-text">Вопрос?</p>
  <div class="quiz-options">
    <label><input type="radio" name="q1" value="wrong"> Неверный вариант</label>
    <label><input type="radio" name="q1" value="right"> Верный вариант</label>
  </div>
  <button type="button" class="quiz-check" data-quiz-check="1">Проверить</button>
  <p class="quiz-feedback" data-quiz-feedback="1" hidden></p>
</div>
```

```js
question.querySelectorAll("input").forEach((input) => { input.disabled = true; });
question.querySelector('input[value="right"]').closest("label").classList.add("quiz-correct-answer");
```

## 10. Что проверять перед сдачей страницы

- `python3 -m http.server 8000` — открыть по HTTP, не по `file://`.
- Десктоп и ширина 375px: навбар скроллится, сетки схлопываются в одну колонку.
- Лайтбокс: открытие, Escape, клик по фону, кнопка скачивания.
- Фуллскрин iframe: открытие, Escape, `src` очищается при закрытии.
- Консоль без ошибок; все `id` уникальны; у всех картинок есть `alt`.
- `python3 -m unittest discover -s tests -p "check_*.py" -v`.
