from peewee import *
from . import Base


class Categories(Base):
    id = AutoField(primary_key = True)
    code = TextField(unique = True)
    name = TextField(unique = True)
    description = TextField()