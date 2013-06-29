from shira.pojos.model import *
from shira.pojos.constants import *
from shira.sort.default_constraints import *

def vegetarian_test():
    aviad = Educative()
    aviad.first_name = 'Aviad'
    aviad.food = VEGETARIAN
    
    hug = Hug()
    hug.food = MEAT
    aviad.hug = hug
    
    constraint = VegetarianHardConstraint()
    assert(not constraint.is_valid(aviad, [aviad], [hug]))

def madrich_test():
    ken = Ken()
    ken.name = 'Misgav'
    
    hug = Hug()
    hug.name = 'Nice Hug'
    
    aviad = Educative()
    aviad.first_name = 'Aviad'
    aviad.ken = ken
    aviad.hug = hug
    
    madrich = Madrich()
    madrich.first_name = 'Cool'
    madrich.last_name = 'Guy'
    madrich.ken = ken
    madrich.hug = hug
    
    constraint = MadrichHardConstraint()
    assert(not constraint.is_valid(aviad, [aviad], [hug]))
    
    