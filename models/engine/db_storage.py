#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import os
from models.base_model import Base


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
            #drop all tables
            pass
