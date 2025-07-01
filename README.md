# 🎮 Advanced Hangman Game

A feature-rich Hangman game built in Python.  
This project follows Agile development principles, starting from a simple terminal-based version and evolving into a structured, testable, and potentially deployable application with a GUI and/or web interface.

---

## 🚀 Demo

<!-- 
[👉 Live Demo](https://your-deployment-link.com)  
Or clone and run locally (see instructions below).
-->

Clone and run locally (see instruction below

---

## 📌 Possible Features

- Modular, object-oriented design
- Terminal-based gameplay
- GUI (Tkinter) and/or Web Interface (Flask)
- Clean codebase with comments and docstrings
- Integrated unit tests with `pytest`
- GitHub Actions for automated testing (CI)
- Docker support
- Agile-style development log
- Ready for deployment
- Multiplayer mode
- Word difficulty levels
- Scoreboard and persistent stats
- Online dictionary integration (using API)
- Hint system using NLP
- Dark mode (UI)
- Mobile-friendly web version

---

## 📂 Project Structure

hangman_project/ <br />
│ <br />
├── documentation/ # Documentation <br />
│ <br />
├── src/ # Core game logic <br />
│ ├── game.py # HangmanGame class <br />
│ ├── word_provider.py # Word selection logic (static or API) <br />
│ └── ui_terminal.py # Terminal version of the game <br />
│ <br />
├── tests/ # Unit tests <br />
│ └── test_game.py <br />
│ <br />
├── web/ # Optional Flask web interface <br />
│ ├── app.py <br />
│ ├── templates/ <br />
│ └── static/ <br />
│ <br />
├── .github/workflows/ # CI configuration <br />
│ └── python-app.yml <br />
│ <br />
├── Dockerfile # For Optional docker deployment <br />
├── requirements.txt # Dependencies <br />
├── README.md # Project documentation <br />
└── development-log.md # Sprint log and Agile documentation <br />

---

## 🧑‍💻 How to Run

### 🔹 Terminal Version

```bash
git clone https://github.com/yourusername/hangman_project.git
cd hangman_project
pip install -r requirements.txt
python src/ui_terminal.py
```

<!-- 
---

### 🔹 Web Version 

```bash
cd web
python app.py
Then visit http://localhost:5000 in your browser.
```

-->

<!--
---

### 🧪 Running Tests

```bash
pytest tests/
-->

<!--
---

### 🐳 Docker

```bash
docker build -t hangman-app .
docker run -p 5000:5000 hangman-app
```
-->
---

### 🌀 Agile Methodology

This project was developed using Agile principles.
The progress is documented in development-log.md, following sprints like:

- Sprint 1: Basic CLI game logic

- Sprint 2: Refactor & UI development

- Sprint 3: Testing, CI, and optional deployment

---

### 👨‍🎓 About the Author
Lesedi Manoto <br />
Final-Year Computer Science Student <br />
Passionate about clean code, interactive design, and full-stack development. <br />
<br />
Connect with me on [LinkedIn](https://www.linkedin.com/in/lesedimanoto/) <br />
<!-- Portfolio: -->


