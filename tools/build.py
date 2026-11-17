"""Build the site: each src/*.html (a header of title/desc, '---', then the body) becomes
<name>/index.html with the shared layout. index.html and 404.html stay at their own paths.
Run: python3 tools/build.py"""
import html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
NAV = '<nav><a href="/#games">Games</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a></nav>'
FOOT = ('<footer><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a><a href="/conduct/">Conduct</a>'
        '<a href="/ai/">AI use</a><a href="mailto:hello@getexp.com">Contact</a>'
        '<p>© 2026 getexp. All rights reserved.</p></footer>')

def page(title: str, desc: str, body: str, path: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="https://getexp.com{path}">
<link rel="canonical" href="https://getexp.com{path}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header><a class="logo" href="/">get<span>exp</span></a>{NAV}</header>
<main>
{body.strip()}
</main>
{FOOT}
</body>
</html>
"""

for src in sorted(SRC.rglob("*.html")):
    head, body = src.read_text().split("\n---\n", 1)
    meta = dict(line.split(": ", 1) for line in head.splitlines() if line.strip())
    rel = src.relative_to(SRC).with_suffix("")
    if rel.name in ("index", "404"):
        out, path = ROOT / src.relative_to(SRC), "/" if rel.name == "index" else "/404.html"
    else:
        out, path = ROOT / rel / "index.html", f"/{rel.as_posix()}/"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(meta["title"], meta["desc"], body, path))
    print(out.relative_to(ROOT))
