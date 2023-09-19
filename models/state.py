#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from models.city import City
import models
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(
    String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City',
            cascade='all, delete, delete-orphan',
            backref='state'
        )
    else:
        @property
        def cities(self):
            """Returns the cities in this State"""
            from models import storage
            cs_in_state = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    cs_in_state.append(value)
            return cs_in_state
