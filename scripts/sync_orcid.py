"""Discover ORCID works and prepare reviewable Jekyll publication drafts."""
import json
import re
from pathlib import Path
from urllib.request import Request, urlopen

ORCID = "0009-0008-5977-498X"
ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS = ROOT / "_publications"
HEADERS = {"Accept": "application/json", "User-Agent": "portfolio-orcid-sync/1.0"}


def fetch(url):
    with urlopen(Request(url, headers=HEADERS), timeout=20) as response:
        return json.load(response)


def text(field):
    return (field or {}).get("value") or ""


def existing_dois():
    return set(re.findall(r"(?im)^doi:\s*['\"]?([^\s'\"]+)", "\n".join(
        p.read_text(encoding="utf-8") for p in PUBLICATIONS.glob("*.md")
    )))


def main():
    known = existing_dois()
    groups = fetch(f"https://pub.orcid.org/v3.0/{ORCID}/works").get("group", [])
    created = []
    for group in groups:
        identifiers = (group.get("external-ids") or {}).get("external-id") or []
        doi = next(((item.get("external-id-value") or "") for item in identifiers
                    if item.get("external-id-type", "").lower() == "doi"), "")
        if not doi or doi in known:
            continue
        summary = (group.get("work-summary") or [{}])[0]
        title = text((summary.get("title") or {}).get("title"))
        if not title:
            continue
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:70]
        path = PUBLICATIONS / f"orcid-{slug}.md"
        if path.exists():
            continue
        year = text((summary.get("publication-date") or {}).get("year"))
        journal = text(summary.get("journal-title"))
        kind = "conferences" if "conference" in (summary.get("publication-type") or "").lower() else "journals"
        metadata = {"title": title, "collection": "publications", "category": kind,
                    "permalink": f"/publication/{slug}/", "venue": journal,
                    "doi": doi, "orcid": ORCID, "published": False}
        if year.isdigit():
            metadata["year"] = int(year)
        # JSON strings are valid YAML scalars. A draft remains hidden until reviewed.
        body = "---\n" + "".join(f"{key}: {json.dumps(value, ensure_ascii=False)}\n" for key, value in metadata.items()) + "---\n\nPublication details from ORCID. Review authors, venue, type and status before setting `published: true`.\n"
        path.write_text(body, encoding="utf-8")
        created.append(path.name)
        known.add(doi)
    print(f"Created {len(created)} review drafts: {', '.join(created)}")


if __name__ == "__main__":
    main()
