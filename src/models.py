import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(Integer)
    population = Column(Integer)

    def to_dict(self):
        return {}

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), unique=True)
    planet = relationship(Planets, primaryjoin=planet_id == Planets.id)
    
    def to_dict(self):
        return {}

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    length = Column(Integer)

    def to_dict(self):
        return {}

class FavoriteVehicles(Base):
    __tablename__ = 'favorite_vehicles'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), unique=True)
    vehicle = relationship(Vehicles, primaryjoin=vehicle_id == Vehicles.id)

    def to_dict(self):
        return {}

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship(Planets, primaryjoin=planet_id == Planets.id)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship(Vehicles, primaryjoin=vehicle_id == Vehicles.id)

    def to_dict(self):
        return {}

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'), unique=True)
    character = relationship(Character, primaryjoin=character_id == Character.id)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')