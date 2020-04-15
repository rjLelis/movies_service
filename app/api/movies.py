from typing import List

from fastapi import APIRouter, HTTPException

from models import Movie

fake_movie_db = [
    {
        'name': 'Star Wars: Episode IX - The Rise of Skywalker',
        'plot': 'The survinving members of the resistence face the First Order once again.',
        'genres': ['Action', 'Adventure', 'Fantasy'],
        'casts': ['Daisy Ridley', 'Adam Driver'],
    }
]

movies = APIRouter()


@movies.get('/movies', response_model=List[Movie])
async def get_all_movies():
    return fake_movie_db


@movies.get('/movies/{id}')
async def get_movie(id: int):
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    return fake_movie_db[id - 1]


@movies.post('/movies', status_code=201)
async def add_movie(payload: Movie):
    movie = payload.dict()
    fake_movie_db.append(movie)
    return {'id': len(fake_movie_db) - 1}


@movies.put('/movies/{id}')
async def update_movie(id: int, payload: Movie):
    movie = payload.dict()
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    fake_movie_db[id] = movie
    return None


@movies.delete('/movies/{id}')
async def delete_movie(id: int):
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    del fake_movie_db[id]
    return None
