# В файле models.py с использованием объявленной в config.py базы
# данных будут объявлены базовые модели и все модели, необходимые для работы приложения.
import peewee as pw
from config import BaseModel, db


class UserRole(BaseModel):
    id = pw.AutoField(column_name='id_role')
    name = pw.CharField(max_length=50, null=False, column_name='name_role')

    class Meta:
        database = db
        table_name = 'user_role'


class User(BaseModel):
    name = pw.CharField(primary_key=True, max_length=50, null=False, unique=True, column_name='name_user')
    password = pw.CharField(max_length=50, null=False, column_name='password_user')
    role = pw.ForeignKeyField(UserRole, backref='users', null=False, column_name='role_user')

    class Meta:
        database = db
        table_name = 'user'


class Actor(BaseModel):
    id = pw.AutoField(column_name='id_actor')
    name = pw.CharField(max_length=100, unique=True, null=False, column_name='name_actor')
    age = pw.IntegerField(null=False, column_name='age_actor')

    class Meta:
        database = db
        table_name = 'actor'


class Genres(BaseModel):
    id = pw.AutoField(column_name='id_genres')
    name = pw.CharField(max_length=100, unique=True, null=False, column_name='name_genres')

    class Meta:
        database = db
        table_name = 'genres'


class Movie(BaseModel):
    id = pw.AutoField(column_name='id_movie')
    name = pw.CharField(max_length=100, null=False, column_name='name_movie')
    releaseYear = pw.IntegerField(column_name='release_year')
    description = pw.CharField(max_length=500, column_name='description')

    class Meta:
        database = db
        table_name = 'movie'


class GenresMovie(BaseModel):
    movie_id = pw.ForeignKeyField(Movie, backref='genmovies', null=False, column_name='movie_id')
    genres_id = pw.ForeignKeyField(Genres, backref='genmovies', null=False, column_name='genres_id')

    class Meta:
        database = db
        table_name = 'genres_movie'
        primary_key = pw.CompositeKey('movie_id', 'genres_id')


class PlayMovie(BaseModel):
    movie_id = pw.ForeignKeyField(Movie, backref='plmovies', null=False, column_name='movie_id')
    actor_id = pw.ForeignKeyField(Actor, backref='plmovies', null=False, column_name='actor_id')

    class Meta:
        database = db
        table_name = 'play_movie'
        primary_key = pw.CompositeKey('movie_id', 'actor_id')




# Создание таблиц для всех моделей
with db:
    db.create_tables([
        User, UserRole, Actor, Movie, GenresMovie, Genres, PlayMovie])
