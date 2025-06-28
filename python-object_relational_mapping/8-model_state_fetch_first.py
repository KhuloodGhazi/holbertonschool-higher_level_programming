#!/usr/bin/python3
"""
Fetches the first State object from the database hbtn_0e_6_usa.
Usage: ./8-model_state_fetch_first.py
<mysql_username> <mysql_password> <database_name>
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Create engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]
        ), pool_pre_ping=True
    )

    session = Session(engine)

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
