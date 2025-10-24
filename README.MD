# InspireAPI     🔗[LIVE DEMO](https://inspire-oivj.onrender.com/docs)


A simple REST API serving motivational quotes. Built with FastAPI, SQLite, SQLAlchemy, and Pydantic.

## Features

- Fetch all motivational quotes.
- Fetch a random quote.
- Add new quotes to the database.

## Tech Stack

- Python 3.13
- FastAPI – REST API framework
- SQLite – lightweight database
- SQLAlchemy – ORM for database operations
- Pydantic – input validation and serialization


## Installation

- Clone the repository:

`git clone https://github.com/yourusername/inspire-api.git`
`cd inspire-api`

- Install dependencies:

`pip install -r requirements.txt`


Start the FastAPI server:

`uvicorn main:app --reload`



## API Endpoints
| Endpoint	      | Method | Description          |
|----------------|--------|----------------------|
| /quotes/	      | GET	   | Fetch all quotes     |
| /quotes/random	| GET	   | Fetch a random quote |
| /quotes/	      | POST	  | Add a new quote      |


### Future Improvements

- Add CLI tool to fetch and add quotes.
- Deploy API to Render/Railway/Fly.io.
- Add filters and search.
- Dockerize API for easy deployment.
