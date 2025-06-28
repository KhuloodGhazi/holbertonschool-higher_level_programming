#!/usr/bin/python3
"""
This module defines a class State that inherits from Base.
It links to the MySQL table 'states'.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base instance
Base = declarative_base()


class State(Base):
    """
    State class that maps to the states table in MySQL.
    Attributes:
        id (int): The state's id, primary key.
        name (str): The name of the state.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
