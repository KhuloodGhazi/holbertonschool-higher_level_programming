#!/usr/bin/python3
"""
Prints the State object's id with the name passed as argument.
Usage: ./10-model_state_my_get.py
<username> <password> <db_name> <state_name>
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]
        ), pool_pre_ping=True
    )

    session = Session(engine)

    state = session.query(State).filter(State.name == argv[4]).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
