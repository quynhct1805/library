from .categories import Categories
from .users import Users
from peewee import *
from . import Base
from enum import Enum
from playhouse.postgres_ext import ArrayField


class EnumField(CharField):
    """
    This class enable a Enum like field for Peewee
    """
    def __init__(self, choices, *args, **kwargs):
        super(CharField, self).__init__(*args, **kwargs)
        self.choices = choices


    def db_value(self, value):
        return value


    def python_value(self, value):
        return self.choices(value)


class Status(Enum):
    AVAILABLE = 'Available'
    BORROWING = 'Borrowing'
    OVERDUE = 'Overdue'


class Books(Base):
    id = AutoField(primary_key = True)
    name = TextField()
    user_id = ForeignKeyField(Users, to_field = "id")
    category_id = ForeignKeyField(Categories, to_field = "id")
    author_ids = ArrayField(IntegerField)
    publisher = TextField()
    years = IntegerField()
    pages = IntegerField()
    fee_per_day = DoubleField()
    summary = TextField()
    due_date = DateField()
    book_status = EnumField(choices=Status)
    image = TextField()