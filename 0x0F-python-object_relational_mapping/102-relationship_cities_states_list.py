#!/usr/bin/python3
'''
a script that lists all City objects from
the database hbtn_0e_101_usa.
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == "__main__":
    '''Create a SQLAlchemy engine to connect to the MySQL server.'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    '''Bind the engine to the Base class.'''
    Base.metadata.bind = engine

    '''Create a session to interact with the database.'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Query all City objects and their associated State objects.'''
    cities = session.query(City).order_by(City.id).all()

    '''Display the cities.'''
    for instance in session.query(State).order_by(State.id):
        for city_ins in instance.cities:
            print(city_ins.id, city_ins.name, sep=": ", end="")
            print(" -> " + instance.name)

    '''Close the session.'''
    session.close()
