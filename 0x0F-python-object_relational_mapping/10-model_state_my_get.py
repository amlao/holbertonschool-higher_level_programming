#!/usr/bin/python3
"""
prints the State object with the name passed as argument from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    sus = session()

    test = sus.query(State).filter(State.name == argv[4]).all()
    if len(test) == 0:
        print("Not found")
    for e in test:
        print("{}: {}".format(e.id, e.name))
