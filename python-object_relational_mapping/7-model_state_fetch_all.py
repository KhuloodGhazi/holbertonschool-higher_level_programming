#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.

Usage: ./7-model_state_fetch_all.py
<mysql_username> <mysql_password> <database_name>
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    session = Session(engine)

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
