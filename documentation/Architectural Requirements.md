# 🏛️ Software Architecture Document

## 1. Overview

This document describes the architecture of the Hangman Game project including its key components, data flow, and technologies used.

---

## 2. Architecture Goals

- **Scalability** (modular code for future features)
- **Maintainability** (clean design, unit testing, CI/CD pipeline)
- **Cross-platform deployment**
- **Performance** <br>

---

## 3. System Components

### 3.1 Game Logic
- `HangmanGame`: Manages word state, guesses, lives
- `WordProvider`: Fetches or selects words
- `GameState`: Tracks current progress

### 3.2 User Interface
- CLI: `ui_terminal.py`
- GUI: Tkinter (future)
- Web: Flask-based interface with Jinja templates (future)

### 3.3 Optional Services
- Scoreboard system (SQLite/JSON)
- Word API (Wordnik, Datamuse)
- Multiplayer (WebSockets)

---

## 4. Technology Stack

| Layer         | Technology      |
|---------------|------------------|
| Language      | Python 3.11+     |
| CLI           | Standard I/O     |
| GUI           | Tkinter          |
| Web API       | Flask            |
| CI/CD         | GitHub Actions   |
| Testing       | Pytest           |
| Container     | Docker           |

## 5. Design Patterns Used

- **Strategy Pattern**: Difficulty modes (easy/medium/hard)
- **Observer **: UI reacting to state changes
- **Factory **: Game modes or players
- **State**: Each state of the game (head, arm, etc.)

---

## 6. Risks and Mitigations

| Risk                             | Mitigation                              |
|----------------------------------|------------------------------------------|
| Feature creep                    | Stick to sprint plans and backlog scope |
| API downtime (word fetch)        | Use fallback local word list            |
| GUI unresponsiveness             | Use event-based programming             |

---

## 7. Agile Integration

Development was managed through mini-sprints with progress documented in `development-log.md`.
