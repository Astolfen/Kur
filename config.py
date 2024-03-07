# # В файле config.py будут описаны объект приложения Flask и объект,
# # предоставляющий инструменты для взаимодействия с базой данных.

from peewee import *

db = PostgresqlDatabase('cursach', user='postgres', password='1111', host='localhost', port='5432')
db.connect()

class BaseModel(Model):
    class Meta:
        database = db
