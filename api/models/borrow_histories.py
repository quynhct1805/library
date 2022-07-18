from .books import Books
from .users import Users
from peewee import *
from . import Base

class Borrow_histories(Base):
    """CREATE TABLE Borrow_histories ( 
  id serial primary key,
  user_id int,
  book_id int,
  start_date date not null default current_date,
  end_date date,
  fee float,
  foreign key (user_id) references Users (id),
  foreign key (book_id) references Books (id)
);"""
    id = AutoField(primary_key = True)
    user_id = ForeignKeyField(Users, to_field = "id")
    book_id = ForeignKeyField(Books, to_field="id")
    start_date = DateField()
    end_date = DateField()
    fee = DoubleField()