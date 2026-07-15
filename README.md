# VisuAlgo

VisuAlgo is a small Streamlit pet project for exploring algorithms through a simple interactive UI.

At the moment, the app includes:
- an `About` page
- an interactive `Binary Search` demo
- a core binary search implementation in `src`
- pytest coverage for the binary search logic

## Overview

The project is built as a multipage Streamlit application. Navigation is wired in `main.py`, available pages are declared in `front/templates/pages_container.py`, and algorithm logic lives in `src/`.

The current focus is a binary search demo that lets you:
- define a sorted integer range
- choose a target value
- run binary search and get the target index if it exists

## Features

- Multipage Streamlit app with sidebar navigation
- Dedicated `About` page
- Interactive binary search demo
- Separated UI and algorithm logic
- Automated tests for binary search behavior

## Tech Stack

- Python 3.12+
- Streamlit
- Loguru
- Pytest
- `uv` lockfile and dependency workflow

## Project Structure

```text
VisuAlgo/
├── front/
│   ├── pages/
│   │   ├── about.py
│   │   └── binary_search.py
│   └── templates/
│       └── pages_container.py
├── src/
│   └── binary_search.py
├── tests/
│   └── src_tests/
│       ├── conftest.py
│       └── test_binary_search.py
├── main.py
├── pyproject.toml
└── uv.lock
```

## Getting Started

### Using uv

```bash
uv sync
```

### Without uv

```bash
python -m venv .venv
source .venv/bin/activate
pip install streamlit loguru pytest
```

## Running the App

```bash
uv run streamlit run main.py
```

Then open the local Streamlit URL shown in the terminal.

## Running Tests

Run the full test suite:

```bash
uv run pytest
```

Run only binary search tests:

```bash
uv run pytest tests/atgorithms_tests/test_binary_search.py
```

## Binary Search Demo

The binary search page is implemented in `front/pages/binary_search.py`, while the core search logic is implemented in `src/binary_search.py`.

The page currently:
- explains the algorithm and its complexity
- lets the user define a sorted integer range
- accepts a target number
- runs iterative binary search on button click
- displays the found index or an error message

## Current Status

This project is in an early stage.

Right now, only one algorithm demo is implemented: binary search. The app is structured to make it easy to add more algorithm pages later, but they are not part of the current codebase yet.

## Current Limitations

- The project currently demonstrates only binary search
- The UI is an interactive demo, not a step-by-step animated visualizer
- Tests currently cover only the binary search core logic

## Roadmap

Possible next steps for the project:
- add more algorithm pages
- expand automated test coverage
- improve the binary search page with richer visualization of each search step
