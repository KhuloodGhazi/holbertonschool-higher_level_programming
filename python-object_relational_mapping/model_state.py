#!/usr/bin/python3
"""
Defines a State class mapped to the states table in MySQL database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base instance to use for all ORM-mapped classes
Base = declarative_base()

class State(Base):
    """
    Represents a state with an id and a name.
    Mapped to the MySQL table `states`.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
