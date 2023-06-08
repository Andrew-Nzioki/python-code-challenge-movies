import os
import sys

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///db/movies.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    character_name = Column(String())
    salary = Column(Integer())
    movie_id = Column(Integer, ForeignKey('movies.id'))
    actor_id = Column(Integer, ForeignKey('actors.id'))

    movie = relationship("Movie", back_populates="roles")
    actor = relationship("Actor", back_populates="roles")

    def credit(self):
        return f"{self.character_name}: Played by {self.actor.name}"


class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String())

    roles = relationship("Role", back_populates="actor")

    def movies(self):
        return [role.movie for role in self.roles]

    def total_salary(self):
        return sum(role.salary for role in self.roles)

    def blockbusters(self):
        return [role.movie for role in self.roles if role.movie.box_office_earnings > 50000000]

    @classmethod
    def most_successful(cls):
        actors = session.query(cls).all()
        return max(actors, key=lambda actor: actor.total_salary())

    def __repr__(self):
        return f'Actor: {self.name}'


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String())
    box_office_earnings = Column(Integer())

    roles = relationship("Role", back_populates="movie")

    def actors(self):
        return [role.actor for role in self.roles]

    def all_credits(self):
        return [role.credit() for role in self.roles]

    def cast_role(self, actor, character_name, salary):
        role = Role(character_name=character_name, salary=salary)
        self.roles.append(role)
        actor.roles.append(role)
        session.commit()

    def fire_actor(self, actor):
        for role in self.roles:
            if role.actor == actor:
                self.roles.remove(role)
                session.delete(role)
        session.commit()

    def __repr__(self):
        return f'Movie: {self.title}'
