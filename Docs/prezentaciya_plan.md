# План сайта-презентации «ИИ как помощник предпринимателя»

Одна страница-лонгрид `index.html` + пять интерактивных демо в `web/`. Показывается с проектора во время вебинара и остаётся участникам после него.

**Брендирование — заказчика.** Основной бренд «Сделано в Атомграде»: знак `assets/logo_atomgrad_znak.png` в навбаре, в hero и в подвале. Знак ведущего «Просто делай» (`assets/logo_prosto_delay.svg`) — только в подвале, в блоке «Ведущий вебинара».

Палитра и типографика сняты с сайта проекта — сделановатомграде.рф: синий `#20599D` (основной), красный `#E31E24` (редкий акцент), текст `#111418`, приглушённый `#6B7380`, границы `#DDE6EE`, фон белый с чередованием полос `#F4F7FA`. Шрифт Montserrat с системным запасным. Карточки со скруглением 24px, кнопки и бейджи — пилюли, заголовки крупные и жирные с отрицательным межбуквенным. Зелёного в палитре нет: «хорошо» и «получилось» показываются синим, «нельзя» и «ошибка» — красным.

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
| 7 | `s7` | Контроль, риски и деньги | 08, **11** | `kalkulyator_ekonomii.html` |
| 8 | `s8` | Ваш первый помощник | 09 | `matrica_processov.html` |
| 9 | `s9` | Где брать готовое | 10 | `karta_servisov.html` |
| — | `checklist` | Чек-лист готовности | — | localStorage |
| — | `quiz` | Проверьте себя | — | 6 вопросов |
| — | `final` | Что забрать с собой | — | — |

## Интерактивные демо

1. **`chat_vs_agent.html`** — переключатель «чат / помощник» на одной задаче. Слева запрос, справа — что происходит: у чата один шаг и текст на выходе, у помощника цепочка шагов и готовый документ.
2. **`konstruktor_agenta.html`** — шесть тумблеров (роль, цель, инструкция, знания, память, ограничения). Участник включает их и видит, как меняется ответ на жалобу клиента. Повторяет блок 2 вебинара, чтобы можно было переиграть дома.
3. **`kalkulyator_ekonomii.html`** — часы в неделю × ставка × доля процесса против стоимости подписки. Показывает экономию в месяц, за год и срок окупаемости настройки.
4. **`matrica_processov.html`** — матрица «частота × рутинность». Участник расставляет свои процессы, правый верхний угол подсвечивается как кандидат на первый пилот.
5. **`karta_servisov.html`** — карточки сервисов с фильтром по доступности (без карты и VPN / нужна зарубежная карта / работает на своём компьютере) и по задаче.

---

# Промпты для генерации инфографики

Все — 16:9, не меньше 1672×941, белый фон, текст по-русски с буквой «ё». Файлы кладём в `png/prezentaciya/` под именами `01_...png` … `10_...png`.

**Логотип не просим рисовать** — генераторы искажают знаки. Он накладывается на странице средствами HTML.

## Атомная стилистика: сквозной приём всей серии

Проект называется «Сделано в Атомграде», у заказчика в знаке — атом. Поэтому вся серия строится на визуальном языке атомной энергетики и науки. Это не украшение: **каждая метафора работает на смысл блока**, иначе картинка превращается в открытку.

**Фоновый слой — одинаковый во всех одиннадцати картинках.** Он и делает серию серией:

- Одна-две **огромные орбитальные окружности**, уходящие за края кадра, прозрачностью 6–8 % синего `#20599D` — как будто кадр вырезан из схемы атома.
- **Пунктирные эллиптические траектории** электронов, тонкие, прозрачностью 10 %, пересекающиеся под разными углами.
- Редкие мелкие **точки-электроны** на этих траекториях, прозрачностью 15 %.
- Поверх — привычная **точечная сетка** `#DDE6EE`, как на сайте проекта.

Фон должен читаться как еле заметный водяной знак: с последнего ряда зала его почти не видно, а вблизи он собирает всю серию в одно целое. Если генератор делает фон навязчивым — в промпте усиливаем формулировку «barely visible, 6% opacity, must not compete with text».

**Композиционные метафоры по блокам** — по одной на картинку, чтобы приём не приелся:

| № | Метафора | Почему она про смысл блока |
|---|---|---|
| 01 | Модель атома | Ядро — помощник, электроны — сценарии применения вокруг него |
| 02 | Одиночная частица против цепной реакции | Чат — один удар и всё; агент — реакция, которая идёт сама |
| 03 | Атом с шестью электронами | Шесть частей помощника на своих орбитах вокруг ядра |
| 04 | Топливный стержень: пустой и заряженный | Без документов помощник холостой, с ними — выдаёт энергию |
| 05 | Пульт управления энергоблоком | Инструменты — это приборы и рычаги, к которым он получил доступ |
| 06 | Топливная таблетка | Skill — маленькая капсула, в которую спрессован процесс |
| 07 | Стандартный разъём контура | MCP — единый стык вместо самодельных переходников |
| 08 | Защитная оболочка, три барьера | Зоны доступа — контуры безопасности вокруг реактора |
| 09 | Управляемая цепная реакция | Три ступени внедрения — нарастающий, но контролируемый каскад |
| 10 | Таблица элементов | Сервисы как элементы: символ, номер, группа |

---

## 01 · Обзорная (hero)

```
16:9 dense professional Russian infographic in the style of a modern data-journalism explainer poster
(flat design with glossy 3D glass elements), clean white background.

BACKGROUND LAYER (same across the whole series): one huge orbital circle running off the edges of the
frame and two crossing dashed elliptical electron trajectories, deep blue #20599D at only 6-8% opacity,
with a few small electron dots on the paths at 15% opacity. Over it a subtle light-grey dotted grid
(#DDE6EE dots). The background must be barely visible and must not compete with the text.

Bold near-black (#111418) title top center in a geometric sans-serif (Montserrat-like), tight
letter-spacing: "ИИ как помощник предпринимателя"
Deep blue (#20599D) subtitle beneath: "От вопроса в чате — до сотрудника, который доводит дело до конца"

CENTRAL MOTIF — an atom model rendered as glowing 3D glass: a solid deep blue nucleus labelled
"ПОМОЩНИК", and four electrons orbiting it on elliptical glass paths. Each electron is a small
labelled sphere: "продажи", "закупки", "поддержка", "документы". The orbits are deep blue #20599D,
the nucleus has a soft inner glow.

Left column, deep blue (#20599D) pill-shaped section header "Что он уже делает": white panel with
thin #DDE6EE border and 24px rounded corners, icon+label rows:
"Разбирает сайт конкурента" (magnifier icon), "Пишет КП по вашему прайсу" (document icon),
"Отвечает на жалобы" (chat bubble icon), "Готовит протокол планёрки" (microphone icon).

Right column, deep blue (#20599D) pill-shaped section header "Из чего он состоит": white panel with
thin #DDE6EE border and 24px rounded corners, icon+label rows:
"Роль и цель" (badge icon), "Знания — ваши документы" (folder icon),
"Инструменты — почта, файлы, сайты" (wrench icon), "Ограничения — что нельзя" (shield icon).

Bottom horizontal stepper across the full width: four connected numbered circles styled as small
atoms, linked by a dotted trajectory line:
"1" lightning icon — "Сегодня" — "15 минут, первый результат";
"2" gear icon — "За неделю" — "процесс и документы";
"3" capsule icon — "За месяц" — "упакованное умение";
"4" plug icon — "Дальше" — "подключение к вашим системам".

No watermarks, no real company logos, all text in correct Russian.
```

## 02 · Чат против помощника

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements, white background.

BACKGROUND LAYER: huge orbital circle off the frame edges plus dashed elliptical electron
trajectories, deep blue #20599D at 6-8% opacity, few electron dots at 15%, over a subtle #DDE6EE
dotted grid. Barely visible, must not compete with the text.

Bold near-black (#111418) title top center in a geometric sans-serif, tight letter-spacing:
"Чат отвечает — помощник делает"
Deep blue (#20599D) subtitle beneath: "Одна и та же задача, два разных результата"

Split composition, vertical dashed divider down the middle.

LEFT HALF — the "single particle" metaphor. Pill header "ЧАТ" in muted grey (#6B7380).
One grey glass particle hits a wall and stops: a single short arrow from the particle to a plain
sheet of paper labelled "Текст, который вы дальше доделываете руками". Nothing happens after it.
Small grey caption: "Один шаг · знает только общее · вы дорабатываете".

RIGHT HALF — the "chain reaction" metaphor. Pill header "ПОМОЩНИК" in deep blue (#20599D).
One glowing blue particle strikes a nucleus and sets off a branching chain: four sequential glass
nodes connected by glowing blue trajectories, each labelled — "читает задачу" (eye icon),
"заходит на сайт" (globe icon), "считает по прайсу" (calculator icon), "собирает документ"
(document icon). The chain ends in a finished document with a deep blue check mark, labelled
"Готово — можно отправлять".
Small caption: "Столько шагов, сколько нужно · пользуется вашими данными · доводит до результата".

Bottom horizontal bar, deep blue pill header "Простой тест": one wide white panel with large text:
"Надо доделывать руками — это был чат. Можно отправить клиенту — это был помощник."

No watermarks, no real company logos, all text in correct Russian.
```

## 03 · Шесть частей помощника

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements, white background.

BACKGROUND LAYER: huge orbital circle off the frame edges plus dashed elliptical electron
trajectories, deep blue #20599D at 6-8% opacity, few electron dots at 15%, over a subtle #DDE6EE
dotted grid. Barely visible.

Bold near-black (#111418) title top center in a geometric sans-serif, tight letter-spacing:
"Из чего собран помощник"
Deep blue (#20599D) subtitle beneath: "Шесть частей. Настройка — час, польза — годы"

CENTRAL MOTIF — a full atom model as the structural diagram of the assistant. A glowing deep blue
glass nucleus in the centre labelled "ПОМОЩНИК". Six electrons orbit it on three intersecting
elliptical glass paths — exactly six, evenly distributed. Each electron is a labelled glass sphere
connected by a thin glowing line to its own white card with a #DDE6EE border and 24px rounded corners:

"РОЛЬ" (name badge icon) — "Кем он себя считает: управляющий кофейней, а не робот";
"ЦЕЛЬ" (target icon) — "Ради чего: вернуть клиента, а не закрыть обращение";
"ИНСТРУКЦИЯ" (numbered list icon) — "Порядок действий и формат ответа";
"ЗНАНИЯ" (folder icon) — "Ваш прайс и регламенты — иначе выдумает";
"ПАМЯТЬ" (notebook icon) — "Что помнит между обращениями";
"ОГРАНИЧЕНИЯ" (shield icon) — "Чего не делает никогда и когда зовёт человека".

Bottom horizontal bar with a before/after pair separated by a dashed arrow:
left side, red (#E31E24) crossed-out speech bubble: "Приносим извинения за доставленные неудобства";
right side, blue-outlined document: "Ирина, сырники правда были пересушены — повару указали.
Зайдите на этой неделе, кофе за наш счёт."

No watermarks, no real company logos, all text in correct Russian.
```

## 04 · Откуда берётся враньё

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements, white background.

BACKGROUND LAYER: huge orbital circle off the frame edges plus dashed elliptical electron
trajectories, deep blue #20599D at 6-8% opacity, over a subtle #DDE6EE dotted grid. Barely visible.

Bold near-black (#111418) title top center in a geometric sans-serif, tight letter-spacing:
"Почему он выдумывает цены — и как это лечится"
Deep blue (#20599D) subtitle beneath: "Нейросеть начитана, но в вашей компании не работала"

METAPHOR — a fuel rod, empty versus loaded.

LEFT HALF, pill header "БЕЗ ВАШИХ ДОКУМЕНТОВ" in red (#E31E24): a tall glass fuel rod standing
empty and unlit, grey and cold. Around it float generic book and website icons that never enter it.
An arrow points to a price tag "≈ 1 200 ₽/м" stamped with a red crossed-out mark,
caption "Цифра правдоподобная. И выдуманная."

RIGHT HALF, pill header "С ВАШИМИ ДОКУМЕНТАМИ" in deep blue (#20599D): the same fuel rod, now
loaded with stacked glowing blue pellets, each pellet labelled — "Прайс", "Регламент", "Договор" —
and the whole rod emitting a soft blue glow. An arrow points to a price tag "1 450 ₽/м" with a deep
blue check mark and a small quote block beneath: "источник: прайс, строка 14".

Bottom horizontal stepper across the full width: four numbered circles styled as small atoms,
linked by a dotted trajectory:
"1" folder icon — "Соберите" — "прайс, регламенты, скрипты";
"2" upload icon — "Загрузите" — "прямо файлами, ничего не переписывая";
"3" quote icon — "Требуйте источник" — "«покажи, откуда взял»";
"4" refresh icon — "Обновляйте" — "поменялся прайс — поменяйте файл".

No watermarks, no real company logos, all text in correct Russian.
```

## 05 · Инструменты помощника

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements, white background.

BACKGROUND LAYER: huge orbital circle off the frame edges plus dashed elliptical electron
trajectories, deep blue #20599D at 6-8% opacity, over a subtle #DDE6EE dotted grid. Barely visible.

Bold near-black (#111418) title top center in a geometric sans-serif, tight letter-spacing:
"Инструменты: помощник выходит за пределы чата"
Deep blue (#20599D) subtitle beneath: "Консультант по телефону становится сотрудником с доступами"

METAPHOR — a control room desk of a power plant, seen head-on and stylised as clean flat design.

CENTRAL MOTIF: a wide curved control console in deep blue glass. Above it a bank of six round
instrument dials, each dial captioned with the tool it stands for: envelope "почта",
spreadsheet "таблицы", calendar "календарь", folder "файлы", globe "сайты и поиск",
microphone "запись встреч". Every dial is connected to a small glass assistant core sitting at the
centre of the console by a glowing blue line.

Left column, deep blue (#20599D) pill-shaped section header "Что он делает сам": white panel with
thin #DDE6EE border and 24px rounded corners, icon+label rows:
"Читает входящие письма" (envelope icon), "Ищет и проверяет в интернете" (globe icon),
"Считает и сводит в таблицу" (calculator icon), "Расшифровывает планёрку" (microphone icon).

Right column, deep blue (#20599D) pill-shaped section header "Пример сквозной задачи": white panel
with thin #DDE6EE border and 24px rounded corners, containing a vertical numbered chain:
"1 Найти письма поставщиков за неделю" → "2 Вытащить позиции и цены" →
"3 Свести в таблицу и отсортировать" → "4 Прислать готовый файл".

Bottom horizontal bar with a red (#E31E24) left border, pill header "Граница": wide white panel:
"Он ошибается: не так понял письмо, взял не тот прайс. Право отправлять письма и платить деньги
ему не дают."

No watermarks, no real company logos, all text in correct Russian.
```

## 06 · Skills

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements, white background.

BACKGROUND LAYER: huge orbital circle off the frame edges plus dashed elliptical electron
trajectories, deep blue #20599D at 6-8% opacity, over a subtle #DDE6EE dotted grid. Barely visible.

Bold near-black (#111418) title top center in a geometric sans-serif, tight letter-spacing:
"Skills: один раз описал — дальше в два слова"
Deep blue (#20599D) subtitle beneath: "Инструкция для нового сотрудника, только читает её помощник"

METAPHOR — a fuel pellet: a whole process pressed into one small dense capsule.

LEFT HALF, pill header "КАЖДЫЙ РАЗ ЗАНОВО" in muted grey (#6B7380): a large loose scattered pile of
grey paper sheets densely filled with small text lines, spilling out of frame, a tired clock icon in
the corner. Caption: "Полстраницы задания. Каждый раз."

A dashed arrow pointing right, labelled "спрессовали".

RIGHT HALF, pill header "ОДИН РАЗ И НАВСЕГДА" in deep blue (#20599D): one small glowing deep blue
glass pellet-capsule sitting on a pedestal, with a neat label tag reading "рассылка по базе".
Next to it a tiny speech bubble containing just "сделай рассылку по этому файлу".
A thin cutaway line shows the pellet's inside: three compressed layers labelled
"когда применять", "что делать по шагам", "каких ошибок избегать".
Caption: "Процесс внутри. Снаружи — имя."

Bottom horizontal stepper across the full width: four numbered circles styled as small atoms,
linked by a dotted trajectory:
"1" repeat icon — "Повторяется" — "чаще раза в неделю";
"2" document icon — "Один формат" — "результат всегда одинаковый";
"3" speech icon — "Объясняли дважды" — "сотруднику приходилось повторять";
"4" moon icon — "Делаете вечером" — "потому что днём некогда".
Caption under the stepper: "Сошлись три пункта из четырёх — это ваш первый skill."

No watermarks, no real company logos, all text in correct Russian.
```

## 07 · MCP — единый разъём

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements, white background.

BACKGROUND LAYER: huge orbital circle off the frame edges plus dashed elliptical electron
trajectories, deep blue #20599D at 6-8% opacity, over a subtle #DDE6EE dotted grid. Barely visible.

Bold near-black (#111418) title top center in a geometric sans-serif, tight letter-spacing:
"MCP: единый разъём для помощника"
Deep blue (#20599D) subtitle beneath: "Раньше под каждую программу — свой переходник. Теперь один стандарт"

METAPHOR — pipework of a plant circuit: chaotic homemade joints versus one standard flange.

LEFT HALF, pill header "БЫЛО" in red (#E31E24): a tangled mess of pipes of different diameters
joined by mismatched homemade adapters, leaking, each junction a different shape and colour,
red warning marks at the joints. Caption: "Каждое подключение — отдельная разработка".

RIGHT HALF, pill header "СТАЛО" in deep blue (#20599D): one clean closed circuit of deep blue glass
pipes meeting at a single standard round flange connector in the centre. Six identical branch pipes
run out of the flange, each neatly labelled: "Почта", "Календарь", "Таблицы", "Telegram", "CRM",
"Файлы". Soft blue glow along the circuit showing flow. Caption: "Один стык — любой помощник".

Bottom horizontal bar split into three pill-headed zones, styled as containment status indicators:
deep blue "Работает" — "почта, календари, таблицы, файлы, Telegram";
amber "Работает с оговорками" — "CRM, отраслевые сервисы, часть коннекторов сырая";
red (#E31E24) "Пока нет" — "глубокая интеграция с учётными системами без разработчика".

No watermarks, no real company logos, all text in correct Russian.
```

## 08 · Три зоны доступа

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements, white background.

BACKGROUND LAYER: huge orbital circle off the frame edges plus dashed elliptical electron
trajectories, deep blue #20599D at 6-8% opacity, over a subtle #DDE6EE dotted grid. Barely visible.

Bold near-black (#111418) title top center in a geometric sans-serif, tight letter-spacing:
"Что помощнику можно, а что нельзя"
Deep blue (#20599D) subtitle beneath: "Генерация — ему, отправка — вам. По крайней мере первые два месяца"

METAPHOR — containment barriers around a reactor: three concentric protective shells.

CENTRAL MOTIF: a cross-section of three concentric containment rings around a small glowing core
labelled "ВАШ БИЗНЕС". The innermost ring is deep blue, the middle amber, the outer red (#E31E24),
each drawn as a thick glass shell. A thin line runs from every ring outward to its own white panel
with #DDE6EE border and 24px rounded corners:

Inner blue panel, pill header "ДЕЛАЕТ САМ": icon+label rows — "Черновики писем" (pencil icon),
"Расшифровки встреч" (microphone icon), "Разбор конкурентов" (magnifier icon),
"Поиск и аналитика" (chart icon).

Middle amber panel, pill header "ДЕЛАЕТ И ПОКАЗЫВАЕТ": icon+label rows — "Письма клиентам"
(envelope icon), "Ответы на отзывы" (star icon), "Документы и счета" (document icon).

Outer red panel, pill header "НЕ ТРОГАЕТ": icon+label rows — "Платежи" (banknote icon),
"Договоры" (stamp icon), "Персональные данные клиентов" (passport icon),
"Кадровые решения" (people icon), "Обещания скидок" (percent icon).

Bottom horizontal bar, deep blue pill header "Персональные данные": wide white panel:
"Что именно можно загружать — на следующей схеме. Три группы: не грузим никогда,
грузим после замены, грузим как есть."

No watermarks, no real company logos, all text in correct Russian.
```

## 09 · Лестница внедрения

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements, white background.

BACKGROUND LAYER: huge orbital circle off the frame edges plus dashed elliptical electron
trajectories, deep blue #20599D at 6-8% opacity, over a subtle #DDE6EE dotted grid. Barely visible.

Bold near-black (#111418) title top center in a geometric sans-serif, tight letter-spacing:
"Ваш первый помощник: сегодня, за неделю, за месяц"
Deep blue (#20599D) subtitle beneath: "Порядок нарушать нельзя — девять из десяти провалов начинаются с третьей ступени"

METAPHOR — a controlled chain reaction that grows step by step.

CENTRAL MOTIF: three ascending stages drawn as a widening cascade of glass particles. Stage one is a
single particle, stage two splits into three, stage three into nine — all deep blue #20599D, linked
by glowing trajectories, contained inside a thin outlined boundary that shows the reaction is
controlled, not runaway. Each stage has its own white panel with #DDE6EE border and 24px rounded
corners beside it:

Stage 1 panel, pill header "СЕГОДНЯ · 15 МИНУТ": icon+label rows — "Дайте роль и цель" (badge icon),
"Приложите один документ" (folder icon), "Сделайте один рабочий текст" (document icon).
Caption: "Цель — не автоматизация, а первое «работает»".

Stage 2 panel, pill header "ЗА НЕДЕЛЮ": icon+label rows — "Выберите процесс по матрице" (grid icon),
"Опишите шесть частей" (list icon), "Прогоните двадцать раз" (repeat icon),
"Замерьте время до и после" (stopwatch icon).

Stage 3 panel, pill header "ЗА МЕСЯЦ": icon+label rows — "Упакуйте в skill" (capsule icon),
"Дайте инструменты" (wrench icon), "Поставьте подтверждение" (check icon),
"Назначьте ответственного и метрику" (person icon).

Bottom horizontal bar, deep blue pill header "Выбор процесса": a small 2x2 matrix diagram with axes
"как часто" and "насколько рутинно", the top-right cell highlighted deep blue and labelled
"ваш первый пилот".

No watermarks, no real company logos, all text in correct Russian.
```

## 10 · Карта сервисов

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements, white background.

BACKGROUND LAYER: huge orbital circle off the frame edges plus dashed elliptical electron
trajectories, deep blue #20599D at 6-8% opacity, over a subtle #DDE6EE dotted grid. Barely visible.

Bold near-black (#111418) title top center in a geometric sans-serif, tight letter-spacing:
"Где брать помощников и готовые решения"
Deep blue (#20599D) subtitle beneath: "Три группы: начать без вложений, вырасти, взять готовое"

METAPHOR — a periodic table. Every service is drawn as an element tile: a square white card with
#DDE6EE border and rounded corners, a small number in the top-left corner, a short two-letter symbol
in large bold deep blue in the centre, and the full service name in small text underneath. Tiles are
arranged in three labelled groups, exactly like groups of a periodic table.

Group 1, deep blue (#20599D) pill header "БЕЗ ВЛОЖЕНИЙ И БЕЗ КАРТЫ": a row of element tiles for
Russian-accessible assistants, with a one-line use-case caption under each — «чат-помощник в
браузере», «помощник в поиске», «сборка помощника со своими документами».

Group 2, amber pill header "КОГДА НУЖНО БОЛЬШЕ": element tiles for international services, each
carrying a small amber corner tag "нужна зарубежная карта". Captions describe what they add:
длинные документы, работа с файлами, длинные цепочки шагов.

Group 3, muted grey pill header "ГОТОВЫЕ РЕШЕНИЯ": element tiles — "Каталоги агентов",
"Библиотеки готовых умений", "Каталоги коннекторов", "Сообщества и разборы".

Bottom horizontal bar, deep blue pill header "Правило выбора": wide white panel:
"Начните с того, что открывается в браузере без карты. Переходите дальше, только когда упрётесь
в конкретное ограничение."

No watermarks, no real company logos, all text in correct Russian.
```

## 11 · Какие данные можно отдавать помощнику

Ставится в секции 7, между таблицей зон доступа и карточками-светофором. Файл — `png/prezentaciya/11_kakie_dannye.png`.

```
16:9 dense professional Russian infographic, flat design with glossy 3D glass elements, white background.

BACKGROUND LAYER: huge orbital circle off the frame edges plus dashed elliptical electron
trajectories, deep blue #20599D at 6-8% opacity, over a subtle #DDE6EE dotted grid. Barely visible.

Bold near-black (#111418) title top center in a geometric sans-serif, tight letter-spacing:
"Какие данные можно отдавать помощнику"
Deep blue (#20599D) subtitle beneath: "Три группы. Первая не спасается обезличиванием"

METAPHOR — a three-stage airlock: material passes through gates that filter it.

CENTRAL LAYOUT: three tall vertical panels side by side, equal width, white fill, #DDE6EE border,
24px rounded corners, each with a thick 6px colored top edge and a pill header in that color.

LEFT PANEL, red (#E31E24) top edge, pill header "НЕ ГРУЗИМ НИКОГДА": a closed red glass padlock
icon at the top, then icon+label rows — "Паспорт, СНИЛС, ИНН" (passport icon),
"Карты и выписки" (bank card icon), "Медицинские документы" (cross icon),
"Фото лица, запись голоса" (face-scan icon), "Данные детей" (small figure icon),
"Пароли и доступы" (key icon), "База клиентов целиком" (stacked database icon),
"Зарплаты и кадровые дела" (folder icon).
Footer strip inside the panel, light red fill: "Обезличивание здесь не помогает"

MIDDLE PANEL, amber (#B45309) top edge, pill header "ТОЛЬКО ПОСЛЕ ЗАМЕНЫ": an amber glass funnel
or filter icon at the top, then four before-after rows, each showing the old value struck through
in red and an arrow to the new value in green (#2E7D32):
"Иванов Пётр → Клиент А"
"+7 927 431-15-47 → +7 9ХХ ХХХ-ХХ-47"
"ул. Садовая, 8 → СНТ «Мичуринский»"
"ДГ-2026-0147 → Договор 1"
Footer strip inside the panel, light amber fill: "Замена — до загрузки, а не после"

RIGHT PANEL, green (#2E7D32) top edge, pill header "МОЖНО КАК ЕСТЬ": an open green glass gate icon
at the top, then icon+label rows — "Регламенты и инструкции" (document icon),
"Прайс" (price tag icon), "Скрипты продаж" (speech bubble icon),
"Тексты сайта" (globe icon), "Данные юрлиц из ЕГРЮЛ" (building icon),
"Суммы, даты, объёмы" (chart icon).
Footer strip inside the panel, light green fill: "И это 80% вашей работы"

Bottom horizontal bar, deep blue pill header "Правило для адреса": wide white panel:
"Оставляем тот адрес, по которому нельзя постучать в конкретную дверь. Многоквартирный дом —
улицу и дом можно, квартиру нет. Частный сектор и СНТ — номер дома убираем."

Bottom numbered stepper strip: 11 of 11.

No watermarks, no real company logos, all text in correct Russian.
```

---

# Что нужно от заказчика перед публикацией

- **Ссылки на ведущего** в подвале проставлены: почта `ilya1986@mail.ru`, Telegram `@churilov_ai`, канал в MAX, ВКонтакте `vk.ru/ilyachurilov`, сделановатомграде.рф.
- **Подтверждение имени** в подвале: сейчас указан «Илья Чурилов» — выведено из адреса почты.
- **Инфографика** — одиннадцать PNG по промптам выше в `png/prezentaciya/`, все готовы. Формат серии: 1672×941, вес 600–750 КБ после `pngquant --quality=65-85`.

## Если генератор не справляется с атомным фоном

Частая беда: фоновые орбиты выходят слишком яркими и спорят с текстом. Что делать по порядку:

1. Усилить формулировку: `background orbits at 5% opacity, barely perceptible, must not compete with foreground text`.
2. Если не помогает — убрать фон из промпта совсем и генерировать чистую картинку, а орбиты добавить отдельным слоем в редакторе поверх, режимом наложения с прозрачностью.
3. Крайний вариант — оставить только точечную сетку `#DDE6EE`: серия всё равно держится на палитре, композиционных метафорах и общей типографике.

**Чего не делать:** не просить генератор рисовать радиационные знаки, предупреждающие «трилистники» и грибовидные облака. Атомная тема здесь — про энергию, науку и точность, а не про опасность. Заказчику это важно.
