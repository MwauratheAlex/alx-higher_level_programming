#!/usr/bin/python3
"""contains the class definition of a City"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """Describes a state"""
    __tablename__ = "cities"
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128),  nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
