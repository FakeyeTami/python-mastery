# python-mastery

Topic-by-topic Python learning repo — going from "I use Python for data analysis" to actually understanding the language, as part of a broader zero-to-hero developer roadmap.

## How this repo works

Each concept lives in its own numbered folder: `<section>/<topic>/`. Every topic folder contains:

- **`README.md`** — the explanation: what the concept is, why it matters, how it connects to the previous topic
- **`main.py`** — working file, where the concept gets written and run as it's learned
- **`challenge.py`** — a self-contained exercise attempted after `main.py` clicks
- **`tests/`** — pytest coverage for the challenge solution

Folders are numbered (`00-`, `01-`, `02-`…) at both the section and topic level, so the directory listing itself is the syllabus, in order.

## Sections

| Section | Focus |
|---|---|
| `00-fundamentals` | syntax, types, control flow, functions, error handling |
| `01-idiomatic-python` | comprehensions, generators/iterators, context managers |
| `02-oop-and-design` | classes, dunder methods, inheritance vs. composition, dataclasses |
| `03-tooling-and-packaging` | uv, type hints/mypy, pytest, packaging |
| `04-concurrency` | the GIL, threading, multiprocessing, asyncio |
| `05-applied-backend` | FastAPI basics, async API design, ORM/database integration |

## Setup

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt   # added per-topic as tooling is introduced
```

## Progress

- [ ] 00-fundamentals
- [ ] 01-idiomatic-python
- [ ] 02-oop-and-design
- [ ] 03-tooling-and-packaging
- [ ] 04-concurrency
- [ ] 05-applied-backend

