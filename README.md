# Lake

My solutions and projects for [CS50x](https://cs50.harvard.edu/x/), Harvard's introductory computer science course.

## About

This repository is a collection of problem sets and exercises completed throughout CS50x. Each folder represents a separate exercise or project, ranging from early C fundamentals to later work in Python.

**Languages used:**
- Python — 52.3%
- C — 46.8%
- Makefile — 0.9%

## Structure

Every top-level folder corresponds to a single problem set or exercise. A few standalone scripts live at the root of the repo as well (`cat.py`, `extensions.py`, `generate.py`, `hogwarts.py`, `interpreter.py`, `meal.py`, `calculator.py`).

| Folder | Description |
|---|---|
| `adieu`, `camel`, `einstein`, `emojize`, `faces`, `figlet`, `indoor`, `jar`, `nutrition`, `pizza`, `playback`, `professor`, `seasons`, `taqueria`, `twttr`, `um`, `watch`, `working`, `world` | Python exercises |
| `caesar`, `cash`, `mario-less`, `plates`, `readability`, `fuel`, `speller`, `scrabble` | C exercises |
| `bank`, `bitcoin`, `coke`, `deep`, `goodbye`, `grocery`, `hello`, `inheritance`, `lines`, `me`, `numb3rs`, `outdated`, `response`, `scourgify`, `shirt`, `shirtificate`, `src1`, `tip`, `game`, `project` | Additional exercises and projects |
| `test_bank`, `test_fuel`, `test_plates`, `test_twttr.py` | Unit tests for corresponding exercises |

Open any folder to find the relevant source code and, where applicable, a short description of the assignment.

## Getting Started

To explore or run any of the exercises locally:

```bash
git clone https://github.com/Laketown95/lake.git
cd lake
```

Then navigate into the folder for the exercise you're interested in. Python scripts can be run directly:

```bash
python3 <filename>.py
```

C programs can be compiled with `make` (if a Makefile is present) or directly with `clang`/`gcc`:

```bash
make <filename>
./<filename>
```

Some folders include their own `test_*` files, which can be run with `pytest`:

```bash
pytest test_<name>.py
```

## Academic Honesty

This repository is intended as a personal record of coursework. If you're currently taking CS50, please don't copy this code for your own submissions — doing so violates CS50's [academic honesty policy](https://cs50.harvard.edu/x/academic-honesty/) and your own institution's guidelines. Use it as a reference only after you've made an honest attempt of your own.

## Author

[Laketown95](https://github.com/Laketown95)
