# -*- coding: utf-8 -*- 

from elixir import Entity, Field, Unicode, OneToMany, ManyToOne, using_options, Enum
from liron.pojos.constants import *

class Seminar(Entity):
    name = Field(Unicode(60))
    camps = OneToMany('Camp', lazy=False)

class Camp(Entity):
    name = Field(Unicode(60))
    hugs = OneToMany('Hug', lazy=False)
    seminar = ManyToOne('Seminar', lazy=False)
    
class Hug(Entity):
    """
    A hug in the seminar.
    """

    name = Field(Unicode(60))
    educatives = OneToMany('Educative', lazy=False)
    madrichim = OneToMany('Madrich', lazy=False)
    camp = ManyToOne('Camp', lazy=False)
    food = Field(Enum(MEAT, VEGETARIAN))
    
    def __init__(self):
        self.kens_count = {}
        self.second_kens_count = {}
        self.male_count = 0
        self.educatives_count = 0
    
    def __repr__(self):
        return self.name
        
    def update_count(self, educative, is_removed = False):
        ken = educative.ken
        second_ken = educative.second_ken
        gender = educative.gender
        
        if is_removed:
            self.educatives_count -= 1
            if gender == MALE:
                self.male_count -= 1
            self.kens_count[ken] = self.kens_count[ken] - 1
            if self.kens_count[ken] == 0:
                del self.kens_count[ken]
            self.second_kens_count[second_ken] = self.second_kens_count[second_ken] - 1
            if self.second_kens_count[second_ken] == 0:
                del self.second_kens_count[second_ken]
        else:
            self.educatives_count += 1
            if gender == MALE:
                self.male_count += 1
            if ken in self.kens_count:
                self.kens_count[ken] = self.kens_count[ken] + 1
            else:
                self.kens_count[ken] = 1
            if second_ken in self.second_kens_count:
                self.second_kens_count[second_ken] = self.second_kens_count[second_ken] + 1
            else:
                self.second_kens_count[second_ken] = 1
            
        
    def get_male_count(self):
        """
        Counts and returns the number of male educatives in the hug.
        """
        return self.male_count
        
    def get_educative_count(self):
        """
        Returns the number of educatives in the hug
        """
        return self.educatives_count
    
    def get_kens_count(self):
        """
        Counts the number of educatives in each ken, in the hug.
        Returns a dictionary between the ken and the number of educatives.
        """
        return self.kens_count
        
    def get_second_kens_count(self):
        """
        Counts the number of educatives in each second ken, in the hug.
        Returns a dictionary between the second ken and the number of educatives.
        """
        return self.second_kens_count
        

class AbstractKen(Entity):
    """
    An abstract ken class.
    Both ken and second ken inherit from it.
    """
    using_options(inheritance='multi')
    name = Field(Unicode(40))
    
    def __repr__(self):
        return str(self.name)

class Ken(AbstractKen):
    """
    A ken in the seminar.
    """
    using_options(inheritance='multi')
    educatives = OneToMany('Educative')
    madrichim = OneToMany('Madrich')

class SecondKen(AbstractKen):
    """
    A second ken in the seminar.
    """
    using_options(inheritance='multi')
    educatives = OneToMany('Educative')
    madrichim = OneToMany('Madrich')