# Morse Trainer

A modern terminal-based Morse code learning and practice application written in Python.

The goal of this project is to provide a complete environment for learning, practicing, and mastering International Morse Code from beginner to advanced levels.

---

## Features

### Current

- ✅ Text ↔ Morse code translation
- ✅ Unit tested core translation engine
- ✅ Modern Python project structure (`src` layout)
- ✅ Installable as a Python package
- ✅ Terminal application foundation

### Planned

- Flashcard practice
- Character recognition training
- Morse audio playback
- Adjustable WPM (Words Per Minute)
- Farnsworth timing
- Koch learning method
- Lesson progression
- Progress tracking
- Statistics dashboard
- Session history
- Custom practice sets
- Randomized quizzes
- Rich-powered terminal interface
- Configuration system

---

## Project Structure

```
morse-trainer/
│
├── assets/
├── data/
├── src/
│   └── morse_trainer/
│       ├── core/
│       ├── controllers/
│       ├── ui/
│       ├── app.py
│       └── main.py
│
├── tests/
├── pyproject.toml
└── README.md
```

---

## Installation

Clone the repository.

```bash
git clone git@github.com:stopcorptracking/morse-trainer.git
```

Enter the project.

```bash
cd morse-trainer
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install the project in editable mode.

```bash
pip install -e .
```

---

## Running

During development:

```bash
python main.py
```

Eventually the application will also support:

```bash
python -m morse_trainer.main
```

---

## Running Tests

```bash
python -m pytest
```

---

## Development Principles

This project follows a layered architecture.

```
UI
│
Controllers
│
Core
```

### Core

Contains the application logic.

- Morse translation
- Trainer logic
- Statistics
- Timing
- Audio

### Controllers

Coordinate communication between the UI and the application logic.

### UI

Responsible only for terminal interaction.

---

## Technologies

- Python 3.13+
- Rich
- Pytest

Planned additions:

- NumPy
- sounddevice
- soundfile

---

## Roadmap

### Phase 1

- Core translation engine
- Trainer engine
- Unit tests

### Phase 2

- Rich terminal UI
- Flashcards
- Recognition mode

### Phase 3

- Audio generation
- Adjustable WPM
- Farnsworth timing

### Phase 4

- Koch Method
- Lessons
- Progress tracking
- Statistics dashboard

### Phase 5

- Configuration
- User profiles
- Custom practice modes

---

## License

License to be added.

---

## Author

Created by **stopcorptracking** as a long-term Python learning project focused on clean architecture, testing, and terminal application development.
