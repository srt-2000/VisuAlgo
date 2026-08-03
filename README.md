# VisuAlgo

VisuAlgo is a Streamlit pet project for exploring algorithms through an interactive UI with step-by-step process tables.

## Overview

- **`domains/`** — frozen step snapshots and status enums
- **`algorithms/`** — pure algorithm logic that yields step objects (`AlgorithmBase` in `algorithms/interfaces.py`)
- **`services/`** — turns steps into human-readable column logs for tables (`ServiceBase` in `services/interfaces.py`)
- **`front/`** — Streamlit pages, copy, widgets, and navigation
- **`utils/`** — shared helpers (e.g. random unsorted lists)

## Tech Stack

- Python 3.12+
- Streamlit
- loguru
- Pandas (tables on algorithm pages)
- Pytest
- `uv` lockfile and dependency workflow

## Project Structure

```text
VisuAlgo/
├── algorithms/
│   ├── interfaces.py
│   ├── binary_search.py
│   └── insertion_sort.py
├── domains/
│   ├── binary_search.py
│   └── sorting.py
├── services/
│   ├── interfaces.py
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
├── .streamlit_example/
│   └── example_secrets.toml
├── main.py
├── makefile
├── pyproject.toml
└── uv.lock
```

## Architecture Notes

| Layer | Responsibility |
| --- | --- |
| `domains` | Immutable step VOs (`BinarySearchStepValueObject`, `InsertionSortStepValueObject`) and status enums |
| `interfaces` | Shared ABCs: `AlgorithmBase` (`iter_steps`) and `ServiceBase` (log + `get_result_and_process_data`) |
| `algorithms` | Core logic: `search` / `sort` plus `iter_steps` generators; subclasses of `AlgorithmBase` |
| `services` | `*ProcessDataLogger` classes that record steps into table-ready dicts; subclasses of `ServiceBase` |
| `front` | UI only: inputs, buttons, pandas tables, success/error messages |
| `utils` | Small helpers used by pages/tests (random list factory) |

Adding a new algorithm demo usually means: 
tests → algorithm (`AlgorithmBase`) → service logger (`ServiceBase`) → page package → register the page in `PagesContainer`.

## Getting Started

### Using uv

```bash
uv sync
# or: make init
```

### Without uv

```bash
python -m venv .venv
source .venv/bin/activate
pip install streamlit loguru pytest pandas
```

### Streamlit secrets

Page paths are loaded from Streamlit secrets (`st.secrets.project_pages_paths`).

Create the default local config rename:
- .streamlit_example -> .streamlit
- .example_secrets.toml -> secrets.toml

Do not commit real secrets; keep `.streamlit/secrets.toml` local.

## Makefile

Common tasks (requires `uv`):

| Target | Command |
| --- | --- |
| `make init` | `uv sync` |
| `make lock` | `uv lock` |
| `make test` | `uv run pytest -v` |
| `make dev` | `uv run streamlit run main.py` |
| `make format` | `uv run ruff format` |
| `make lint` | `uv run ruff check --fix` |

## Running the App

```bash
make dev
# or: uv run streamlit run main.py
```

## Running Tests

```bash
make test
# or: uv run pytest -v
```
