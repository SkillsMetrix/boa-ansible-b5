
from sqlalchemy import Column,String

from .database import Base

class Student(Base):
    __tablename__="STUDENT"

    uname=Column(String,primary_key=True)
    email=Column(String)
    city=Column(String)