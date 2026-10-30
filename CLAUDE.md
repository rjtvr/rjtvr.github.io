# CLAUDE.md

Personal portfolio of Rajat Verma, live at https://rjtvr.github.io/.

## Site

- Two static pages in a pixel-art "Town Square" theme: `index.html` (home) and `workshop.html` (all projects). Both share `assets/site.css` and `assets/favicon.svg`, and repeat the same `<head>` and header nav; keep those in sync across both pages.
- Styling is [Oat](https://oat.ink) 1.0.0 from jsDelivr, pinned with an SRI hash, plus `assets/site.css`. Oat styles semantic HTML and puts its CSS in cascade layers, so the unlayered rules in `site.css` win without extra specificity. Theme it by overriding Oat's variables (`--background`, `--primary`, `--font-sans`, ...) in the `:root` block of `site.css`. Oat's JS is left out because no page uses tabs, dropdowns or toasts; add it only alongside one of those.
- Reuse the existing classes (`card note`, `badge chip`, `a.button`, `label`, `meta`, Oat's `row`/`col-*`, `hstack`/`vstack`) for new content; the design is light-only (`color-scheme: light`).
- Phone layout lives in one `@media (max-width: 600px)` block at the end of `site.css`, following the mobile frames of the mockup. Keep desktop rules outside it so phone changes never alter desktop. Use `.hide-sm` / `.show-sm` when copy differs between the two. The home page's hamburger menu is a small inline script in `index.html`; links stay visible when JS is off (the `js` class on `<html>` gates hiding them).
- Fonts are Pixelify Sans and Silkscreen from Google Fonts. There is no build step, `package.json` or bundler.
- Preview by opening `index.html` in a browser.
- Content comes from Rajat's resume. `docs/` (resume PDF and design mockup) is gitignored: it is source material, never published, because the resume includes a phone number.
- The Workshop's "Side quests" section for personal Go/Python projects is left out until real projects exist.

## Deployment

GitHub Pages serves the repo root of `master` at `rjtvr.github.io`, with no custom domain. A push to `master` is a deploy. Every file in the repo is publicly served, so keep the repo to portfolio files only.

The `rjtvr.com` custom domain was removed on purpose: keep the repo free of a `CNAME` file.

## Commit conventions

Follow [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/). CI lints the commits of every pull request (`.github/workflows/commitlint.yml`).

```
<type>[optional scope][!]: <description>

[optional body]

[optional footer(s)]
```

- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`. Write them lowercase.
- `feat` is a new feature (MINOR bump); `fix` is a bug fix (PATCH bump).
- Breaking changes: add `!` after the type/scope, and/or a `BREAKING CHANGE: <details>` footer (MAJOR bump). `BREAKING-CHANGE` is a synonym.
- Description: imperative mood, lowercase, no trailing period, ideally under 72 characters.
- Separate the body and the footers from what precedes them with a blank line.
- Wrap body and footer lines at 100 characters; CI rejects longer lines (`body-max-line-length`).
- Footers use `Token: value` or `Token #value` (e.g. `Refs: #123`). Tokens use `-` in place of spaces, except `BREAKING CHANGE`.
- Apply this to new commits only; existing history stays as it is.
