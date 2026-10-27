"""Inline logos and the brand mark into src.html -> index.html (the artifact host blocks external images)."""
import base64, mimetypes, pathlib, re, sys

here = pathlib.Path(__file__).parent
assets = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else here / "assets"
src = (here / "src.html").read_text()

brand = re.search(r'<path d="([^"]+)"', (assets / "logo.svg").read_text()).group(1)
src = src.replace("{{BRAND}}", brand)

def logo(m):
    f = assets / m.group(1)
    mime = mimetypes.guess_type(f.name)[0]
    return f"data:{mime};base64," + base64.b64encode(f.read_bytes()).decode()

out = re.sub(r"\{\{LOGO:([^}]+)\}\}", logo, src)
assert "{{" not in out, "unreplaced placeholder"
# index.html is the Artifact body (the host adds the document shell); docs/ is the standalone GitHub Pages site
(here / "index.html").write_text(out)
shell = ('<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n'
         '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
         '<style>:root{color-scheme:light;padding-block:env(safe-area-inset-top,0px) env(safe-area-inset-bottom,0px)}'
         'body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n')
(here / "docs").mkdir(exist_ok=True)
(here / "docs" / "index.html").write_text(shell + out + "\n</html>\n")
(here / "docs" / ".nojekyll").write_text("")
print(f"index.html: {len(out) // 1024} KB, docs/index.html written")
