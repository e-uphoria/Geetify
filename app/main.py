from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import router
from app.config import settings
import os

app = FastAPI(title=settings.app_name, version=settings.api_version)

# Path relative to the root directory (not /app)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Mount static files
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Set templates folder
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Include router
app.include_router(router)

# Render home HTML page
@app.get("/", include_in_schema=False)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
