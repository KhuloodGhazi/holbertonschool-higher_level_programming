#!/usr/bin/python3
"""
Changes the name of a State object with id = 2 to 'New Mexico'
Usage: ./12-model_state_update_id_2.py
<username> <password> <database>
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

    state = session.query(State).get(2)
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
