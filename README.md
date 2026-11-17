# getexp.com

The getexp studio site, served by GitHub Pages from `main` at https://getexp.com.

- Pages live in `src/` as a short header (`title:`, `desc:`), a `---` line, then the HTML body.
- `python3 tools/build.py` wraps each one in the shared layout and writes `<name>/index.html`
  (`index.html` and `404.html` stay where they are). Commit the built files; Pages serves them as-is.
- `style.css` holds the colours (light and dark) and layout; `CNAME` holds the custom domain.

## Policies

`src/privacy.html`, `src/terms.html`, `src/conduct.html` and `src/ai.html` describe what the games
actually do. When a game changes what it stores or where it sends data, change its section here
in the same week, and update the "Last updated" date.
