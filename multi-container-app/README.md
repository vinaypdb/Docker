# Multi-Container Flask + PostgreSQL App (Using Docker Compose)

This guide demonstrates how to use Docker Compose to create a **production-style, multi-container application** with Flask (as a web API) and PostgreSQL (as a database). It covers containerization, database setup, environment variables, volume management, and inter-service communication—essential concepts for real-world deployment.

## 1. Project Structure

```plaintext
multi-container-app/
├── app/
│   ├── app.py
│   ├── requirements.txt
├── db/
│   └── init.sql
├── Dockerfile
├── docker-compose.yml
└── .env
```

## 2. Flask Application (`app/app.py`)

- **Purpose:** Handles web requests, connects to PostgreSQL, and exposes an endpoint `/` that returns the PostgreSQL version.
- **Key detail:** `host='0.0.0.0'` ensures accessibility from outside the container.

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## 3. Flask Dependencies (`app/requirements.txt`)

```plaintext
flask
psycopg2-binary
```
- Ensures Flask and PostgreSQL Python drivers are installed inside the image.

## 4. Database Bootstrap (`db/init.sql`)

```sql
CREATE TABLE IF NOT EXISTS sample (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);
```
- This script creates a simple table and runs automatically upon DB container startup—ideal for bootstrapping or seeding data.

## 5. Dockerfile

```Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "app.py"]
```
- **Purpose:** Builds a minimal Python image, installs dependencies, copies code, and sets up the entry point for the Flask app.

## 6. Environment Variables (`.env`)

```plaintext
POSTGRES_DB=flaskdb
POSTGRES_USER=flaskuser
POSTGRES_PASSWORD=flaskpass
DB_HOST=db
```
- Variables are referenced throughout Docker Compose and the Flask app for configuration consistency.

## 7. Docker Compose (`docker-compose.yml`)

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - DB_HOST=${DB_HOST}
    depends_on:
      - db

  db:
    image: postgres:14
    restart: always
    volumes:
      - db-data:/var/lib/postgresql/data
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}

volumes:
  db-data:
```

- **Highlights:**
  - Defines two services: `web` (Flask app) and `db` (Postgres).
  - Synchronizes settings using the `.env`.
  - Maps host port 5000 to Flask.
  - Initializes DB schema automatically.
  - Ensures DB data persists across container restarts.

## 8. How Everything Works Together

- `docker-compose up` launches both containers.
- The **db** container initializes PostgreSQL with `init.sql`.
- The **web** container waits for **db** (using `depends_on`), then starts Flask.
- The Flask app pulls its DB credentials from environment variables, establishes a connection to the database service (`db`), and responds to requests with database info.
- Accessing [http://localhost:5000](http://localhost:5000) yields output similar to:
  ```
  Hello from Flask!
  PostgreSQL version: (PostgreSQL 14.x ...)
  ```
---

## 9. Key Learning Concepts

| Concept                | What You Learned                                       |
|------------------------|--------------------------------------------------------|
| Docker Compose         | Simplifies orchestration of multi-container deployments|
| Environment Variables  | Central config reused across app and DB                |
| Volumes                | Data persistence and automatic DB schema setup         |
| Container Networking   | Service discovery via container names                  |
| Flask Production Prep  | Correct network binding inside Docker (`0.0.0.0`)      |
| Layered Dockerfile     | Efficient and readable Python build process            |

**Created by vinaypdb — open for use, learning, and modification. Ideal for DevOps, backend, and full-stack development practice.**