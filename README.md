# OSINT Aggregation Platform

A beginner-friendly OSINT project with:
- **Frontend**: Next.js dashboard
- **Backend**: FastAPI API
- **Worker**: Celery background tasks
- **Data services**: Redis + Neo4j

---

## 1) What this project does

This app helps you create an investigation, run OSINT-style tools, and generate reports.

Main API routes:
- `POST /auth/token`
- `POST /investigation`
- `GET /results/{id}`
- `POST /tools/run`
- `GET /reports/{id}`
- `GET /health`

---

## 2) Easiest way to run it (recommended)

If you are new, use **Docker Compose**. It starts everything for you.

### Step 1: Install these tools first
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (includes Docker Compose)
- [Git](https://git-scm.com/downloads)

### Step 2: Open a terminal in the project folder
If you already cloned the repo, go into it:

```bash
cd Osint
```

### Step 3: Create your `.env` file
Copy the example environment file:

```bash
cp .env.example .env
```

### Step 4: Start everything

```bash
docker compose up --build
```

Wait until the logs say services are running.

### Step 5: Open the app
- Frontend: http://localhost:3000
- Backend API docs (Swagger): http://localhost:8000/docs
- Health check: http://localhost:8000/health
- Neo4j UI: http://localhost:7474

Default Neo4j login from `docker-compose.yml`:
- Username: `neo4j`
- Password: `neo4jpassword`

### Step 6: Stop everything when you are done
Press `Ctrl + C` in the terminal where Docker is running.

To remove containers after stopping:

```bash
docker compose down
```

---

## 3) Quick API test (copy/paste friendly)

After the app is running, try this in a new terminal.

### 3.1 Get a token

```bash
curl -s -X POST http://localhost:8000/auth/token \
  -H "Content-Type: application/json" \
  -d '{"username":"tester","role":"analyst"}'
```

Copy the `access_token` from the response.

### 3.2 Create an investigation
Replace `<TOKEN_HERE>` with your token:

```bash
curl -s -X POST http://localhost:8000/investigation \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN_HERE>" \
  -d '{"full_name":"Jane Doe","email_address":"jane@example.com"}'
```

Copy the investigation `id` from the response.

### 3.3 Get results
Replace `<INVESTIGATION_ID>`:

```bash
curl -s http://localhost:8000/results/<INVESTIGATION_ID> \
  -H "Authorization: Bearer <TOKEN_HERE>"
```

---

## 4) Optional: run frontend/backend separately (for development)

Use this only if you want to develop each service yourself.

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 5) Running checks

### Frontend

```bash
cd frontend
npm run build
# npm run lint (may ask for first-time ESLint setup if not configured yet)
```

### Backend tests

```bash
cd backend
python -m pytest
```

---

## 6) Common problems (and simple fixes)

### “Port already in use”
Another app is already using that port.
- Stop the other app, or
- Change the port mapping in `docker-compose.yml`

### Docker build feels slow the first time
This is normal. First build downloads many dependencies.
Later builds are faster because of cache.

### I changed code but don’t see updates
If using Docker, rebuild:

```bash
docker compose up --build
```

---

## 7) Project structure

- `/frontend` → Next.js UI
- `/backend` → FastAPI API
- `/workers` → Celery workers
- `/docker` → Dockerfiles
- `/docs` → deployment notes
- `/scripts` → helper scripts

---

If you want, I can also create a **very short 5-minute quickstart version** for absolute beginners.
