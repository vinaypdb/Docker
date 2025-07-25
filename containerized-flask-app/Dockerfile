# Use the official Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy files into the container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port for the app
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
