#!/usr/bin/env python3
"""
User Class module
"""


from models.base_model import Base, BaseModel


class User(BaseModel, Base):
    """
    User class that inherits from BaseModel
    """
    __tablename__ = "users"
    email = ""
    password = ""
    first_name = ""
    last_name = ""
