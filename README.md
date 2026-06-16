# Tournament-League-Management-System

# Tournament League Management System

A Python-based Tournament League Management System designed to manage sports tournaments, teams, players, matches, and standings through a structured command-line interface. The project follows a layered architecture with separate CLI, Service, and Data Access layers for maintainability and scalability.

## Features

* Tournament creation and management
* Team registration and management
* Player management
* Match scheduling and tracking
* Sport category management
* Database integration using Supabase
* Modular architecture following separation of concerns

## Architecture

```text
CLI Layer
    ↓
Service Layer
    ↓
DAO Layer
    ↓
Supabase Database
```

## Project Structure

```text
Tournament-League-Management-System/
│
├── src/
│   ├── cli/
│   │   ├── tournament_cli.py
│   │   ├── team_cli.py
│   │   ├── player_cli.py
│   │   ├── match_cli.py
│   │   └── sport_cli.py
│   │
│   ├── dao/
│   │   ├── tournament_dao.py
│   │   ├── team_dao.py
│   │   ├── player_dao.py
│   │   ├── match_dao.py
│   │   └── sport_dao.py
│   │
│   ├── services/
│   ├── db_client.py
│   └── main.py
│
├── app.py
├── requirements.txt
└── README.md
```

## Tech Stack

* Python
* Supabase
* PostgreSQL (via Supabase)
* dotenv

## Design Principles

* Layered Architecture
* Separation of Concerns
* Modular Code Organization
* Data Access Object (DAO) Pattern

## Installation

```bash
git clone <repository-url>
cd Tournament-League-Management-System

pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file and add:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

## Run the Application

```bash
python app.py
```

or

```bash
python src/main.py
```

## Learning Outcomes

* Database integration with Supabase
* Layered software architecture
* DAO pattern implementation
* Python application development
* Modular project organization
* CRUD operations and data management

## Author

T. Spoorthi
