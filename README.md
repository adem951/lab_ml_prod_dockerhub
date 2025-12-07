# Task Manager - ML Production Lab

Flask application avec PostgreSQL, Docker et CI/CD vers DockerHub.

## Quick Start

### Local
```bash
# Clone et installer
git clone https://github.com/adem951/lab_ml_prod_dockerhub.git
cd lab_ml_prod_dockerhub
pip install -r requirements.txt

# Configurer .env (copier .env.example)
# Lancer
python migrate.py
python app.py
```

### Docker
```bash
docker-compose up --build
```

## GitHub Secrets (Settings → Secrets → Actions)

| Secret | Valeur |
|--------|--------|
| `DOCKERHUB_USERNAME` | Votre username DockerHub |
| `DOCKERHUB_TOKEN` | Token d'accès DockerHub |
| `ENV_VARIABLES` | Voir `.env.example` |

## CI/CD Pipeline

**Pull Request / Push `dev`:** Lint + Tests + Build validation  
**Push `main`:** Build + Push vers DockerHub

## DockerHub
```bash
docker pull <username>/taskmanager:latest
```
