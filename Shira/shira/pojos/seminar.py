# -*- coding: utf-8 -*- 

from elixir import Entity, Field, Unicode, OneToMany, using_options

class Hug(Entity):
    """
    A hug in the seminar.
    """
    name = Field(Unicode(60))
    educatives = OneToMany('Educative')
    
    def __init__(self):
        self.kens_count = {}
        self.second_kens_count = {}
        self.male_count = 0
    
    def update_count(self, educative, is_removed = False):
        from shira.pojos.persons import Person
        ken = educative.ken
        second_ken = educative.second_ken
        gender = educative.gender
        
        if is_removed:
            if gender == Person.MALE:
                self.male_count -= 1
            self.kens_count[ken] = self.kens_count[ken] - 1
            if self.kens_count[ken] == 0:
                del self.kens_count[ken]
            self.second_kens_count[second_ken] = self.second_kens_count[second_ken] - 1
            if self.second_kens_count[second_ken] == 0:
                del self.second_kens_count[second_ken]
        else:
            if gender == Person.MALE:
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
        return len(self.educatives)
    
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