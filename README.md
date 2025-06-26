#  Late Show Guest Appearances API

A Flask-based RESTful API for managing episodes, guests, and appearances on a fictional late-night talk show. Built with SQLAlchemy, Flask-Migrate, and SQLite.

---

## Features

- View all episodes and their guest appearances
- View all guests and their associated episodes
- Create new guest appearances with validation
- Seed sample episode and guest data
- JSON responses for all endpoints

---

## Tech Stack

- Python 3.x
- Flask
- Flask SQLAlchemy
- Flask-Migrate
- SQLite (default)
- SQLAlchemy ORM

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/TheWilliams254/Lateshow.git
cd lateshow
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate 
```
### On Windows:
```bash 
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set environment variables
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

### 5. Initialize the database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Seed the database
```bash
python seed.py
```

### 7. Run the app
```bash
flask run
```

## API Endpoints
GET /episodes
Returns a list of all episodes:

```json
[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  }
]
```

GET /episodes/<id>
Returns a specific episode with its guest appearances:

```json
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "rating": 4,
      "episode_id": 1,
      "guest_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      }
    }
  ]
}
```
POST /appearances
Create a new appearance:

Request body:

```json
{
  "rating": 5,
  "episode_id": 2,
  "guest_id": 3
}
```
Success response (201):

```json
{
  "id": 162,
  "rating": 5,
  "guest_id": 3,
  "episode_id": 2,
  "episode": {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  },
  "guest": {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
}
```
Error response (400/404):

```json
{
  "errors": ["Episode or Guest not found"]
}
```
### Testing
Use Postman, cURL, or browser tools to interact with endpoints. Sample test cases can be added with pytest or unittest.

### License
MIT License. Free to use and modify.

### Author
William Wambugu
williamwambugu663@gmail.com