# Petroleum Well Data API

A RESTful API built with Python and Flask to manage petroleum well records. This project demonstrates API development, CRUD operations, input validation, HTTP status codes, error handling, and integration with an external API.

Developed as part of my practical learning journey in **AI Application Development with Flask**.

## Project Objectives

- Build RESTful API endpoints using Flask.
- Implement Create, Read, Update, and Delete (CRUD) operations.
- Validate incoming JSON data.
- Handle HTTP errors and return appropriate status codes.
- Consume external APIs using Python Requests.
- Apply API development concepts to a petroleum engineering use case.

## Technologies Used

- Python 3.12
- Flask
- Requests
- REST API
- JSON
- cURL

## Project Structure

```text
01-flask-api/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd flask-ai-application-development/01-flask-api
```

### 2. Create a virtual environment

```bash
python3 -m venv flask_venv
```

### 3. Activate the environment

```bash
source flask_venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

The API will be available at:

`http://127.0.0.1:5000`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/api/wells` | Retrieve all wells |
| GET | `/api/wells/<well_id>` | Retrieve a specific well |
| POST | `/api/wells` | Create a new well |
| PUT | `/api/wells/<well_id>` | Replace a well's information |
| PATCH | `/api/wells/<well_id>` | Partially update a well |
| DELETE | `/api/wells/<well_id>` | Delete a well |
| GET | `/api/books/<isbn>` | Retrieve book information from Open Library |

## Sample Well Record

```json
{
    "id": 1,
    "name": "Well A",
    "field": "Escravos",
    "depth_m": 2500
}
```

## Example API Requests

### Retrieve all wells

```bash
curl http://127.0.0.1:5000/api/wells
```

### Retrieve a specific well

```bash
curl http://127.0.0.1:5000/api/wells/1
```

### Create a new well

```bash
curl -X POST http://127.0.0.1:5000/api/wells \
-H "Content-Type: application/json" \
-d '{"name":"Well D","field":"Forcados","depth_m":3000}'
```

### Update a well

```bash
curl -X PUT http://127.0.0.1:5000/api/wells/1 \
-H "Content-Type: application/json" \
-d '{"name":"Well A Updated","field":"Escravos","depth_m":2600}'
```

### Partially update a well

```bash
curl -X PATCH http://127.0.0.1:5000/api/wells/1 \
-H "Content-Type: application/json" \
-d '{"depth_m":2700}'
```

### Delete a well

```bash
curl -X DELETE http://127.0.0.1:5000/api/wells/1
```

## External API Integration

The project also integrates with the Open Library API to retrieve book information using an ISBN.

Example:

```bash
curl http://127.0.0.1:5000/api/books/9780140328721
```

This demonstrates how a Flask application can consume external services and handle responses, timeouts, and connection errors.

## Error Handling

The API implements HTTP error handling for common scenarios:

| Status Code | Meaning |
|---|---|
| 200 | Successful request |
| 201 | Resource created |
| 400 | Invalid request or input |
| 404 | Resource or endpoint not found |
| 405 | HTTP method not allowed |
| 500 | Internal server error |
| 502 | External API unavailable |
| 504 | External API timeout |

## Design Notes and Limitations

- Well records are currently stored in Python memory.
- Data resets whenever the application restarts.
- Database persistence and authentication are outside the scope of this first project.
- The API is intended for learning and demonstration, not production deployment.

## Learning Outcomes

Through this project, I practised:

1. Flask application initialization and routing.
2. RESTful API design.
3. CRUD implementation.
4. JSON request and response handling.
5. Input validation.
6. HTTP status codes and error handling.
7. External API integration using Requests.

## Future Improvements

- Integrate a relational database using Flask-SQLAlchemy.
- Add authentication and authorization.
- Introduce automated API testing.
- Deploy the application to a cloud platform.
- Extend the API to support additional petroleum engineering datasets.

---

**Project:** 01 – Building an API with Flask  
**Domain:** Petroleum Engineering and Data Applications  
**Learning Track:** AI Application Development with Flask