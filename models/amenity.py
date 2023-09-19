#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base
import models
import os
from models.place import Place, place_amenity

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(
        String(128), nullable=False
        ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    place_amenities = relationship(
            'Place',
            secondary=place_amenity,
            back_populates="amenities"
            ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
