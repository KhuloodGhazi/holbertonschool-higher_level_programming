#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
formatted as <state name>: (<city id>) <city name>
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]
        ),
        pool_pre_ping=True
    )

    session = Session(engine)

    cities = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
