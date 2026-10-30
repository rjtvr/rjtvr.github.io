# Design reference: "Town Square"

How the pixel-art portfolio design is built, and why. Read this before changing the look or layout of `index.html`, `workshop.html` or `assets/site.css`. Exact values (colours, sizes) live in `site.css`; this file explains the system around them.

## Vocabulary

The design is a village **Town Square** with a **Quest Board**. Keep these names in copy, comments and class names.

| Term | What it is | Where |
|---|---|---|
| Town Square | The home page and the brand in the header | `index.html` |
| Workshop | The all-projects page | `workshop.html` |
| Board | Wooden frame (`.board`) around a cork or plank surface (`.board-inner`) | both pages |
| Board sign | Brown plaque hanging over the board's top edge ("Guild Hall · Quest Board") | `.board-sign` |
| Note | A card pinned to the board: hero, Now, Featured builds, Toolbelt, Achievements, Quest log | `.card.note` |
| Pin | The round pin on each note's top edge | `.card.note::before`, colour via `--pin` |
| Shelves | The Workshop's plank background, in place of cork | `.board-inner.shelves` |
| Project card | One project on the Workshop, unpinned | `.card.project` |
| Chip | A skill tag with a coloured drop shadow (blue = frontend, teal = backend) | `.badge.chip`, `.chip.be` |
| Leveling up | Skills in training (Go, Python), shown with an XP bar | `.xp-row`, `.xp` |
| Quest log | The career timeline; the dashed last entry is "Next" | `.quests`, `li.next` |
| Contact sign | "Send a carrier pigeon" panel below the board | `.contact` |
| Side quests | Personal Go/Python projects. In the mockup, intentionally not built yet | (none) |
| Splash screen | "Town Square" sign over a pinned note with the avatar, name and a segmented loading bar, shown on the home page before the board | `.splash-screen`, `.show-splash` |

## Stack

- [Oat](https://oat.ink) 1.0.0 CSS from jsDelivr, pinned with SRI. Oat styles semantic HTML and puts everything in cascade layers, so unlayered rules in `site.css` win without extra specificity. Theme Oat through its variables in the `:root` block of `site.css`, never by editing Oat.
- Pages load `assets/site.min.css`, generated from `site.css`. Edit only `site.css`, then regenerate (see CLAUDE.md).
- Oat pieces in use: `.container`, `.row` / `.col-*` (12-column grid, stacks below 769px), `.hstack` / `.vstack`, `.card`, `.badge`, `a.button`, `ul.unstyled`, `gap-*`, `mt-*`. Oat's JS is not loaded.
- Fonts: Pixelify Sans (body, headings) and Silkscreen (caps labels and metadata, via `--font-mono`), both from Google Fonts.
- Light-only: `color-scheme: light` pins Oat's `light-dark()` values. There is no dark theme.

## Tokens

All tokens are named in `:root` of `site.css`:

- **Ink:** `--ink` for text and every outline, plus `--ink-soft` / `--ink-mute` for secondary text.
- **Surfaces:** `--paper`, `--cream`, and the five `--note-*` note colours.
- **World:** `--ground` (the green grass page background), `--wood`, `--wood-dark`, `--sky`.
- **Accents:** `--accent` (rust red, links and primary buttons), `--teal`, `--blue`, `--gold`, `--pin-red`.

Shared rules:
- No border radius anywhere; Oat's radius tokens are set to 0.
- Outlines are solid `--ink`: 2px on chips and tags, 3px on notes and buttons, 4px on the board and header.
- Shadows are hard offsets, never blurred: `--note-shadow` on notes, `4px 4px 0 var(--ink)` on buttons.
- Notes tilt slightly with an inline `--tilt` (for example `style="--tilt: -0.7deg"`). Hero and Quest log stay straight.

## Layout

- The home page board stacks: hero note, then a `.row` with Now + Featured builds (`col-6` each), a `.row` with Toolbelt + Achievements (`col-7` / `col-5`), then the Quest log note. The contact sign and footer sit below the board.
- Workshop: a heading row (`.workshop-head`), then `.row.projects` with `col-4` project cards. Cards are three across on desktop, two at 769–1080px, one below that.
- Featured builds link to Workshop cards by id (`workshop.html#pegasus`). Keep card ids lowercase and hyphenated.
- The two pages repeat the same `<head>` and header markup; change both together.

## Phone layout

- One `@media (max-width: 600px)` block at the end of `site.css` holds every phone rule, following the mobile frames of the mockup. Desktop rules stay outside it, so phone changes can't alter desktop. After a change, compare desktop renders before and after.
- `.hide-sm` / `.show-sm` swap copy between widths: shorter achievement captions, the footer line break, the Workshop's bottom Back button.
- Phone-only behaviour:
  - Hamburger menu on the home page (an inline script in `index.html`). Links stay visible without JS, because the `js` class on `<html>` gates hiding them.
  - The Workshop header shows only the current-page label (`.current-only-sm`).
  - Hero facts render as chips.
  - Featured builds become full-row links with arrows.
  - Achievements become a 2×2 grid of tiles.
  - The Quest log becomes a vertical timeline.
  - Contact buttons stack full-width.
- Notes don't tilt on phones.

## Avatar

- 16×16 pixel art as inline SVG (`viewBox="0 0 16 16"`, `shape-rendering="crispEdges"`). It's drawn at 128px on desktop (8px per art pixel) and 80px on phones.
- Its layers are `.av-bob` (whole figure), `.av-body`, `.av-head` and `.av-eyes` (the two blue glints in the goggles).
- **On first load:** it rises 3 art pixels into its frame in steps, then blinks twice. The animation is pure CSS, plays once, and is off under `prefers-reduced-motion`.
- **Motion rule:** animate in whole art pixels with `step-end` / `steps()` timing, never smooth tweens, so it stays pixel art. Inside the SVG, CSS `1px` equals one art pixel.

## Splash screen

- Home page only, once per browser session (`sessionStorage` key `splash-seen`). A `<head>` script adds `.show-splash` to `<html>` before first paint; the end-of-body script removes it after 5s or on any tap or key.
- Timeline: the 12-segment bar fills in steps from 0.3s to 4.5s, then the screen fades out in 4 steps (4.6–5s). Keep the CSS timings and the 5000ms timeout in step.
- The hero avatar intro is held while the splash shows and plays when it closes.
- Without JS, or with storage blocked, there is no splash. Under reduced motion it still shows and can be skipped, but the dots and fade are static.

## Gotchas

- **Box sizing:** the mockup sizes outlined boxes with borders *added outside* the width, but Oat sets `box-sizing: border-box`. Any outlined marker or square copied from the mockup needs its border width added to its size, or it renders too small and sits off-centre. The quest log markers needed this: 22px on desktop, 20px on phones.
- **Italics:** Oat italicises `<i>`; the hero-fact separators reset it with `.facts i { font-style: normal }`.
- **Oat's `.hstack` wraps** by default. Set `flex-wrap: nowrap` on any `.hstack` turned into a column, or its items shrink to their content width (the phone menu needed this).
- **Narrow phones:** the hero name column is a size container (`hero-name`). When it is narrower than "Verma" (about 104px, so up to roughly 330px viewports), `.surname` is hidden visually, so the heading reads "Rajat" rather than breaking mid-word. Screen readers still hear the full name. If the h1 font size changes, re-measure the threshold.

## Mockup source

`docs/Portfolio_mockup.html` (gitignored, along with the resume PDF) is a self-unpacking bundle. Each page sits gzip+base64-encoded in the `__bundler/manifest` script tag, and its HTML is a JSON string in that page's `__bundler/template` tag. Decode them to read the design. The bundle has four frames: desktop Home (1280px), desktop Workshop, mobile Home (390px) and mobile Workshop.

Mockup inline styles map to classes here. Port new elements as named classes in `site.css`, not inline styles.

## Decisions

| Decision | Instead of | Why |
|---|---|---|
| Oat + `site.css` | Tailwind Play CDN, inline styles | The owner picked Oat; the Play CDN isn't meant for production, and inline styles from the mockup would need every change made in many places |
| Resume used only as source material | A public Resume download | The PDF includes a phone number, and the whole repo is public |
| Go/Python shown as "Leveling up" | Leaving them off | Framed as learning in progress, not claimed experience |
| Rise-and-blink intro on load | Pointer-following eyes, hand wave, looping bob/blink | The owner tried and rejected each in turn; they wanted one normal animation on first load |
| 16×16 avatar | 32×32 redraw with display-scale sizing | Tried, then reverted at the owner's request |
| Pixel-drawn SVG digits for Workshop stat numbers (5×7 glyphs, `role="img"` + `aria-label`) | Bold or larger Pixelify Sans, Silkscreen | Pixelify's "5" reads as "S" at stat size, and Silkscreen overflows the desktop tiles; SVG keeps both fonts unchanged and stays crisp. New stat values need their glyphs drawn |
| Splash screen once per session, skippable | Showing it on every load, unskippable | The owner asked for a 5s splash; limiting it keeps return visits and in-site navigation fast |
| Side quests section omitted | Shipping the mockup's placeholders | No real Go/Python projects yet |
