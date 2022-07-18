from .books import Books
from .users import Users
from peewee import *
from . import Base


class Reviews(Base):
  id = AutoField(primary_key = True)
  user_id = ForeignKeyField(Users, to_field = "id", unique = True)
  book_id = ForeignKeyField(Books, to_field = "id", unique = True)
  rate_stars = FloatField()
  comment = TextField()
  created_at = DateTimeField()
  updated_at = DateTimeField()
