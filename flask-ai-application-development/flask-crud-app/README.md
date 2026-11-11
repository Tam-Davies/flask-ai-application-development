# PetroWell Manager – Flask CRUD Application

## Overview

PetroWell Manager is a petroleum well management web application built with Python and Flask. It provides an interface for registering, viewing, editing, deleting, and administrating petroleum well records.

The application uses SQLite for persistent data storage and demonstrates additional Flask capabilities through extensions such as Flask-SQLAlchemy, Flask-Migrate, Flask-WTF, Flask-Admin, and Marshmallow.

## Features

- **Create:** Register new petroleum wells.
- **Read:** Retrieve and display registered well records.
- **Update:** Modify existing well information.
- **Delete:** Remove well records.
- **Database Management:** SQLite integration using Flask-SQLAlchemy.
- **Database Migrations:** Schema management using Flask-Migrate and Alembic.
- **Form Validation:** Input validation and CSRF protection using Flask-WTF and WTForms.
- **Administrative Dashboard:** Manage database records through Flask-Admin.
- **Custom Admin Dashboard:** Display total wells and aggregate production.
- **Serialization:** Convert SQLAlchemy model instances into Python dictionaries using Marshmallow.
- **Responsive Interface:** HTML, CSS, and Jinja2 templates.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| Flask-SQLAlchemy | Database ORM |
| SQLite | Relational database |
| Flask-Migrate | Database migrations |
| Flask-WTF | Form handling and CSRF protection |
| WTForms | Form validation |
| Flask-Admin | Administrative interface |
| Marshmallow | Data serialization |
| Jinja2 | HTML templating |
| HTML/CSS | Frontend development |

## Project Structure

```text
flask-crud-app/
├── app.py
├── models.py
├── forms.py
├── schemas.py
├── requirements.txt
├── README.md
├── .gitignore
├── migrations/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── wells.html
│   ├── add_well.html
│   ├── edit_well.html
│   └── admin/
│       └── index.html
├── static/
│   └── css/
│       └── style.css
└── instance/
    └── petro_wells.db
```

The SQLite database is generated locally and is excluded from version control.

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/Tam-Davies/flask-ai-application-development.git
```

Navigate to the project directory:

```bash
cd flask-ai-application-development/flask-crud-app
```

Activate your Python environment and install dependencies:

```bash
pip install -r requirements.txt
```

Initialize and apply database migrations if setting up a fresh database:

```bash
flask --app app db upgrade
```

Start the application:

```bash
python app.py
```

Open the application:

```text
http://127.0.0.1:5000
```

## Application Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Homepage |
| `/wells` | GET | Display all wells |
| `/wells/add` | GET, POST | Register a well |
| `/wells/edit/<well_id>` | GET, POST | Update a well |
| `/wells/delete/<well_id>` | POST | Delete a well |
| `/admin/` | GET | Administrative dashboard |

## Database Model

The `Well` model contains:

- `id`: Unique well identifier.
- `name`: Well name.
- `field`: Petroleum field.
- `depth_m`: Well depth in metres.
- `production_bopd`: Production rate in barrels of oil per day.
- `status`: Operational status.

## Learning Outcomes

This project demonstrates practical knowledge of:

1. Flask application architecture and routing.
2. Database integration and ORM operations.
3. Database migrations and schema management.
4. Form processing, validation, and CSRF protection.
5. Jinja2 template inheritance.
6. Flask extension integration.
7. Administrative interface development.
8. SQLAlchemy model serialization.

## Limitations and Future Improvements

- Implement user authentication and role-based access control.
- Add REST API endpoints for well records.
- Introduce pagination and advanced search.
- Add automated tests.
- Replace SQLite with PostgreSQL for larger deployments.
- Implement production-ready configuration and deployment.

## Project Status

Core CRUD functionality, database integration, form validation, Flask-Admin, and Marshmallow serialization have been implemented and tested.

This project is part of a practical Flask AI application development portfolio.
