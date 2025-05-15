import json

def load_songs():
    with open("songs.json", "r") as file:
        return json.load(file)

songs_db = load_songs()
