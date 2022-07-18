from peewee import *
from . import Base

"""CREATE TABLE Authors ( 
  id serial primary key,
  name text not null,
  nick_name text,
  born date,
  died date,
  achievement text
);"""

class Authors(Base):
    id = AutoField(primary_key = True)
    name = TextField()
    nick_name = TextField()
    born = DateField()
    died = DateField()
    achievement = TextField()