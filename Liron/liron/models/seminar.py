# -*- coding: utf-8 -*-

from sqlalchemy import *
from sqlalchemy.orm import relationship
from liron.models import Base
from sqlalchemy.ext.declarative import declarative_base
from liron.models.constants import *
from liron.models.persons import *


class Seminar(Base):
    __tablename__ = 'seminar'

    id = Column(Integer, primary_key=True)
    name = deferred(Column(Unicode(60)))
    camps = relationship('Camp', backref='seminar')

class Camp(Base):
    __tablename__ = 'camp'

    id = Column(Integer, primary_key=True)
    name = deferred(Column(Unicode(60)))
    hugs = relationship('Hug', backref='camp')
    seminar_id = Column(Integer, ForeignKey('seminar.id'))

class Hug(Base):
    """
    A hug in the seminar.
    """
    __tablename__ = 'hug'

    id = Column(Integer, primary_key=True)
    name = deferred(Column(Unicode(60)))
    educatives = relationship('Educative', backref='hug')
    madrichim = relationship('Madrich', backref='hug')
    camp_id = deferred(Column(Integer, ForeignKey('camp.id')))
    food = deferred(Column(Enum(MEAT, VEGETARIAN)))
    
    def __init__(self):
        self.kens_count = {}
        self.second_kens_count = {}
        self.male_count = 0
        self.educatives_count = 0
    
    def __repr__(self):
        return self.name


class AbstractKen(Base):
    """
    An abstract ken class.
    Both ken and second ken inherit from it.
    """
    __tablename__ = 'abstract_ken'

    id = Column(Integer, primary_key=True, index=True)
    name = deferred(Column(Unicode(40)))
    type = deferred(Column(String(20), index=True))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'abstract_ken'
    }

    def __repr__(self):
        return str(self.name)

class Ken(AbstractKen):
    """
    A ken in the seminar.
    """
    __tablename__ = 'ken'
    id = Column(Integer, ForeignKey('abstract_ken.id'), primary_key=True, index=True)
    educatives = relationship('Educative', backref='ken')
    madrichim = relationship('Madrich', backref='ken')

    __mapper_args__ = {
        'polymorphic_identity': 'ken'
    }

class SecondKen(AbstractKen):
    """
    A second ken in the seminar.
    """
    __tablename__ = 'second_ken'
    id = Column(Integer, ForeignKey('abstract_ken.id'), primary_key=True, index=True)
    educatives = relationship('Educative', backref='second_ken')
    madrichim = relationship('Madrich', backref='second_ken')

    __mapper_args__ = {
        'polymorphic_identity':'second_ken'
    }