#!/usr/bin/env python3
"""Search and download textbook mechanism diagrams from Wikimedia Commons with polite rate limiting."""

import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent / "assets" / "mechanisms" / "web"
OUT_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) OrgChemStudyBot/1.0 (https://commons.wikimedia.org; educational)"
}

QUERIES = {
    "01-hx-addition": "hydrohalogenation mechanism alkene HBr",
    "02-x2-addition": "halogenation of alkene bromonium ion mechanism",
    "03-halohydrin": "halohydrin formation mechanism",
    "04-oxymercuration": "oxymercuration mechanism",
    "05-hydroboration": "hydroboration oxidation mechanism",
    "06-hydrogenation": "alkene hydrogenation mechanism",
    "07-epoxidation": "epoxidation mechanism peroxyacid",
    "08-epoxide-hydrolysis": "acid catalyzed epoxide ring opening mechanism",
    "09-oso4-hydroxylation": "dihydroxylation OsO4 mechanism",
    "10-carbene-dichloro": "dichlorocarbene alkene mechanism",
    "11-simmons-smith": "Simmons Smith mechanism",
    "12-ozonolysis": "ozonolysis mechanism molozonide ozonide",
    "13-kmno4-cleavage": "KMnO4 alkene cleavage mechanism",
    "14-diol-cleavage": "periodate cleavage diol mechanism",
    "15-allylic-bromination": "Wohl Ziegler NBS bromination mechanism",
    "16b-socl2": "SOCl2 alcohol mechanism chlorosulfite",
    "16c-pbr3": "PBr3 alcohol mechanism",
}


def api_get(params: dict) -> dict:
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download_file(url: str, dest: Path) -> None:
    if dest.exists() and dest.stat().st_size > 1000:
        return
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=25) as resp:
        dest.write_bytes(resp.read())
    time.sleep(1.2)


def main() -> None:
    search_hits: dict[str, list[str]] = {}
    all_titles: list[str] = []

    for key, q in QUERIES.items():
        try:
            data = api_get({
                "action": "query",
                "list": "search",
                "srsearch": f"{q} filetype:bitmap|drawing",
                "srnamespace": "6",
                "srlimit": "2",
                "format": "json",
            })
            titles = [h["title"] for h in data.get("query", {}).get("search", [])]
            search_hits[key] = titles
            for t in titles:
                if t not in all_titles:
                    all_titles.append(t)
            time.sleep(0.4)
        except Exception as e:
            print(f"[SEARCH ERR] {key}: {e}")

    # Batch query imageinfo in chunks of 40 titles
    title_to_url: dict[str, str] = {}
    for i in range(0, len(all_titles), 40):
        batch = all_titles[i : i + 40]
        info = api_get({
            "action": "query",
            "titles": "|".join(batch),
            "prop": "imageinfo",
            "iiprop": "url",
            "format": "json",
        })
        for p in info.get("query", {}).get("pages", {}).values():
            t = p.get("title", "")
            ii = p.get("imageinfo", [{}])[0]
            if ii.get("url"):
                title_to_url[t] = ii["url"]

    manifest = {}
    for key, titles in search_hits.items():
        manifest[key] = []
        for idx, title in enumerate(titles):
            orig_url = title_to_url.get(title)
            if not orig_url:
                continue
            ext = Path(urllib.parse.urlparse(orig_url).path).suffix.lower() or ".svg"
            out_file = OUT_DIR / f"{key}_{idx}{ext}"
            try:
                download_file(orig_url, out_file)
                manifest[key].append({"title": title, "file": out_file.name, "url": orig_url})
                print(f"[OK] {key}: {title} -> {out_file.name}")
            except Exception as e:
                print(f"[DL ERR] {key} ({title}): {e}")

    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
