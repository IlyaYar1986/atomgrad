# План HTML-страницы — Лекция 4.4 «Управление качеством данных и цифровая безопасность»

Источник: `Docs/лекции/Лекция 4.4.md` + два дополненных пользователем блока (управление качеством данных, цифровая гигиена шире 152-ФЗ — заголовок лекции обещает больше, чем даёт исходный текст).
Целевой файл страницы: `web/bezopasnost_dannyh.html`
Папка инфографики: `png/bezopasnost_dannyh/` — **формат 16:9**, стиль «плотный флагманский инфографик» (как `png/ChatGPT Image 26 апр. 2026 г., 15_49_57.png`, `..._15_50_43.png`), НЕ плоские HTML-постеры и НЕ формат A4 — пользователь генерирует сам через ChatGPT/аналог.

---

## 0. История правок промптов

Версия 1 (отклонена): фотореалистичный 16:9 робот+3 панели+баннер (стиль `personalizaciya_tyutorstvo`). Версия 2 (отклонена пользователем — «плохие картинки», «на отвали»): собственные HTML/CSS-рендеры формата A4. **Версия 3 (текущая):** промпты для фотореалистичной ИИ-генерации в «флагманском» стиле `index.html` — плотная многопанельная инфографика с числовым степпером, стеклянными 3D-иконками, pill-заголовками секций, сравнением «было/стало», дружелюбным роботом-маскотом. Формат 16:9, пользователь генерирует сам.

## 1. Структура страницы (после расширения контента)

| # | id | Секция | Картинка |
|---|----|--------|----------|
| — | `hero` | Хиро | 01 |
| 1 | `s1` | От этики к закону (опрос) | — |
| 2 | `s2` | **Управление качеством данных** (новое) | 02 |
| 3 | `s3` | 152-ФЗ: кто отвечает и сколько это стоит | 03 |
| 4 | `s4` | Кейс Минпросвещения | 04 |
| 5 | `s5` | **Цифровая безопасность шире одного закона** (новое) | 05 |
| 6 | `s6` | Пять вопросов к ИИ-сервису | — |
| 7 | `s7` | GigaChat vs ChatGPT vs Claude | 06 |
| 8 | `s8` | Промпт для проверки сервиса | — |
| 9 | `s9` | Алгоритм действий при инциденте | 07 |
| — | `checklist` | Чек-лист проверки сервиса | — |
| — | `quiz` | Квиз (7 вопросов) | — |
| — | `final` | Заключение (5 выводов) | 08 |

## 2. Промпты для генерации инфографики (16:9, флагманский стиль)

Общие указания для каждого промпта (не повторяются в тексте ниже, но обязательны):
- Соотношение 16:9, разрешение не меньше 1672×941.
- Светлый лавандово-белый фон, крупный жирный чёрный/тёмно-синий заголовок сверху, синий/фиолетовый подзаголовок под ним.
- Множественные закруглённые панели с тонкой синей обводкой; заголовки секций — таблетки (pill-shape) индиго/тил цвета.
- Стеклянный светящийся 3D-мотив (куб / сеть / щит / весы) как центральный визуальный якорь, в духе существующей серии.
- Дружелюбный бело-синий робот-маскот (не логотип, не текст) в выделенной панели, где уместно.
- Нижняя горизонтальная плашка-степпер: пронумерованные кружки (1,2,3,4), каждый — иконка + жирный заголовок + короткая подпись, соединены пунктирной линией.
- Все подписи на изображении — на русском языке, орфографически точные, с буквой «ё» где нужно.
- Никаких водяных знаков, никаких реальных логотипов компаний (OpenAI/Anthropic/Sber) — только текстовые названия сервисов и обобщённые иконки (глобус, флаг, сервер).
- Названия продуктов (GigaChat, ChatGPT, Claude, YandexGPT) — как обычный текст на изображении, это нормально и нужно для ясности.

---

### 01_hero_kachestvo_i_bezopasnost.png

```
16:9 dense professional Russian infographic in the style of a modern data-journalism explainer poster (flat design with glossy 3D glass elements), light lavender-white background.

Bold black title top center: "Качество данных и цифровая безопасность"
Blue/purple subtitle beneath with arrow flow: "Чистые данные → Защищённые данные → Спокойная работа"

Central large glowing 3D glass motif: a stack of database disks flowing upward and transforming into a translucent glowing shield (indigo-to-cyan gradient light, wireframe network nodes inside), symbolizing data becoming protected.

Left column, pill-shaped section header "Что грозит без порядка": a bordered panel with icon+label rows: "Дубликаты и ошибки" (warning icon), "Утечка данных" (open padlock icon), "Штраф по закону" (ruble sign in warning triangle), "Потеря доверия" (broken handshake icon).

Right column, pill-shaped section header "Что даёт порядок": a bordered panel with icon+label rows: "Точные отчёты" (checkmark chart icon), "Защищённые данные" (closed padlock icon), "Законная работа" (scales of justice icon), "Спокойствие" (calm face icon).

Bottom right, a small highlighted rounded panel with a friendly photorealistic-hybrid white-and-blue robot mascot (glowing cyan eyes, round-cornered body) waving one hand and holding a small shield with a checkmark in the other, with a speech-bubble-style callout nearby.

Bottom horizontal stepper across the full width: four connected numbered circles with dotted line between them:
"1" icon of a database with a checkmark — "Качество данных" — "точность и порядок";
"2" icon of a padlock — "Безопасность" — "пароли и доступ";
"3" icon of a document with a ruble sign — "Закон" — "152-ФЗ и штрафы";
"4" icon of a shield with a clock — "Готовность" — "алгоритм при инциденте".

No watermarks, no real company logos, all text in correct Russian.
```

### 02_upravlenie_kachestvom_dannyh.png

```
16:9 dense professional Russian infographic, same house style as the reference "Очистка данных" and "Как обучают LLM" posters: light lavender-white background, bold black title, blue subtitle, multiple bordered panels with pill-shaped section headers, glossy 3D glass icons, numbered bottom stepper.

Bold black title: "Управление качеством данных"
Blue subtitle: "Уборка — это разово, качество — это система"

Left panel, pill header "Разовая уборка (уже пройдено)": small summary icon list — "Убрали объединённые ячейки", "Стандартизировали обозначения", "Разделили ФИО на ID" — each with a small checkmark, slightly muted/faded style to show it's already done.

Center: a glowing 3D glass gear-and-database hybrid icon labeled "Система качества", with five thin glowing lines radiating out to five small pill-badge cards arranged around it, each with an icon and one-word label: "Точность" (target icon), "Полнота" (filled grid icon), "Согласованность" (linked chain icon), "Актуальность" (clock icon), "Уникальность" (fingerprint icon).

Below, a "До / После" comparison panel with a dotted purple arrow: left side shows a messy list of file names in red strikethrough style ("итог2_финал.xlsx", "копия копии.xlsx", "ИСПРАВЛЕНО_v3.xlsx"); right side shows one clean file icon labeled "uspevaemost_2026-10-15.xlsx" with a small version-history clock icon next to it.

Bottom horizontal stepper, four numbered circles connected by dotted line: "1" — "Единый шаблон" — icon of a template/grid; "2" — "Регулярный аудит" — icon of a magnifying glass over a checklist; "3" — "Резервная копия" — icon of a cloud with an arrow; "4" — "Документация" — icon of a document with a question mark turning into a checkmark.

No watermarks, no real company logos, all text in correct Russian.
```

### 03_otvetstvennost_i_shtrafy.png

```
16:9 dense professional Russian infographic, same house style, light lavender-white background, bold black title, blue subtitle, glossy 3D glass central motif, bordered panels, numbered bottom stepper.

Bold black title: "Кто отвечает — и сколько это стоит"
Blue subtitle: "152-ФЗ: три категории ответственности"

Central glowing 3D glass motif: a pair of illuminated scales of justice (весы правосудия), indigo-to-cyan glow, with small ruble sign glyphs floating on one side of the scale.

Three vertical panels arranged below/around the scales, each with a pill-shaped header and a photorealistic-style flat icon:
1) Header "Физическое лицо", person icon, caption "рядовой преподаватель", a horizontal bar-meter showing a short colored bar, bold text "10 000 – 500 000 ₽".
2) Header "Должностное лицо", person-with-briefcase icon, caption "директор, завуч, член комиссии", a longer bar-meter, bold text "50 000 – 1 300 000 ₽".
3) Header "Организация", school-building icon, caption "отвечает всегда", a full-length red bar-meter, bold text "150 000 – 20 000 000 ₽".

Small callout ribbon banner across the top of the three panels: "Новые правила с 30 мая 2025 — штрафы выросли в разы" in bold white text on a dark navy ribbon.

Bottom horizontal stepper, four numbered circles: "1" — "ФИО и оценки" ; "2" — "Медсправки и диагнозы"; "3" — "Фото и видео"; "4" — "Даже номер студенческого" — each with a small relevant icon, illustrating what counts as personal data.

No watermarks, no real company logos, all text in correct Russian.
```

### 04_keys_minprosvescheniya.png

```
16:9 dense professional Russian infographic, same house style, light lavender-white background, bold black title, blue subtitle.

Bold black title: "Один кейс — два закона"
Blue subtitle: "Утечка 3,4 миллиона записей: 2023 против 2025"

Top strip: a small horizontal timeline with three icon-labeled points connected by a thin dotted line: "Июль 2023" (calendar icon) — "утечка в конкурсе «Большая перемена»"; "Роскомнадзор" (magnifying glass icon) — "находит базу в Telegram-каналах"; "Сентябрь 2023" (gavel/scales icon) — "суд, ч.1 ст.13.11 КоАП РФ".

Below, a large "До / После" comparison panel modeled on before/after training-stage comparisons: left bordered card labeled "Правила 2023" with a small single coin icon and bold text "60 000 ₽", caption "старые, мягкие правила"; a bold dotted purple arrow labeled "×250" pointing right; right bordered card with a red accent border labeled "Правила 2025" with a large glowing money-bag icon and bold text "10–15 000 000 ₽", caption "новые правила с 30 мая 2025".

Small side panel: a photorealistic-hybrid white-and-blue robot mascot with a surprised/shocked expression looking at the size difference between the two amounts.

Bottom banner ribbon: bold white text on dark navy "Законодательство стало жёстче в 250 раз".

No watermarks, no real company logos, all text in correct Russian.
```

### 05_cifrovaya_gigiena.png

```
16:9 dense professional Russian infographic, same house style, light lavender-white background, bold black title, blue subtitle.

Bold black title: "Цифровая безопасность шире одного закона"
Blue subtitle: "Пароли → Фишинг → Устройства → Резервные копии"

Central glowing 3D glass shield-with-lock motif, radiating four thin glowing connector lines out to four bordered panels arranged in a 2x2 grid, each with a pill-shaped header and icon-list:

Panel 1, header "Пароли и доступ 🔑": icon of a key, list items "Уникальный пароль для каждого сервиса", "Менеджер паролей", "Двухфакторная аутентификация (2FA)".
Panel 2, header "Фишинг ⚠️": icon of a fishing hook over an envelope, list items "Проверяйте адрес отправителя", "Не переходите по незнакомым ссылкам", "Не вводите пароль на подозрительных страницах".
Panel 3, header "Устройства 💻": icon of a locked laptop, list items "Блокируйте экран", "Обновляйте программы", "Осторожно с публичным Wi-Fi".
Panel 4, header "Резервные копии 💾": icon of a cloud with a download arrow, list items "Регулярно копируйте важные файлы", "Храните копию отдельно от оригинала".

Bottom horizontal stepper, four numbered circles connected by dotted line: "1" — "Проверьте пароли"; "2" — "Включите 2FA"; "3" — "Настройте бэкап"; "4" — "Научитесь узнавать фишинг" — each with a small matching icon.

No watermarks, no real company logos, all text in correct Russian.
```

### 06_sravnenie_treh_servisov.png

```
16:9 dense professional Russian infographic, same house style, light lavender-white background, bold black title, blue subtitle.

Bold black title: "GigaChat, ChatGPT, Claude — что можно педагогу"
Blue subtitle: "Один вопрос — три разных ответа"

Central small glowing 3D glass network-sphere motif, visually split into a green-glowing half and a red-glowing half, symbolizing compliant vs non-compliant.

Below, a wide scorecard table-like panel with three columns, each headed by a plain text product name (no logos) with a small generic icon (a Russian flag icon for GigaChat, a globe icon for ChatGPT, a globe icon for Claude): "GigaChat", "ChatGPT", "Claude". Five rows beneath with criterion labels on the left and a colored circular indicator icon (green circle with checkmark / yellow circle with exclamation mark / red circle with cross) in each column: "Серверы в РФ", "Соответствие 152-ФЗ", "Обучение на данных", "Корпоративная версия", "Можно для данных студентов РФ".

Small highlighted callout panel below the table: "GigaChat и YandexGPT — легальная альтернатива для данных студентов РФ" with two small Russian flag icons.

Bottom banner ribbon: bold white text on dark navy "Для данных граждан РФ — только российские серверы".

No watermarks, no real company logos (use plain text names and generic flag/globe icons only), all text in correct Russian.
```

### 07_algoritm_incidenta.png

```
16:9 dense professional Russian infographic, same house style, modeled on the reference's numbered process-stage layout (like "Pre-training → SFT → RLHF").

Bold black title: "Если данные утекли — действуйте по шагам"
Blue subtitle with arrow flow: "15 минут → 1 час → 1 сутки"

A horizontal glowing pill-shaped progress bar at top with three numbered stage markers (1, 2, 3) connected by a glowing line, labeled above each stage: "15 минут", "1 час", "1 сутки".

Three columns beneath, each a bordered panel under its stage number, with icon-list of actions:
Column 1 "Прекратить и зафиксировать": stop-hand icon, camera/screenshot icon, list items "Остановите загрузку", "Сделайте скриншоты", "Попробуйте удалить файл".
Column 2 "Сообщить и зафиксировать": phone icon, list items "Расскажите руководителю", "Смените пароли", "Запишите детали".
Column 3 "Оформить и подключить юриста": document-with-pen icon, list items "Объяснительная записка", "Юрист организации", "При необходимости — уведомить пострадавших".

Below the three columns, a red-bordered panel with header "Никогда не делайте так" and three small crossed-out icons with labels: "Скрывать инцидент", "Удалять доказательства", "Обвинять других".

Bottom right, a small reassuring highlighted panel with the friendly white-and-blue robot mascot giving a calm thumbs-up, next to text "В большинстве случаев это решаемо".

No watermarks, no real company logos, all text in correct Russian.
```

### 08_final_tri_vyvoda.png

```
16:9 dense professional Russian infographic, same house style, warm concluding mood, modeled on the reference's final "Итог: Chat Assistant" highlighted result panel.

Bold black title: "Берегите данные — и свою карьеру"
Blue subtitle: "Качество → Безопасность → Закон → Готовность"

Right side: a large highlighted rounded panel (soft indigo-to-cyan gradient background) featuring the friendly photorealistic-hybrid white-and-blue robot mascot waving, glowing cyan eyes, with a small speech bubble. Below the robot, four small badge chips stacked vertically, each with an icon and short bold label: "Качественные данные" (checkmark database icon), "Защищённый доступ" (padlock icon), "Законная работа" (scales icon), "Готовность к инциденту" (shield-with-clock icon).

Left side: a short vertical recap strip with five compact icon+one-line rows matching the lecture's five conclusions: "Качество — система, не уборка", "Закон стал жёстче в 250 раз", "Безопасность шире одного закона", "Проверка сервиса — 10 минут", "В России есть легальные инструменты".

Bottom full-width banner ribbon, dark navy background, bold white text: "Данные без действий — просто цифры. Данные с действиями — забота о студентах и о себе."

No watermarks, no real company logos, all text in correct Russian.
```

## 3. Технические требования (без изменений)

- Дизайн-система страницы и скрипты (лайтбокс со скачиванием `iivobrazovanii-club_<имя>.png`, фуллскрин для iframe, IntersectionObserver, scroll-fade) — без изменений.
- Ссылка «← Оглавление» и ссылка клуба в футере — уже на месте.
- Три интерактивные визуализации (`shtraf_kalkulyator.html`, `sravnenie_servisov.html`, `algoritm_incidenta.html`) — без изменений.
- Тест `tests/check_bezopasnost_dannyh_page.py` обновлён под новую структуру (id s1–s9, маркеры обоих новых блоков, 8 картинок).
