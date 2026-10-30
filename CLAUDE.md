# CLAUDE.md

Personal portfolio of Rajat Verma, live at https://rjtvr.github.io/.

## Site

- Two static pages in a pixel-art "Town Square" theme: `index.html` (home) and `workshop.html` (all projects), sharing `assets/favicon.svg` and the site stylesheet. Styling is [Oat](https://oat.ink) plus that stylesheet; there is no `package.json` or bundler.
- **Stylesheet: edit `assets/site.css`, ship `assets/site.min.css`.** `site.css` is the readable source and the only file to edit; both pages link `site.min.css`. After any change to `site.css`, regenerate the minified file in the same commit with `python scripts/minify-css.py` (Python 3, no dependencies). Never hand-edit `site.min.css`. CI fails a pull request whose `site.min.css` is stale (`.github/workflows/css.yml`, which runs `python scripts/minify-css.py --check`).
- **Read [DESIGN.md](DESIGN.md) before changing the design, layout or avatar.** It holds the vocabulary, tokens, class map, phone layout rules, gotchas and past decisions; record new design decisions there.
- `404.html` is the "Lost in the Woods" page GitHub Pages serves for any missing path, at that path. Keep every URL in it root-relative (`/assets/...`, `/`). Preview it through a local server (e.g. VS Code Live Server), not as a file.
- Search engines: `index.html` carries Person structured data (JSON-LD) and both pages a canonical link; `sitemap.xml` and `robots.txt` sit at the root. When a page's content changes, update its `<lastmod>` in `sitemap.xml`; add new pages there too.
- Preview by opening `index.html` in a browser.
- Content comes from Rajat's resume. `docs/` (resume PDF and design mockup) is gitignored: it is source material, never published, because the resume includes a phone number.

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
