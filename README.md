# Threat Intelligence Platform

A beginner-friendly defensive TIP for storing, searching and reviewing indicators of compromise (IOCs).

## Features
- IP, domain, URL, hash and email IOC types
- Confidence score and source tracking
- SQLite persistence
- Simple web dashboard and JSON API

## Run
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000. This is an educational system and does not claim that an IOC is malicious merely because it was stored.