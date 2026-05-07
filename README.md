# OSINT Aggregation Platform

Production-focused defensive OSINT platform with FastAPI orchestration, Celery workers, Redis queueing, Neo4j correlation, and Next.js dashboard.

## Folder structure
- `/frontend` Next.js + TypeScript + Tailwind dashboard
- `/backend` FastAPI API and orchestration engine
- `/workers` Celery workers/tasks
- `/tools` adapter model lives under `backend/app/tools`
- `/reports` generated JSON/HTML/PDF reports
- `/docker` container images
- `/scripts` deployment/bootstrap scripts
- `/docs` deployment docs

## API
- `POST /investigation`
- `GET /results/{id}`
- `GET /reports/{id}`
- `POST /tools/run`
- `GET /health`

## Quick start
```bash
docker compose up --build
```

See `/docs/deployment.md` for cloud deployment notes and security guidance.
