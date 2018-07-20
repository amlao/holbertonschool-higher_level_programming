#!/usr/bin/python3
"""
City Class
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ City Class Inherited From Base """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True, nullable=False,\
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
