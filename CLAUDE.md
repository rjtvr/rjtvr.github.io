# CLAUDE.md

Personal portfolio of Rajat Verma, live at https://rjtvr.github.io/.

## Site

- Two static pages in a pixel-art "Town Square" theme: `index.html` (home) and `workshop.html` (all projects), sharing `assets/site.css` and `assets/favicon.svg`. Styling is [Oat](https://oat.ink) plus `site.css`; there is no build step, `package.json` or bundler.
- **Read [DESIGN.md](DESIGN.md) before changing the design, layout or avatar.** It holds the vocabulary, tokens, class map, phone layout rules, gotchas and past decisions; record new design decisions there.
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
