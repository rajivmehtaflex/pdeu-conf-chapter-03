# Chapter 3: Deep Agent + Custom Tools

Adds SQL ledger and warehouse delivery tools.

## Setup

```bash
uv sync
cp .env.example .env
```

Set `OPENROUTER_API_KEY` and `OPENROUTER_MODEL` in `.env`.

## Run

```bash
uv run python main.py --self-check
uv run python main.py "Audit the account for Gujarat Steel Corp."
uv run pytest
```
