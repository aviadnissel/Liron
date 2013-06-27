# -*- coding: utf-8 -*- 

from elixir import Entity, Field, Unicode, OneToMany, using_options

class Hug(Entity):
    """
    A hug in the seminar.
    """
    name = Field(Unicode(60))
    educatives = OneToMany('Educative')
        
    def get_male_count(self):
        """
        Counts and returns the number of male educatives in the hug.
        """
        from shira.pojos.persons import Person
        male_count = 0
        for educative in self.educatives:
            if educative.gender == Person.MALE:
                male_count += 1
        return male_count
        
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
        kens_count = {}
        for educative in self.educatives:
            ken = educative.ken
            if kens_count.has_key(ken):
                kens_count[ken] = kens_count[ken] + 1
            else:
                kens_count[ken] = 1
        return kens_count
        
    def get_second_kens_count(self):
        """
        Counts the number of educatives in each second ken, in the hug.
        Returns a dictionary between the second ken and the number of educatives.
        """
        kens_count = {}
        for educative in self.educatives:
            ken = educative.second_ken
            if kens_count.has_key(ken):
                kens_count[ken] = kens_count[ken] + 1
            else:
                kens_count[ken] = 1
        return kens_count
        

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