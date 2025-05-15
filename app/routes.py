from fastapi import APIRouter, Query, HTTPException
from app.data import songs_db

router = APIRouter()

# Root path route
# @router.get("/")
# def read_root():
   # return {"message": "Welcome to the Mood-Based Music App!"}


#@router.get("/moods")
#def get_moods():
    #return list(songs_db.keys())

@router.get("/moods")
def get_moods():
    return {"moods": list(songs_db.keys())}


@router.get("/music")
def get_music(mood: str = Query(..., description="Your current mood")):
    mood = mood.lower()
    if mood not in songs_db:
        raise HTTPException(status_code=404, detail="Mood not found")
    return {"mood": mood, "songs": songs_db[mood]}
