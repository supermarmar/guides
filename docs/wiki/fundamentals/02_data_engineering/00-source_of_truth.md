# Source of truth for data engineering

The authoritative data engineering material in this repository is the twenty-lecture course at `docs/lectures/fundamentals/data_engineering/`, not the notes in this folder. This is a deliberate exception to the general repository convention that `docs/wiki/` is authoritative and lectures are walk-throughs of it. Read this file before treating anything else in this folder as current coverage.

## What happened

The lecture course was built on 31 July 2026 from the eleven notes in this folder plus new material drawn from current industry practice. Roughly half the sequence had a substantive source note here; the rest had none. In several places the lecture is now considerably deeper than the note it came from: `02-sql-intro.md` is a stub against three full SQL lectures, and `03-duckdb.md` is a comparison table against a full lecture. The user decided that for this topic the lectures are the source of truth rather than backfilling these notes from them.

## What follows for anyone working here

New data engineering material goes into the lecture course, not into this folder. Extend or revise the relevant lecture, and update the course landing page if the sequence changes. Do not add notes here expecting them to be the canonical record.

Treat the notes in this folder as origin material with historical value: they show what the coverage was before the course existed, and several contain code worked through in a notebook that the lectures reference rather than reproduce. The notebooks in particular (`04-sql-defintions.ipynb`, `05-sql-queries.ipynb`, `06-sql-manipulation.ipynb`, `09-pdfplumber.ipynb`, `10-pandera.ipynb`) remain runnable and are the executable companion to Lectures 04 to 06, 11, and 16.

Two workflows described elsewhere in the repository read `docs/wiki/` and need to read the lecture course as well for this topic. Gap inventory by `grep -r "<!-- GAP -->"` will not find gaps recorded in the lectures, since the lecture format has no equivalent tag. Flashcard authoring for a data engineering topic should be sourced from the lecture, not from the note.

## Mapping

The course landing page carries the full lecture-to-source-note table, including which notes are now thinner than the lecture built on them. See [the data engineering course](../../../lectures/fundamentals/data_engineering/index.html).
