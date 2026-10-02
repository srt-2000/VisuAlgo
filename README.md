# VisuAlgo

Streamlit app for learning algorithms through interactive demos and step-by-step result tables.

## Features

- **Binary search** — pick a sorted integer range and a target; see each midpoint check in a table.
- **Insertion sort** — generate a random list, sort it, and inspect every insertion step.
- **About** — short intro and links.

## Tech stack

| Tool | Role |
| --- | --- |
| Python 3.12+ | Runtime |
| [Streamlit](https://streamlit.io/) 1.64 | UI and navigation |
| Pandas | Step logs rendered as tables |
| loguru | Service-layer warnings |
| Pytest | Unit tests |
| Ruff | Format and lint |
| mypy | Static typing (`strict` on application code) |
| [uv](https://docs.astral.sh/uv/) | Lockfile and dependency sync |

## Layout

Application code lives under `backend/` and `frontend/`. Tests mirror those layers.

```text
VisuAlgo/
├── backend/
│   ├── algorithms/
│   │   ├── binary_search.py       # BinarySearch.iter_steps
│   │   └── insertion_sort.py      # InsertionSorter.iter_steps
│   ├── domains/
│   │   ├── base.py                # BaseAlgorithmLogDTO (column log + clear)
│   │   ├── binary_search.py       # step VO + BinarySearchAlgorithmLogDTO
│   │   ├── insertion_sort.py      # step VO + InsertionSortAlgorithmLogDTO
│   │   └── constants.py           # BinarySearchStatus, SortingStatus
│   ├── services/
│   │   ├── binary_search.py       # BinarySearchProcessDataLogger
│   │   ├── insertion_sort.py      # InsertionSortProcessDataLogger
│   │   ├── constants.py           # log column labels and messages
│   │   └── exceptions.py
│   └── utils/
│       ├── dataframe.py           # log DTO → pandas DataFrame
│       ├── elements.py            # slider midpoint helper
│       ├── sorting.py             # random list + sort status helper
│       └── constants.py           # DataFrame row-label literals
├── frontend/
│   ├── components/
│   │   ├── pages_container.py     # sidebar StreamlitPage registry
│   │   └── element_settings.py    # nav titles; page paths from secrets
│   ├── pages/
│   │   ├── about/                 # page_about.py, content, element_settings
│   │   ├── binary_search/         # page, content, element_settings
│   │   └── insertion_sort/        # page, content, element_settings, constants
│   └── element_settings.py        # shared titles, icons, table/slider literals
├── tests/
│   ├── algorithms/                # iter_steps invariants + golden cases
│   ├── domains/                   # BaseAlgorithmLogDTO.clear
│   ├── services/                  # ProcessDataLogger recording and errors
│   └── utils/                     # sorting helpers, dataframe builder
├── .streamlit_example/
│   └── example_secrets.toml       # template for local page paths
├── main.py                        # st.navigation entrypoint
├── makefile
├── pyproject.toml
└── uv.lock
```

## How it fits together

```text
Streamlit page
    → *ProcessDataLogger.get_result_and_process_data(...)
        → Algorithm.iter_steps(...)  yields frozen step value objects
        → append each step into a BaseAlgorithmLogDTO subclass (parallel lists)
    → get_dataframe_for_result_table(log) → st.table
```

| Layer | Responsibility |
| --- | --- |
| `backend/domains` | Immutable step snapshots; column-oriented run logs; status enums |
| `backend/algorithms` | Pure logic; generators only (no UI, no pandas) |
| `backend/services` | Run an algorithm, fill a log DTO, read last step / raise domain errors |
| `backend/utils` | Small shared helpers for pages and tests |
| `frontend` | Widgets, copy, session state, tables, navigation |

To add another demo, follow the same path: domain types and log DTO → `iter_steps` implementation → `*ProcessDataLogger` → page package under `frontend/pages/` → register a `StreamlitPage` in `PagesContainer` → add the script path to Streamlit secrets → tests under `tests/algorithms`, `tests/services`, and any new utils.

## Getting started

### With uv (recommended)

```bash
uv sync
# or: make init
```

### Without uv

```bash
python -m venv .venv
source .venv/bin/activate
pip install streamlit loguru pandas pytest ruff mypy
```

### Streamlit secrets

Navigation loads page file paths from `st.secrets.project_pages_paths` (see `frontend/components/element_settings.py`).

1. Copy `.streamlit_example/` to `.streamlit/`.
2. Copy `example_secrets.toml` to `secrets.toml`.
3. Keep paths pointed at `frontend/pages/...` (as in the example).

Do not commit real secrets; `.streamlit/secrets.toml` should stay local.

## Makefile

| Target | Command |
| --- | --- |
| `make init` | `uv sync` |
| `make lock` | `uv lock` |
| `make test` | `uv run pytest -v` |
| `make dev` | `uv run streamlit run main.py` |
| `make format` | `uv run ruff format` |
| `make lint` | `uv run ruff check --fix` |

## Run the app

```bash
make dev
# or: uv run streamlit run main.py
```

## Tests

```bash
make test
# or: uv run pytest -v
```

Type-check application code (optional):

```bash
uv run mypy backend frontend main.py
```
