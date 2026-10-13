"""Add <image:image> entries to sitemap.xml from each page's content images (run after render_shell.py).

Keeps the hand-maintained URL list, lastmod and priority values; only the image entries are regenerated.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://drbhartisurgery.com/'
SKIP = ('logo', 'apple-touch-icon', 'thumb/')


def page_images(name):
    html = (ROOT / name).read_text(encoding='utf-8')
    main = re.search(r'<main.*?</main>', html, re.S)
    main = main.group(0) if main else ''
    found = []
    # Full-size targets of linked thumbnails (gallery), then images shown directly.
    for src in re.findall(r'<a href="(images/[^"]+\.(?:jpe?g|png|webp))"', main) + re.findall(r'<img src="(images/[^"]+)"', main):
        if any(s in src for s in SKIP) or (src.endswith('portrait.jpg') and name not in ('index.html', 'about-dr-vikeerna-bharti.html')):
            continue
        if src not in found and (ROOT / src).exists():
            found.append(src)
    return found


def main():
    path = ROOT / 'sitemap.xml'
    xml = path.read_text(encoding='utf-8')
    xml = re.sub(r'<image:image>.*?</image:image>', '', xml, flags=re.S)
    if 'xmlns:image=' not in xml:
        xml = xml.replace('xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"', 'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"', 1)
    total = 0

    def add(m):
        nonlocal total
        loc = m.group(1)
        name = loc[len(BASE):] or 'index.html'
        imgs = page_images(name)
        total += len(imgs)
        return m.group(0).replace('</url>', ''.join(f'<image:image><image:loc>{BASE}{src}</image:loc></image:image>' for src in imgs) + '</url>')

    xml = re.sub(r'<url><loc>([^<]+)</loc>.*?</url>', add, xml)
    path.write_text(xml, encoding='utf-8')
    print(f'Sitemap: {total} image entries added.')


if __name__ == '__main__':
    main()
