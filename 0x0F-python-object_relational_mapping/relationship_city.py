#!/usr/bin/python3
'''
represent a relationship with the class City.
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    ''' class that defines each city.'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
