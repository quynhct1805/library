from peewee import *
from . import Base


class Categories(Base):
    id = AutoField(primary_key = True)
    name = TextField(null = True, unique = True)
    description = TextField()