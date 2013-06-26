# -*- coding: utf-8 -*- 

from elixir import Entity, Field, Unicode, Enum, ManyToOne, using_options
from shira.pojos.seminar import Ken, SecondKen

class Person(Entity):
    """
    An abstract person.
    """
	MALE = u'זכר'
	FEMALE = u'נקבה'
	using_options(inheritance='multi')
	first_name = Field(Unicode(60))
	last_name = Field(Unicode(60))
	gender = Field(Enum(MALE, FEMALE))
	
	def __repr__(self):
		return "%s %s" % (self.first_name, self.last_name)

class Educative(Person):
    """
    An educative in the seminar.
    """
	using_options(inheritance='multi')
	ken = ManyToOne('Ken')
	second_ken = ManyToOne('SecondKen')
	hug = ManyToOne('Hug')

class Madrich(Person):
    """
    A madrich in the seminar.
    """
	using_options(inheritance='multi')
	ken = ManyToOne('Ken')
	second_ken = ManyToOne('SecondKen')

