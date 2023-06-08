import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine('sqlite:///db/movies.db', echo=True)

# class Role(Base):
#     pass

class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String())

    # movies = relationship("Movie", secondary="", back_populates="actor")

    def __repr__(self):
        return f'Actor: {self.name}'


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String())
    box_office_earnings = Column(Integer())

    # actors = relationship("Role", back_populates="movie")
    
    def __repr__(self):
        return f'Movie: {self.title}'
