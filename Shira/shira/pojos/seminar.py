# -*- coding: utf-8 -*- 

from elixir import Entity, Field, Unicode, OneToMany, using_options

class Hug(Entity):
	name = Field(Unicode(60))
	educatives = OneToMany('Educative')
		
	def get_male_count(self):
		from shira.pojos.persons import Person
		male_count = 0
		for educative in self.educatives:
			if educative.gender == Person.MALE:
				male_count += 1
		return male_count
		
	def get_educative_count(self):
		return len(self.educatives)
	
	def get_kens_count(self):
		kens_count = {}
		for educative in self.educatives:
			ken = educative.ken
			if kens_count.has_key(ken):
				kens_count[ken] = kens_count[ken] + 1
			else:
				kens_count[ken] = 1
		return kens_count
		
	def get_second_kens_count(self):
		kens_count = {}
		for educative in self.educatives:
			ken = educative.second_ken
			if kens_count.has_key(ken):
				kens_count[ken] = kens_count[ken] + 1
			else:
				kens_count[ken] = 1
		return kens_count
		

class AbstractKen(Entity):
	using_options(inheritance='multi')
	name = Field(Unicode(40))
	
	def __repr__(self):
		return str(self.name)

class Ken(AbstractKen):
	using_options(inheritance='multi')
	educatives = OneToMany('Educative')
	madrichim = OneToMany('Madrich')

class SecondKen(AbstractKen):
	using_options(inheritance='multi')
	educatives = OneToMany('Educative')
	madrichim = OneToMany('Madrich')