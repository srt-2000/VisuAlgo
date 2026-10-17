# VisuAlgo

Streamlit app for learning algorithms through interactive demos and step-by-step result tables.

## Features

- **Binary search** — pick a sorted integer range and a target; see each midpoint check in a table.
- **Insertion sort** — generate a random list, sort it, and inspect every insertion step.
- **Bubble sort** — generate a random list, sort it, and inspect every adjacent comparison.
- **Selection sort** — generate a random list, sort it, and inspect every minimum swap into place.
- **About** — short intro and links.

Sidebar groups pages into **Searching** and **Sorting** (plus About at the top).

## Tech stack

<table>
  <thead>
    <tr>
      <th>Tool</th>
      <th>Role</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Python 3.12+</td>
      <td>Runtime</td>
    </tr>
    <tr>
      <td><a href="https://streamlit.io/">Streamlit</a> 1.65</td>
      <td>UI and navigation</td>
    </tr>
    <tr>
      <td>Pandas 3.0</td>
      <td>Step logs rendered as tables</td>
    </tr>
    <tr>
      <td>loguru</td>
      <td>Service-layer warnings</td>
    </tr>
    <tr>
      <td>Pytest 9</td>
      <td>Unit tests</td>
    </tr>
    <tr>
      <td>Ruff 0.17</td>
      <td>Format and lint</td>
    </tr>
    <tr>
      <td>mypy 2.4</td>
      <td>Static typing (<code>strict</code> on application code)</td>
    </tr>
    <tr>
      <td><a href="https://docs.astral.sh/uv/">uv</a></td>
      <td>Lockfile and dependency sync</td>
    </tr>
  </tbody>
</table>

## Layout

Application code lives under `backend/` and `frontend/`. Tests mirror those layers.
Sorting demos share one domain model and live under `sorting/` packages.

```text
VisuAlgo/
├── backend/
│   ├── algorithms/
│   │   ├── binary_search.py           # BinarySearch.iter_steps
│   │   └── sorting/
│   │       ├── bubble.py              # BubbleSorter.iter_steps
│   │       ├── insertion.py           # InsertionSorter.iter_steps
│   │       └── selection.py           # SelectionSorter.iter_steps
│   ├── domains/
│   │   ├── base.py                    # BaseAlgorithmLogDTO (column log + clear)
│   │   ├── binary_search.py           # step VO + BinarySearchAlgorithmLogDTO
│   │   ├── sorting.py                 # BaseSortStepValueObject + BaseSortAlgorithmLogDTO
│   │   └── constants.py               # BinarySearchStatus, SortingStatus
│   ├── services/
│   │   ├── binary_search.py           # BinarySearchProcessDataLogger
│   │   ├── sorting/
│   │   │   ├── bubble.py              # BubbleSortProcessDataLogger
│   │   │   ├── insertion.py           # InsertionSortProcessDataLogger
│   │   │   └── selection.py           # SelectionSortProcessDataLogger
│   │   ├── constants.py               # log column labels and messages
│   │   └── exceptions.py
│   └── utils/
│       ├── dataframe.py               # log DTO → pandas DataFrame
│       ├── elements.py                # slider midpoint helper
│       ├── sorting.py                 # random list + sort status helper
│       └── constants.py               # DataFrame row-label literals
├── frontend/
│   ├── navigation/
│   │   ├── pages_containers.py        # About / Searching / Sorting page registries
│   │   ├── navigation_fabric.py       # sidebar section map for st.navigation
│   │   └── element_settings.py        # nav titles; page paths from secrets
│   ├── pages/
│   │   ├── about/                     # page_about.py, content, element_settings
│   │   ├── binary_search/             # page, content, element_settings
│   │   └── sorting/
│   │       ├── constants.py           # shared session keys and captions
│   │       ├── element_settings.py    # shared widgets for sort pages
│   │       ├── bubble/                # page, content
│   │       ├── insertion/             # page, content
│   │       └── selection/             # page, content
│   └── element_settings.py            # shared titles, icons, table/slider literals
├── tests/
│   ├── algorithms/
│   │   ├── binary_search/             # iter_steps invariants + golden cases
│   │   └── sorting/                   # bubble / insertion / selection
│   ├── domains/                       # BaseAlgorithmLogDTO.clear
│   ├── services/
│   │   ├── binary_search/             # ProcessDataLogger recording and errors
│   │   └── sorting/                   # bubble / insertion / selection loggers
│   └── utils/                         # sorting helpers, dataframe builder
├── .streamlit_example/
│   └── example_secrets.toml           # template for local page paths
├── main.py                            # st.navigation entrypoint
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

<table>
  <thead>
    <tr>
      <th>Layer</th>
      <th>Responsibility</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>backend/domains</code></td>
      <td>Immutable step snapshots; column-oriented run logs; status enums</td>
    </tr>
    <tr>
      <td><code>backend/algorithms</code></td>
      <td>Pure logic; generators only (no UI, no pandas)</td>
    </tr>
    <tr>
      <td><code>backend/services</code></td>
      <td>Run an algorithm, fill a log DTO, read last step / raise domain errors</td>
    </tr>
    <tr>
      <td><code>backend/utils</code></td>
      <td>Small shared helpers for pages and tests</td>
    </tr>
    <tr>
      <td><code>frontend</code></td>
      <td>Widgets, copy, session state, tables, navigation</td>
    </tr>
  </tbody>
</table>

Sorting demos reuse `BaseSortStepValueObject` and `BaseSortAlgorithmLogDTO` from `backend/domains/sorting.py`.
Each sorter still has its own `iter_steps` engine and `*ProcessDataLogger`.

To add another demo, follow the same path: domain types and log DTO → `iter_steps` implementation → `*ProcessDataLogger` → page package under `frontend/pages/` → register a `StreamlitPage` in the matching container under `frontend/navigation/pages_containers.py` → add the script path to Streamlit secrets → tests under `tests/algorithms`, `tests/services`, and any new utils.

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
pip install "streamlit==1.65.0" "loguru>=0.7.3" "pandas>=3.0.6" "pytest>=9.1.1" "ruff==0.17.0" "mypy==2.4.0"
```

### Streamlit secrets

Navigation loads page file paths from `st.secrets.project_pages_paths` (see `frontend/navigation/element_settings.py`).

1. Copy `.streamlit_example/` to `.streamlit/`.
2. Copy `example_secrets.toml` to `secrets.toml`.
3. Keep paths pointed at `frontend/pages/...` (as in the example).

Do not commit real secrets; `.streamlit/secrets.toml` should stay local.

## Makefile

<table>
  <thead>
    <tr>
      <th>Target</th>
      <th>Command</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>make init</code></td>
      <td><code>uv sync</code></td>
    </tr>
    <tr>
      <td><code>make lock</code></td>
      <td><code>uv lock</code></td>
    </tr>
    <tr>
      <td><code>make test</code></td>
      <td><code>uv run pytest -v</code></td>
    </tr>
    <tr>
      <td><code>make dev</code></td>
      <td><code>uv run streamlit run main.py</code></td>
    </tr>
    <tr>
      <td><code>make format</code></td>
      <td><code>uv run ruff format</code></td>
    </tr>
    <tr>
      <td><code>make lint</code></td>
      <td><code>uv run ruff check --fix</code></td>
    </tr>
  </tbody>
</table>

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
