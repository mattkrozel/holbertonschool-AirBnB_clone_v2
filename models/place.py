#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import os


place_amenity = Table('place_amenity', Base.metadata,
                        Column('place_id', String(60),
                                ForeignKey('places.id'),
                                primary_key=True, nullable=False),
                        Column('amenity_id', String(60),
                                ForeignKey('amenities.id'),
                                primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref='place',
                                cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                                  viewonly=False)
    else:
        @property
        def reviews(self):
            ''' getter attribute for reviews '''
            from models import storage
            review_list = []
            all_reviews = storage.all('Review').values()
            for review in all_reviews:
                if self.id == review.place_id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            ''' getter attribute for amenities '''
            from models import storage
            from models.amenity import Amenity
            amenity_list = []
            all_amenities = storage.all('Amenity').values()
            for amenity in all_amenities:
                if self.id == amenity.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            ''' setter attrbitue '''
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_id.append(obj.id)
