# Ten Million Project 💰

A desktop savings tracker built with Python and CustomTkinter, designed to help you manage and visualize your savings over time.

## Features

- **Create** savings entries with a name and amount (COP)
- **Read** and filter saved entries
- **Update** entries *(coming soon)*
- **Delete** entries *(coming soon)*
- Live sidebar list that reflects the latest savings records
- Dark mode UI with a clean, minimal layout

## Tech Stack

- **Python 3.x**
- **CustomTkinter** — modern themed Tkinter widgets
- **SQLite** (via `crud.py`) — local database for persistence

## Project Structure
```
ten-million-project/
├── main.py       # UI and view logic
├── crud.py       # Database initialization and CRUD operations
└── README.md
```

## Requirements
```bash
pip install customtkinter
```

## Getting Started
```bash
# 1. Clone the repository
git clone https://github.com/your-username/ten-million-project.git
cd ten-million-project

# 2. Install dependencies
pip install customtkinter

# 3. Run the app
python main.py
```

## Usage

| View | Description |
|------|-------------|
| **CREATE** | Add a new savings entry with a title and COP amount |
| **READ** | Search and browse all saved entries |
| **UPDATE** | *(Coming soon)* |
| **DELETE** | *(Coming soon)* |

## Database

The app initializes a local SQLite database on first run via `init_db()`. Each savings record stores:

- `id` — auto-incremented primary key
- `title` — entry name
- `amount` — amount in COP
- `type` — transaction type (`deposit` or `withdrawal`)
- `created_at` — timestamp

## Version

`0.0.1` — Initial release