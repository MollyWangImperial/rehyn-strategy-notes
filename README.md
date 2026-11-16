# Rehyn strategy notes

The written content of the Rehyn strategy library: the strategy map list and one strategy note for each of the 66 strategies.
This repository holds the text only, so it can be edited with a language model and returned to the site.

## Layout

- `map/strategies.json`: every strategy on the strategy map, with its style, instruments, description and indicative figures.
- `markdown/<id>.md`: each note as readable Markdown, section by section, in the order the page shows it. Best for reading and editing with a model.
- `notes/<id>.json`: the same note as structured data. This is what the site reads.
- `pages/`: the page sources for the strategy map (`Main.dc.html`) and the strategy note template (`Strategy.dc.html`), for reference.
- `WRITING_RULES.md` and `NOTE_BRIEF.md`: the rules every note follows.
- `tools/build_notes.py`: writes edited notes back into the site.

## Editing

Edit the text values in `notes/<id>.json`, keeping every key, the number of items in each list, the strategy ids in `related`
and the numbers in `past`, `ahead` and `startYear`. Section titles that are not stored in a note are fixed in the page template.

## Status

The figures on the event cards, the historical stress results and the forward scenario estimates were written from model knowledge,
not from Rehyn data, and need checking before they are presented as facts. Indicative return, volatility and drawdown figures come from the
strategy map and are not backtests.
