from sqlalchemy import *
from sqlalchemy.sql import *
from database import Base
from database import dbschema

class Login(Base) :
    __tablename__ = "login_table"
    __table_args__ = {'schema': dbschema}
    UserId = Column(Integer, primary_key=True,autoincrement=True)
    Username = Column(String)
    Password = Column(String)