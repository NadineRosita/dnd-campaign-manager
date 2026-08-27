# 🎲 D&D Campaign Manager

[![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-pytest-green?logo=pytest)](https://pytest.org/)
[![License](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)

A Python-based command-line application for managing tabletop RPG campaigns, characters and sessions.

---

## 📌 About the Project

D&D Campaign Manager is a personal software project created to practice programming and software engineering fundamentals while building a useful tool for tabletop role-playing campaigns.

The project will evolve alongside my learning journey, starting with a simple command-line application and gradually introducing more advanced concepts.

---

## 🎯 Goals

- Practice Python programming
- Apply software engineering fundamentals
- Work with structured data
- Learn how to organize a larger codebase
- Practise Git and GitHub workflows
- Gradually introduce databases and more advanced features

---

## 🚧 Features

**Early development**

- Create D&D characters
- List all characters
- View character details
- Delete characters
- Validate user input
- Handle invalid data safely
- Save character data to JSON
- Load saved characters when the application starts
- Automated tests with pytest

---

## 🛠️ Technologies

- Python 3
- Object-Oriented Programming
- JSON
- pytest
- Git
- GitHub

---

## 🗺️ Project Structure

```text
dnd-campaign-manager/
│
├── data/
│   └── characters.json
│
├── src/
│   ├── __init__.py
│   ├── character.py
│   ├── character_manager.py
│   └── main.py
│
├── tests/
│   ├── test_character.py
│   ├── test_character_manager.py
│   └── test_persistence.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt