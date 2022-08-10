#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        # Relacionamos State con City - si se elimina un Estado, se tendrian
        # que eliminar todas las ciudades dentro de ese Estado.
        reviews = relationship('Review', backref="place", cascade="all ,\
                                delete-orphan")
        amenities = relationship('Amenity', backref="places",
                                 secondary=place_amenity,
                                 viewonly=False)
    else:
        # Si se llega a este else es porque se esata en el storage: FileStorage
        # Seteamos un getter (usando el decorador: @property)
        @property
        def reviews(self):
            """
            Getter attribute reviews that returns the list of Review instances
            with place_id equals to the current Place.id => It will be the
            FileStorage relationship between Place and Review
            """
            return_list = []
            # Guardamos todas las ciudades que haya en la clase Review
            reviews = models.storage.all(Review).values()
            for review in reviews:
                # Se compara id del objeto de tipo Place con reviews
                if self.id == review.place_id:
                    # Se guarda el resultado en la lista a retornar
                    return_list.append(models.storage.all(Review)[review])
            return return_list

        @property
        def amenities(self):
            """
            comments
            """
            return_list = []
            # Guardamos todas las ciudades que haya en la clase Review
            amenities = models.storage.all(Amenity).values()
            for amenity in amenities:
                # Se compara id del objeto de tipo Place con reviews
                if self.id == amenity.place_id:
                    # Se guarda el resultado en la lista a retornar
                    return_list.append(models.storage.all(Amenity)[amenity])
            return return_list

        @amenities.setter
        def amenities(self, amenity_obj):
            if amenity_obj.__clas__.__name__ == "Amenity":
                self.amenity_ids.append(amenity_obj.id)
