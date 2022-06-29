from peewee import *
from . import Base


class Users(Base):
    id = AutoField(primary_key = True)
    name = TextField(unique = True, null = True)
    phone = TextField(unique = True)
    email = TextField(unique = True, null = True)
    balance = DoubleField()
    active = BooleanField(default = True)


