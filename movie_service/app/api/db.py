import os

from databases import Database
from sqlalchemy import (ARRAY, Column, Integer, MetaData, String, Table,
                        create_engine)

DATABASE_URL = 'postgresql://root:root@localhost/django'
# DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts', ARRAY(Integer))
)

database = Database(DATABASE_URL)
