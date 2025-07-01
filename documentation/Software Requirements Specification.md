# 📝 Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Purpose
The goal of this project is to build a Hangman game that evolves from a simple CLI-based version into a full-featured, testable, and deployable application, showcasing software engineering practices suitable for a final-year Computer Science student portfolio.

### 1.2 Scope
This game allows a user to guess letters to reveal a hidden word, with limited attempts. <br />
It includes OOP structure, unit testing, optional GUI or Web interface, and Agile-based planning.

### 1.3 Definitions
- **CLI**: Command-Line Interface
- **GUI**: Graphical User Interface
- **CI/CD**: Continuous Integration/Continuous Deployment
- **SRS**: Software Requirements Specification

---

## 2. Overall Description

### 2.1 Product Perspective
This is a standalone application with modular components: game logic, UI, and an optional API. It is built using Python and optionally Flask or Tkinter.

### 2.2 Product Functions
- Random word generation
- Letter-guessing gameplay loop
- Life tracking and win/loss conditions
- UI rendering
- Hint system (future)
- Score tracking (future)

### 2.3 User Classes and Characteristics
- **Players**: General users playing the game
- **Developers**: Developers modifying or contributing to the code

### 2.4 Operating Environment
- Python 3.11+
- Web browser (Future)
- Any OS (Windows, Linux, macOS)

---

## 3. Specific Requirements

### 3.1 Functional Requirements
- R1: The game must allow a player to guess letters.

- R2: The game must end when the word is guessed or lives are exhausted.

- R3: The word should be chosen randomly.

- R4: The UI must update with each guess.

- R5: The user should be able to see a scoreboard (future)


### 3.2 Non-Functional Requirements
- Code must be modular and testable.
- The system should be responsive and easy to use.
- Unit tests must achieve at least 80% coverage.
- Must be able to handle at least 2 concurrent users (future)

### 3.3 UI Requirements
- CLI: Must display guessed letters, remaining lives, and win/loss.
- GUI: Must include buttons, display word state, and allow restart.

---

## 4. External Interface Requirements

### 4.1 User Interfaces
- CLI: Standard terminal interface
- GUI: Tkinter window (future)
- Web: HTML/CSS via Flask backend (future)

### 4.2 API Interfaces (future)
- `GET /start`: start a new game
- `POST /guess`: submit a letter
- `GET /state`: return current game state

---

## 5. Future Scope
- Multiplayer support (WebSockets)
- Scoreboard and persistent storage
- Dictionary API integration
- Mobile-friendly web interface
- NLP-powered hint system

---
