#!/usr/bin/python3
""" This module contains the class definition of a State
and an instance Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class describes a State.
    Links to the MySQL table states.
        @id: represents a column of an auto-generated, unique integer,
            can’t be null and is a primary key
        @name: that represents a column of a string with maximum 128
            characters and can’t be null
    """
    __tablename__ = "states"

    id = Column(
            Integer,
            autoincrement=True,
            unique=True,
            nullable=False,
            primary_key=True)
    name = Column(String(128), nullable=False)
