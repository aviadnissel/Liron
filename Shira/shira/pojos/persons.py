# -*- coding: utf-8 -*- 

from elixir import Entity, Field, Unicode, Enum, ManyToOne, using_options
from shira.pojos.seminar import Ken, SecondKen
from shira.pojos.constants import *

class Person(Entity):
    """
    An abstract person.
    """

    using_options(inheritance='multi')
    first_name = Field(Unicode(60))
    last_name = Field(Unicode(60))
    gender = Field(Enum(MALE, FEMALE))
    food = Field(Enum(MEAT, VEGETARIAN))
    
    def __repr__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Educative(Person):
    """
    An educative in the seminar.
    """
    using_options(inheritance='multi')
    ken = ManyToOne('Ken')
    second_ken = ManyToOne('SecondKen')
    _hug = ManyToOne('Hug')
    
    def _set_hug(self, hug):
        if self._hug != None:
            self._hug.update_count(self, is_removed = True)
        if hug != None:
            hug.update_count(self)
        self._hug = hug
    
    def _get_hug(self):
        return self._hug
    
    hug = property(_get_hug, _set_hug)
        

class Madrich(Person):
    """
    A madrich in the seminar.
    """
    using_options(inheritance='multi')
    ken = ManyToOne('Ken')
    second_ken = ManyToOne('SecondKen')
    hug = ManyToOne('Hug')

