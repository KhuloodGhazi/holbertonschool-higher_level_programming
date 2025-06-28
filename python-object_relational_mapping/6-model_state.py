#!/usr/bin/python3
"""Creates the states table in the database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    # Connect to MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    # Create all tables
    Base.metadata.create_all(engine)
