#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models import Base
import models 
import os

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(
        String(128), nullable=False
        ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
