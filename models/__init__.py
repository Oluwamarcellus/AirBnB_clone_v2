#!/usr/bin/python3
"""This module instantiates an object of class db_Storage"""

import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


if os.gentenv('HBNB_TYPE_STORAGE') == 'db':
    storage  = DBStorage()
else:
    storage = FileStorage()
    
storage.reload()
