# 🎧 Geetify – Mood-Based Music Suggester

A simple FastAPI microservice that suggests music tracks based on your current mood.

🚀 Features

- Suggest songs for moods like happy, sad, and focus

- Simple REST API with two main endpoints:
  - `/moods` — lists all available moods
  - `/music?mood={mood}` — returns song suggestions for the specified mood

- Uses a JSON file (`songs.json`) as the data source (no database needed)

- Configurable via environment variables using Pydantic and `.env`

- Dockerized for easy deployment and consistency

- Includes automated testing with Pytest

- Continuous Integration workflow using GitHub Actions

- Serves a simple homepage rendered with Jinja2 templates


## 🚀 How to Run

uvicorn app.main:app --reload

## Run with Docker

Build the Docker image:
docker build -t geetify .

Run the container:
docker run -d -p 8000:8000 geetify

Open your browser at:
http://localhost:8000/doc