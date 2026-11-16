"""Rebuilds the site's src/intel/notes.json from the edited notes in this repository.
Usage: python tools/build_notes.py <path to markets-perspectives>"""
import json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
site = pathlib.Path(sys.argv[1]) / "src/intel/notes.json"
old = json.loads(site.read_text(encoding="utf-8"))
for f in sorted((root / "notes").glob("*.json")):
    n = json.loads(f.read_text(encoding="utf-8"))
    i = n.pop("id"); n.pop("name", None)
    old["notes"][i].update(n)
site.write_text(json.dumps(old, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print("updated", len(old["notes"]), "notes")
