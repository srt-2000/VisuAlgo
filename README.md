# VisuAlgo

VisuAlgo is a Streamlit pet project for exploring algorithms through an interactive UI with step-by-step process tables.

Current pages:
- `About`
- `Binary Search` — search a sorted integer range and inspect each half-check
- `Insertion Sort` — generate a random list, sort it, and inspect each insertion step

## Overview

The app is a multipage Streamlit application. Navigation is wired in `main.py` via `front/components/pages_container.py`.

Algorithm demos follow a layered pipeline:

```text
front (page)
  → services (process data logger)
    → algorithms (iter_steps / search / sort)
      → domains (step value objects + status enums)
```

- **`domains/`** — frozen step snapshots and status enums
- **`algorithms/`** — pure algorithm logic that yields step objects
- **`services/`** — turns steps into human-readable column logs for tables
- **`front/`** — Streamlit pages, copy, widgets, and navigation
- **`utils/`** — shared helpers (e.g. random unsorted lists)

## Tech Stack

- Python 3.12+
- Streamlit
- Loguru
- Pandas (tables on algorithm pages)
- Pytest
- `uv` lockfile and dependency workflow

## Project Structure

```text
VisuAlgo/
├── algorithms/
│   ├── binary_search.py
│   └── insertion_sort.py
├── domains/
│   ├── binary_search.py
│   └── sorting.py
├── services/
│   ├── binary_search.py
│   ├── insertion_sort.py
│   ├── constants.py
│   └── exceptions.py
├── front/
│   ├── components/
│   │   ├── pages_container.py
│   │   └── element_settings.py
│   ├── pages/
│   │   ├── about/
│   │   ├── binary_search/
│   │   └── insertion_sort/
│   └── element_settings.py
├── utils/
│   └── sorting.py
├── tests/
│   ├── algorithms/
│   │   ├── binary_search/
│   │   └── insertion_sort/
│   ├── services/
│   │   ├── binary_search/
│   │   └── insertion_sort/
│   └── utils/
├── main.py
├── pyproject.toml
└── uv.lock
```

Each algorithm page package typically contains:
- `page_*.py` — Streamlit entry
- `content.py` — markdown copy
- `constants.py` — page-local field / message keys
- `element_settings.py` — widget labels, limits, titles

## Architecture Notes

| Layer | Responsibility |
| --- | --- |
| `domains` | Immutable step VOs (`BinarySearchStepValueObject`, `InsertionSortStepValueObject`) and status enums |
| `algorithms` | Core logic: `search` / `sort` plus `iter_steps` generators |
| `services` | `*ProcessDataLogger` classes that record steps into table-ready dicts |
| `front` | UI only: inputs, buttons, pandas tables, success/error messages |
| `utils` | Small helpers used by pages/tests (random list factory) |

Adding a new algorithm demo usually means: tests → algorithm → service logger → page package → register the page in `PagesContainer`.

## Getting Started

### Using uv

```bash
uv sync
```

### Without uv

```bash
python -m venv .venv
source .venv/bin/activate
pip install streamlit loguru pytest pandas
```

## Running the App

```bash
uv run streamlit run main.py
```

## Running Tests

Full suite:

```bash
uv run pytest
```
