.PHONY: init lock test dev format lint

UV = uv

init:
	$(UV) sync

lock:
	$(UV) lock

test:
	$(UV) run pytest -v

dev:
	$(UV) run streamlit run main.py

format:
	$(UV) run ruff format

lint:
	$(UV) run ruff check --fix