from typing import List

from fastapi import APIRouter, HTTPException

from app.api.models import MovieIn, MovieOut
from app.api import db_manager

movies = APIRouter()


@movies.get('/', response_model=List[MovieOut])
async def get_all_movies():
    return await db_manager.get_all_movies()


@movies.get('/{id}', response_model=MovieOut)
async def get_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    return movie


@movies.post('/', status_code=201)
async def add_movie(payload: MovieIn):
    movie_id = await db_manager.add_movie(payload)
    response = {
        "id": movie_id,
        **payload.dict()
    }

    return response


@movies.put('/{id}')
async def update_movie(id: int, payload: MovieIn):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie with given id not found")

    update_data = payload.dict(exclude_unset=True)
    movie_in_db = MovieIn(**movie)

    updated_movie = movie_in_db.copy(update=update_data)
    return await db_manager.update_movie(id, update_movie)


@movies.delete('/{id}', status_code=204)
async def delete_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie with given id not found")

    return await db_manager.delete_movie(id)
