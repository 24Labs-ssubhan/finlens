# FinLens

![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![Flask](https://img.shields.io/badge/Flask-API-lightgrey)
![Build](https://github.com/24Labs-ssubhan/finlens/actions/workflows/python-ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green)

🔎 AI-powered income and expense verifier using Open Banking

# FinLens

🔎 AI-powered income and expense verifier using Open Banking

## Features
- Categorises transactions from bank data
- Computes affordability (income, expenses, surplus)
- Simple Flask API backend
- Mock Open Banking data to start

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python backend/app.py
