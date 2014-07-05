# -*- coding: utf-8 -*- 


from sqlalchemy import *
from sqlalchemy.orm import relationship, deferred
from liron.models import Base
from sqlalchemy.ext.declarative import declarative_base
from liron.models.constants import *


class Person(Base):
    """
    An abstract person.
    """
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, index=True)
    first_name = deferred(Column(Unicode(60)))
    last_name = deferred(Column(Unicode(60)))
    tz = deferred(Column(String(12)))
    gender = deferred(Column(Enum(MALE, FEMALE), index=True))
    food = deferred(Column(Enum(MEAT, VEGETARIAN), index=True))
    type = Column(String(20), index=True)

    ken_id = deferred(Column(Integer, ForeignKey('ken.id'), index=True))
    second_ken_id = deferred(Column(Integer, ForeignKey('second_ken.id'), index=True))
    hug_id = deferred(Column(Integer, ForeignKey('hug.id'), index=True))

    __table_args__ = (Index('ix_person_hug_ken', 'hug_id', 'ken_id'),
                    Index('ix_person_hug_second_ken', 'hug_id', 'second_ken_id'),
                    Index('ix_person_hug_gender', 'hug_id', 'gender'))

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': type
    }

    def __repr__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Educative(Person):
    """
    An educative in the seminar.
    """

    __mapper_args__ = {
        'polymorphic_identity': 'educative',
    }
        

class Madrich(Person):
    """
    A madrich in the seminar.
    """


    __mapper_args__ = {
        'polymorphic_identity': 'madrich',
    }