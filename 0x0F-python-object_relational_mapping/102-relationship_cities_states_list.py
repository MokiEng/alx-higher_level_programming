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


def list_cities(username, password, database):
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
    for city in cities:
        state_name = city.state.name if city.state else "Unknown"
        print(f'{city.id}: {city.name} ({state_name})')

    '''Close the session.'''
    session.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python script.py <username> <password> <database>')
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    '''Call the function to list cities.'''
    list_cities(username, password, database)
