# Deployment Overview

## Architecture
- Frontend: Next.js + Tailwind dashboard
- Backend: FastAPI orchestration API with JWT + RBAC
- Queue: Celery workers + Redis
- Correlation: Neo4j for relationship graphing
- Reports: JSON/HTML/PDF artifacts under `reports/generated`

## Local startup
```bash
docker compose up --build
```

## Cloud targets
- Render / Railway / DigitalOcean App Platform: deploy `backend`, `worker`, `frontend` as separate services with managed Redis and Neo4j.
- AWS ECS/EKS: use images built from `docker/*.Dockerfile`; apply `k8s/*.yaml` for Kubernetes.

## Build/bootstrapping
1. Configure `.env` from `.env.example`.
2. Run `scripts/install_osint_tools.sh` in build image layer for Python tool installers.
3. Run database migrations when a relational DB is added.

## Security controls
- JWT auth with role enforcement (`viewer`, `analyst`, `admin`)
- Structured audit events
- Environment-based secret injection
- Task-level retries/timeouts in Celery
