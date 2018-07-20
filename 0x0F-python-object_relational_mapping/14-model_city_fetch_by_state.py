#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.\
                           format(argv[1], argv[2], argv[3]),\
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    sus = session()

    for e in sus.query(City).order_by(City.id).all():
        print("{}: ({}) {}".format(e.state_id, e.id, e.name))
