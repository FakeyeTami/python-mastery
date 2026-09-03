<div align="center">

  <img src="./public/banner.png" alt="Python Mastery by Tamilore Fakeye" width="100%">

  <h1>Python Mastery</h1>

**A personal, topic-by-topic Python learning repo — from syntax to frameworks, DSA, and concurrency.**

_Every section is worked through by hand, documented, and built on as I go — not a pre-built curriculum._

  <br>

![Status](https://img.shields.io/badge/Status-Active-10b981?style=for-the-badge&labelColor=000)
![Last Commit](https://img.shields.io/github/last-commit/FakeyeTami/python-mastery?style=for-the-badge&labelColor=000&color=10b981)
![License](https://img.shields.io/github/license/FakeyeTami/python-mastery?style=for-the-badge&labelColor=000&color=10b981)

</div>

---

## About

This repo is where I'm rebuilding Python from the ground up — not "I use pandas for work," but actually understanding the language: syntax and idioms, data structures and algorithms, OOP, typing, concurrency, testing, and the frameworks built on top of it (FastAPI, Django, Flask). It's part of a longer zero-to-hero developer roadmap that also covers C and Go.

Each section aims to be:

- 🧠 Understood, not copied — every file is written by hand, no AI-generated solutions
- 📖 Documented with my own notes, not just code
- 🧩 Built incrementally — sections are added as I reach them, not pre-scaffolded

---

## Structure

```
python-mastery/
├── 00-fundamentals-part-1/
│   ├── challenges/
│   ├── notes/
│   ├── 01-variables.py
│   ├── 02-data-types.py
│   ├── 03-operators.py
│   ├── 04-strings.py
│   ├── 05-conditionals.py
│   └── 06-loops.py
├── 01-fundamentals-part-2/
│   ├── challenges/
│   ├── notes/
│   └── ... (lists, tuples, sets, dicts, type casting, functions & builtins, exceptions, comments & type annotations)
├── 02-environments-and-package-managers/
├── 03-language-internals-and-idioms/
│   └── ... (modules, error handling, lambdas, decorators, iterators, regex, variable scope)
├── 04-oop/
│   └── ... (classes, methods, inheritance, encapsulation)
├── 05-static-typing/
├── 06-file-handling/
├── 07-data-structures-and-algorithms/
│   └── ... (arrays & linked lists, hashmaps, heaps, stacks & queues, BST, recursion, sorting)
├── 08-testing/
├── 09-concurrency/
├── 10-frameworks/
│   ├── fastapi/
│   ├── django/
│   └── flask/
├── projects/
│   └── ... (applied projects drawing on multiple sections at once)
├── .gitignore
└── README.md
```

Every section folder follows the same shape: `notes/` for the write-up per concept, `challenges/` for exercises attempted without notes open, and numbered files for the actual working code.

---

## Lessons / Progress

| #   | Section                              | Key topics                                                                              | Status         |
| --- | ------------------------------------ | ----------------------------------------------------------------------------------------| -------------- |
| 00  | Fundamentals – Part 1                | Syntax, variables & data types, operators, strings, conditionals, loops                 | 🟢 In progress |
| 01  | Fundamentals – Part 2                | Lists, tuples, sets, dicts, type casting, functions & built-ins, exceptions, annotations | ⚪ Not started |
| 02  | Environments & Package Managers      | venv, uv, pip, dependency management                                                    | ⚪ Not started |
| 03  | Language Internals & Idioms          | Modules, error handling, lambdas, decorators, iterators, regex, variable scope          | ⚪ Not started |
| 04  | OOP                                   | Classes, methods, inheritance, encapsulation                                            | ⚪ Not started |
| 05  | Static Typing                         | Type hints, mypy, generics                                                              | ⚪ Not started |
| 06  | File Handling                         | Reading/writing files, paths, context managers                                          | ⚪ Not started |
| 07  | Data Structures & Algorithms          | Arrays & linked lists, hashmaps, heaps, stacks & queues, BST, recursion, sorting         | ⚪ Not started |
| 08  | Testing                               | pytest, unittest, mocking                                                               | ⚪ Not started |
| 09  | Concurrency                           | Threading, multiprocessing, asyncio, the GIL                                            | ⚪ Not started |
| 10  | Frameworks                            | FastAPI, Django, Flask                                                                  | ⚪ Not started |
| —   | Projects                              | Applied builds that draw on multiple sections at once                                   | ⚪ Not started |

> Update the status column as sections are completed — 🟢 In progress, ✅ Complete, ⚪ Not started.

---

## ⚙️ Technologies

<div>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-DE5FE9?style=for-the-badge&logo=uv&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![mypy](https://img.shields.io/badge/mypy-1F6FEB?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

</div>

---

<details>
<summary><b>📍 Running a section locally</b></summary>

<br/>

```bash
uv venv
source .venv/bin/activate
uv run 00-fundamentals-part-1/01-variables.py
```

For sections with tests once `08-testing` is reached:

```bash
uv run pytest 08-testing/
```

</details>

---

## Disclaimers

- This is a **personal learning repo**, not a tutorial or a maintained package — code here prioritizes understanding a concept over production quality.
- **AI is used for explanation and review only** — every solution here is written by hand; if it's wrong or non-idiomatic, that's the point where I'm still learning.
- Sections are added **as I reach them**, in the order in the progress table above — folders that don't exist yet simply haven't started.
- Expect inconsistency early on and increasing polish later — this repo is a record of the learning process, not a finished artifact.

---

## 💎 Let's connect

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-fakeyetami-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/fakeyetami)
&nbsp;[![GitHub](https://img.shields.io/badge/GitHub-FakeyeTami-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/FakeyeTami)
&nbsp;[![Portfolio](https://img.shields.io/badge/Portfolio-tamicodes.dev-4770FF?style=for-the-badge&logo=vercel&logoColor=white)](https://tamicodes.dev)
&nbsp;[![Email](https://img.shields.io/badge/Email-fakeyetami@gmail.com-4770FF?style=for-the-badge&logo=gmail&logoColor=white)](mailto:fakeyetami@gmail.com)

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=4770FF&height=120&section=footer&fontColor=ffffff" width="100%"/>

</div>

---

<div align="center">
  <sub>Built with stubbornness and attention to detail · © 2026 Tamilore Fakeye</sub>
</div>

