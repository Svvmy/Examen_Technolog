from fastapi import FastAPI
from pymongo import MongoClient

from music import Music
from store import Store

from constants import MUSIC_COLLECTION_NAME, STORE_COLLECTION_NAME, MONGO_HOST, DB_NAME
from utils import (
    extract_initials_artist,
    extract_initials_artist_from_immat,
    extract_music_length_from_immat,
    extract_type_music_from_immat,
    extract_id_from_immat,
)

client = MongoClient('MONGO_HOST')
db = client[DB_NAME]
app = FastAPI()

#Music endpoints
@app.get("/musics")
def get_musics():
    musics = db[MUSIC_COLLECTION_NAME].find()
    
    return musics
    
@app.post("/musics")
def create_musics(music: Music):
    inserted_music = db[MUSIC_COLLECTION_NAME].insert_one(dict(music))
    
    return {"_id": str(inserted_music.inserted_id)} | dict(music)