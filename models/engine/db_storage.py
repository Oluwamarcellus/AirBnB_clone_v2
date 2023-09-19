import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

class DBStorage:
    """ New engine DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """ Public instance methods"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST', 'localhost'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session"""
        from models import base_model
        session = self.__session

        if cls is None:
            all_objs = {}
            for class_name in base_model.classes:
                class_objs = session.query(base_model.classes[class_name]).all()
                for obj in class_objs:
                    key = "{}.{}".format(class_name, obj.id)
                    all_objs[key] = obj
            return all_objs
        else:
            class_objs = session.query(cls).all()
            return {"{}.{}".format(cls.__name__, obj.id): obj for obj in class_objs}

    def new(self, obj):
        """ add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()


