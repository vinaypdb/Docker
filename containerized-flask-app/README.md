# 🚀 Containerized Flask Web Application (Beginner)

## 🌟 Goal

Learn the basics of Docker by building and containerizing a simple Flask-based Python web application.

---

## 🧰 Tech Stack

* **Programming Language**: Python (Flask)
* **Containerization Tool**: Docker

---

## 📁 Folder Structure

```
containerized-flask-app/
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🧱 Step-by-Step Guide

### 1. ✅ Initialize the Project Directory

```bash
mkdir containerized-flask-app
cd containerized-flask-app
```

---

### 2. 📝 Create `app.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🌟 Crafted with purpose by vinaypdb — 'Don't just deploy apps, deploy your passion.' 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

### 3. 🧾 Create `requirements.txt`

```txt
flask
```

---

### 4. 🐳 Create `Dockerfile`

```Dockerfile
# Use an official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application
COPY . .

# Expose the app port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
```

---

### 5. 🔨 Build the Docker Image

Run this in the project directory (where the `Dockerfile` is located):

```bash
docker build -t flask-docker-app .
```

---

### 6. 🚀 Run the Docker Container

```bash
docker run -p 5000:5000 flask-docker-app
```

---

### 7. 🌐 Access the Application

Open your browser and go to:

👉 [http://localhost:5000](http://localhost:5000)

You should see:

```
🌟 Crafted with purpose by vinaypdb — 'Don't just deploy apps, deploy your passion.' 🚀
```

---

### 🧼 Stop the Running Container

In the terminal where it's running, press:

```bash
CTRL + C
```

Or list and stop it:

```bash
docker ps                # Get container ID
docker stop <container_id>
```

---

### 🧪 Helpful Docker Commands

| Command                             | Description                     |
| ----------------------------------- | ------------------------------- |
| `docker build -t name .`            | Build image                     |
| `docker run -p host:container name` | Run container with port mapping |
| `docker ps`                         | List running containers         |
| `docker stop <id>`                  | Stop a container                |
| `docker rm <id>`                    | Remove a container              |
| `docker rmi <image>`                | Remove an image                 |

---

## ✅ Project Status

✅ Basic Flask app built
✅ Dockerized
✅ Custom message
✅ Successfully tested via `localhost`

---

## 🪄 What's Next (Advanced Ideas)

* Use **HTML templates**
* Add a **database** with Docker Compose
* Implement **CI/CD with GitHub Actions**
* Push to **Docker Hub**
* Deploy to **cloud** (AWS EC2, EKS, or Render)

---

## 💍 Credits

This project was proudly built by **vinaypdb** to demonstrate hands-on containerization using Docker and Flask.

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute it.
