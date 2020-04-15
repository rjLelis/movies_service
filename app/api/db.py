from sqlalchemy import (ARRAY, Column, Integer, MedaData, String, Table,
                        create_engine)

from databases import Database

DATABASE_URL = 'postgresql://root:root@localhost/django'

engine = create_engine(DATABASE_URL)
metadata = MedaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts', ARRAY(String))
)

database = Database(DATABASE_URL)
