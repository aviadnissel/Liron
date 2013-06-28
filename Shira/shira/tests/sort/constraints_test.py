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
    print constraint.is_valid([aviad], [hug])