# Leaderboard_Service

> Microservice exposing a top 10 leaderboard of users ranked by their quiz scores.

![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

## Overview

Microservice exposing a top 10 leaderboard of users ranked by their quiz scores.

## Tech Stack

Python, FastAPI

## Features

- Top 10 ranking by score
- Ranked user data returned as JSON
- Integrates with the quiz scoring system

## Getting Started

### Prerequisites

Make sure you have the tools required for this stack installed (e.g. Python 3.10+, Node.js 18+, or Android Studio).

### Installation & Usage

```bash
git clone https://github.com/<your-username>/Leaderboard_Service.git
cd Leaderboard_Service
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
Interactive API docs: http://localhost:8000/docs
> Adjust `main:app` if your entry module is named differently.

## Contributing

Contributions are welcome. Fork the repo, create a feature branch, and open a pull request.

## License

Distributed under the MIT License (change as needed).

## Author

**Louai**: [GitHub](https://github.com/<louals>)
