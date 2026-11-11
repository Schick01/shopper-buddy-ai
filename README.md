# Shopper Buddy - AI Shopping List Agent

## Overview
Shopper Buddy is an AI agent that manages a shopping list through natural language commands, using function calling to translate user intent into concrete actions (add, remove, view, or clear items). Natural language understanding is handled locally by the **Mistral** model through **Ollama**, integrated via the `langchain_ollama` library, so the assistant runs entirely on your machine without external API calls.

This project was developed for the seminar "Agenti Intelligenti e Machine Learning by Aitho" at the University of Catania (Academic Year 2025), by Alessandro Sciacca.

## Key Features
The key features of this project are:

**Function calling**: the LLM interprets the user's message and returns the name of the function to call along with its arguments in JSON format, which the agent then executes.

**Local LLM inference**: natural language understanding runs locally through Ollama (Mistral model), with no data sent to external services.

**Shopping list management**: add, remove, view, and clear items, with quantity tracking for each item.

**Interactive CLI**: a simple command-line chat interface to talk to the agent in Italian.

## Repository Contents
- `src/agente_spesa_ai/main.py` — entry point, runs the interactive CLI chat loop.
- `src/agente_spesa_ai/agent.py` — builds the prompt, calls the LLM, and dispatches the parsed function call.
- `src/agente_spesa_ai/functions.py` — the shopping list operations (add, remove, view, clear).
- `pyproject.toml` / `poetry.lock` — project dependencies, managed with Poetry.
- `project_report.pdf` — project report (Italian).

## How to Run
Requires [Ollama](https://ollama.com) installed locally with the `mistral` model pulled (`ollama run mistral`).

```bash
poetry install
poetry run python src/agente_spesa_ai/main.py
```
