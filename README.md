# RuneScape Compare

[![CI](https://github.com/TijnvandenBergh/RuneScapeCompare/actions/workflows/ci.yml/badge.svg)](https://github.com/TijnvandenBergh/RuneScapeCompare/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.9%20|%203.10%20|%203.11%20|%203.12-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.1.3-green)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)

A web application that fetches and displays player statistics from the Old School RuneScape (OSRS) Hiscores API. Look up any player or compare two players side by side.

## About

RuneScape Compare connects to the [OSRS Hiscores API](https://secure.runescape.com/m=hiscore_oldschool/) to retrieve player data such as total level, skill levels, and rankings. The app parses the hiscores lite endpoint and presents the data in a clean web interface.

## Features

- Look up any OSRS player's stats by username
- View combat and non-combat skills with levels, XP, and ranks
- Compare two players side by side
- Error handling for invalid players and API failures

## Tech Stack

- **Framework:** [Flask 3.1.3](https://flask.palletsprojects.com/)
- **Language:** Python 3.9+
- **HTTP Client:** requests
- **Template Engine:** Jinja2

## Project Structure

```
RuneScapeCompare/
├── app/
│   ├── __init__.py              # Application factory
│   ├── routes.py                # Route definitions (Blueprint)
│   ├── models/
│   │   ├── __init__.py
│   │   └── player.py            # Player data model
│   └── templates/
│       ├── base.html            # Base template with layout
│       ├── home.html            # Player lookup page
│       └── compare.html         # Player comparison page
├── tests/
│   ├── conftest.py              # Pytest fixtures
│   ├── test_player.py           # Player model tests
│   └── test_routes.py           # Route tests
├── config.py                    # Configuration classes
├── run.py                       # Application entry point
├── requirements.txt             # Production dependencies
├── requirements-dev.txt         # Development dependencies
└── .gitignore
```

## Prerequisites

- Python 3.9+

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd RuneScapeCompare
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python run.py
   ```
   You should see output like:
   ```
    * Serving Flask app 'app'
    * Debug mode: on
    * Running on http://127.0.0.1:5000
   ```

5. **Open your browser:**
   Navigate to `http://127.0.0.1:5000/` to look up player stats, or `http://127.0.0.1:5000/compare` to compare two players.

### Verified Working

The application has been tested and confirmed working:
- Flask dev server starts on port 5000
- Index page (`/`) renders the player lookup form
- Compare page (`/compare`) renders the comparison form
- Live OSRS Hiscores API calls return player data successfully
- All 28 tests pass with 97% code coverage

## Development

Install dev dependencies for testing:
```bash
pip install -r requirements-dev.txt
```

Run tests with coverage:
```bash
pytest --cov=app --cov-report=term-missing
```

## Configuration

The app uses configuration classes in `config.py`. Set the environment:

```bash
export FLASK_CONFIG=development  # development | testing | production
export SECRET_KEY=your-secret-key  # override default in production
```

## API Reference

The app uses the OSRS Hiscores Lite endpoint:
```
https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=<username>
```

This returns CSV-formatted data with skill rankings, levels, and experience for all 24 OSRS skills.

## Roadmap

Planned features and improvements for future releases:

- [ ] **Player search history** - Remember recently looked-up players using browser local storage
- [ ] **Boss kill counts** - Parse and display boss KC data from the hiscores (available in the API response beyond the 24 skill rows)
- [ ] **Clue scroll tracking** - Show clue scroll completion counts by tier
- [ ] **Player progress over time** - Store snapshots of player stats and visualize XP gains with charts
- [ ] **Multi-player comparison** - Compare more than two players at once in a table view
- [ ] **RS3 support** - Add a toggle to also support RuneScape 3 hiscores (different API endpoint)
- [ ] **Account type badges** - Detect and display ironman, HCIM, and UIM status
- [ ] **REST API** - Expose a JSON API (`/api/player/<name>`) for programmatic access
- [ ] **Dark/light theme toggle** - Let users switch between the dark OSRS theme and a light theme
- [ ] **Deploy to production** - Containerize with Docker and deploy (e.g., Railway, Fly.io, or Render)
- [ ] **Rate limiting** - Add request rate limiting to avoid hitting the OSRS API too aggressively
- [ ] **Caching** - Cache API responses (e.g., with Flask-Caching / Redis) to speed up repeated lookups
