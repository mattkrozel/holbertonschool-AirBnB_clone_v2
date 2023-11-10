#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            ''' getter attribute for cities '''
            from models import storage
            from models.city import City
            citylist = []
            allcities = storage.all(City).values()
            for city in allcities:
                if self.id == city.state_id:
                    citylist.append(city)
            return citylist
