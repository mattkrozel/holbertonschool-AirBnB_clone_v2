#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """This Class manages storage of hbnb models in a database engine"""
    __engine: None
    __session: None

    def __init__(self):
        """Instantiates a new database map object"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv("HBNB_MYSQL_USER"),
                                              os.getenv("HBNB_MYSQL_PWD"),
                                              os.getenv("HBNB_MYSQL_HOST"),
                                              os.getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            self.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects of a certain (or all) Class(es)"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        obj_dict = {}
        if cls is None:
            objects = self.__session.query(User, State, City, Amenity,
                                           Place, Review).all()
        else:
            objects = self.__session.query(cls).all()

        for obj in objects:
            obj_dict.update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

        return obj_dict

    def new(self, obj):
        """Adds object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes object from current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads table data into current database session"""
        from models.base_model import Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
