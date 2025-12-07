# Task Manager Application - ML Production Lab

A Flask-based task management application with user authentication and PostgreSQL database, containerized with Docker and deployed via CI/CD pipeline to DockerHub.

## Lab Overview

This project demonstrates:
- Flask application development with PostgreSQL
- Containerization with Docker
- CI/CD pipeline with GitHub Actions
- Automated image publishing to DockerHub
- Production deployment with NeonDB

## Description

This is a web application that allows users to register, login, and manage their personal tasks. Users can create, edit, toggle completion status, and delete tasks. Each task can have a title, description, and due date.

## Features

- User registration and authentication
- Create, read, update, and delete tasks
- Mark tasks as completed or incomplete
- Set due dates for tasks
- Filter tasks by status (all, open, done)
- Automatic overdue task detection

## Technologies Used

- Python 3.10+
- Flask 3.0.2
- PostgreSQL 18
- SQLAlchemy
- psycopg2-binary
- python-dotenv

## Prerequisites

- Python 3.10 or higher
- PostgreSQL 18
- pip (Python package manager)

## Local Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd flask-app
```

### 2. Create Virtual Environment

```bash
python -m venv Lab_dockerhub
```

Activate the virtual environment:

- Windows: `.\Lab_dockerhub\Scripts\Activate.ps1`
- Linux/Mac: `source Lab_dockerhub/bin/activate`

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Create a PostgreSQL database:

```bash
psql -U postgres -c "CREATE DATABASE taskmanager;"
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory:

```
SECRET_KEY="your-secret-key-here"
POSTGRES_USER="postgres"
POSTGRES_PASSWORD="your-postgres-password"
POSTGRES_HOST="localhost"
POSTGRES_PORT="5432"
POSTGRES_DB="taskmanager"
```

### 6. Run Database Migrations

```bash
python migrate.py
```

### 7. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Running with Docker

### Build and Run with Docker Compose

```bash
docker-compose up --build
```

The application will be available at `http://localhost:5000`

### Stop the Application

```bash
docker-compose down
```

## CI/CD Pipeline with GitHub Actions

This project uses GitHub Actions to automatically build and push Docker images to DockerHub.

### Setup GitHub Secrets

1. Go to your GitHub repository
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Add the following secrets:
   - `DOCKERHUB_USERNAME`: Your DockerHub username
   - `DOCKERHUB_TOKEN`: Your DockerHub access token

### Workflow

The GitHub Actions workflow (`.github/workflows/docker-publish.yml`) automatically:
- Triggers on push to main/master branch
- Builds the Docker image
- Tags the image with branch name, SHA, and 'latest'
- Pushes the image to DockerHub

## Docker Hub

The Docker image is available on Docker Hub:

```bash
docker pull <your-dockerhub-username>/taskmanager:latest
```

### Run from DockerHub

```bash
docker run -d -p 5000:5000 \
  -e SECRET_KEY="your-secret-key" \
  -e DATABASE_URL="postgresql://user:pass@host:5432/dbname" \
  --name taskmanager \
  <your-dockerhub-username>/taskmanager:latest
```

## Running Tests

### Install Test Dependencies

```bash
pip install pytest selenium webdriver-manager pytest-cov
```

### Create Test Database

```bash
psql -U postgres -c "CREATE DATABASE taskmanager_test;"
```

### Run All Tests

```bash
pytest tests/
```

### Run Specific Test Suites

Unit tests:
```bash
pytest tests/test_unit.py
```

Integration tests:
```bash
pytest tests/test_integration.py
```

End-to-end tests:
```bash
pytest tests/test_e2e.py
```

### Run Tests with Coverage

```bash
pytest --cov=. tests/
```

## Project Structure

```
.
├── app.py                 # Main application file
├── models.py              # Database models
├── extensions.py          # Flask extensions
├── migrate.py             # Database migration script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in git)
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── task_form.html
└── tests/                # Test files
    ├── __init__.py
    ├── conftest.py
    ├── test_unit.py
    ├── test_integration.py
    └── test_e2e.py
```

## API Endpoints

- `GET /` - Task list (requires authentication)
- `GET /login` - Login page
- `POST /login` - Login user
- `GET /register` - Registration page
- `POST /register` - Register new user
- `GET /logout` - Logout user
- `GET /tasks/new` - Create task form
- `POST /tasks/new` - Create new task
- `GET /tasks/<id>/edit` - Edit task form
- `POST /tasks/<id>/edit` - Update task
- `POST /tasks/<id>/toggle` - Toggle task completion
- `POST /tasks/<id>/delete` - Delete task

## Environment Variables

### Local Development

| Variable | Description | Default |
|----------|-------------|---------|
| SECRET_KEY | Flask secret key | dev-unsafe-secret |
| POSTGRES_USER | PostgreSQL username | postgres |
| POSTGRES_PASSWORD | PostgreSQL password | postgres |
| POSTGRES_HOST | PostgreSQL host | localhost |
| POSTGRES_PORT | PostgreSQL port | 5432 |
| POSTGRES_DB | Database name | taskmanager |

### Production (Docker)

For production deployment, use `DATABASE_URL`:

```
DATABASE_URL=postgresql://user:password@host:port/database
SECRET_KEY=your-production-secret-key
```

## Production Deployment

### Using NeonDB (Recommended)

1. Create a NeonDB account at [neon.tech](https://neon.tech)
2. Create a new project and database
3. Get your connection string
4. Run the container:

```bash
docker run -d -p 5000:5000 \
  -e SECRET_KEY="your-production-secret-key" \
  -e DATABASE_URL="postgresql://user:pass@host.neon.tech:5432/dbname?sslmode=require" \
  --name taskmanager-prod \
  <your-dockerhub-username>/taskmanager:latest
```

## License

This project is for educational purposes.

## Author

Created as part of ML Production and DockerHub deployment lab.
