from html import escape
from pathlib import Path

source = Path('docs/guide.md').read_text(encoding='utf-8')
out = Path('site')
out.mkdir(exist_ok=True)
(out / 'index.html').write_text('<!doctype html><html lang="ru"><meta charset="utf-8"><title>Документация TODO</title><body><pre>' + escape(source) + '</pre></body></html>', encoding='utf-8')
print('Документация создана: site/index.html')
