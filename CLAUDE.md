# CLAUDE.md

Personal portfolio of Rajat Verma, live at https://rjtvr.github.io/.

## Site

- The whole site is `index.html`: one self-contained page. Keep markup, styles and the scroll-animation script inside it.
- Styling is Tailwind via the Play CDN (`cdn.tailwindcss.com`) plus the Inter font from Google Fonts. There is no build step, `package.json` or bundler; write Tailwind utility classes directly in the markup.
- Preview by opening `index.html` in a browser: it has no local file dependencies.
- The Projects section is intentionally commented out. Leave it hidden unless asked to show it.

## Deployment

GitHub Pages serves the repo root of `master` at `rjtvr.github.io`, with no custom domain. A push to `master` is a deploy. Every file in the repo is publicly served, so keep the repo to portfolio files only.

The `rjtvr.dev` custom domain was removed on purpose: keep the repo free of a `CNAME` file.

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
- Footers use `Token: value` or `Token #value` (e.g. `Refs: #123`). Tokens use `-` in place of spaces, except `BREAKING CHANGE`.
- Apply this to new commits only; existing history stays as it is.
