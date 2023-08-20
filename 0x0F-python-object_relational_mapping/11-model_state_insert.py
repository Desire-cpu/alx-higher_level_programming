#!/usr/bin/python3
"""
Script ts state to the database

Arguments:
    takes in three arguments
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from model_state import Base, State


if __name__ == "__main__":
    mySql_u = sys.argv[1]
    mySql_p = sys.argv[2]
    db_name = sys.argv[3]

    url = {'drivername': 'mysql+mysqldb', 'host': 'localhost',
           'username': mySql_u, 'password': mySql_p, 'database': db_name}

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    new = State(name="Louisiana")
    session.add(new)
    session.commit()

    print(new.id)
