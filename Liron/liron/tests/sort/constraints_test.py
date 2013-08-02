import liron.pojos.model # @UnusedImport
from liron.pojos.constants import VEGETARIAN, MEAT, MALE, FEMALE
from liron.pojos.persons import Educative, Madrich
from liron.pojos.seminar import Seminar, Camp, Hug, Ken, SecondKen
from liron.sort.default_constraints import VegetarianHardConstraint, \
    MadrichHardConstraint, GenderRandomSoftConstraint, SizeRandomSoftConstraint, \
    KenRandomSoftConstraint
import unittest

def create_seminar(num_of_camps, num_of_hugs):
    seminar = Seminar()
    seminar.name = 'Seminar'
    for i in xrange(num_of_camps):
        camp = Camp()
        camp.name = 'Camp ' + str(i)
        camp.seminar = seminar
    
    for i in xrange(num_of_hugs):
        hug = Hug()
        hug.name = 'Hug ' + str(i)
        hug.camp = seminar.camps[i % num_of_camps]
        
    return seminar

class TestConstraints(unittest.TestCase):

    def test_vegetarian(self):
        aviad = Educative()
        aviad.first_name = 'Aviad'
        aviad.food = VEGETARIAN
        
        seminar = create_seminar(1, 1)
        hug = seminar.camps[0].hugs[0]
        hug.food = MEAT
        aviad.hug = hug
        
        constraint = VegetarianHardConstraint()
        self.assertTrue(not constraint.is_valid(aviad, [aviad], [hug]))

    def test_madrich(self):
        ken = Ken()
        ken.name = 'Misgav'
        
        seminar = create_seminar(1, 1)
        hug = seminar.camps[0].hugs[0]

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
        self.assertTrue(not constraint.is_valid(aviad, [aviad], seminar))

    def test_gender_constant(self):
        constraint = GenderRandomSoftConstraint(10, 10, 10)
        
        seminar = create_seminar(1, 2)
        hugs = seminar.camps[0].hugs
        
        educative1 = Educative()
        educative1.gender = MALE
        educative1.hug = hugs[0]
        
        educative2 = Educative()
        educative2.gender = FEMALE
        educative2.hug = hugs[0]
        
        educative3 = Educative()
        educative3.gender = FEMALE
        educative3.hug = hugs[1]
        
        score = constraint.calculate_score([educative1, educative2, educative3], seminar)
        self.assertEquals(score, 30)

    def test_size_constant(self):
        constraint = SizeRandomSoftConstraint(10, 10, 10)
        
        seminar = create_seminar(1, 2)
        hugs = seminar.camps[0].hugs
        
        educative1 = Educative()
        educative1.hug = hugs[0]
        
        educative2 = Educative()
        educative2.hug = hugs[0]
        
        educative3 = Educative()
        educative3.hug = hugs[1]
        
        score = constraint.calculate_score([educative1, educative2, educative3], seminar)
        self.assertEquals(score, 50)

    def test_ken_constant(self):
        constraint = KenRandomSoftConstraint(10, 10, 10)
        
        seminar = create_seminar(1, 2)
        hugs = seminar.camps[0].hugs
        
        ken1 = Ken()
        ken2 = Ken()
        second_ken = SecondKen()
        
        educative1 = Educative()
        educative1.ken = ken1
        educative1.hug = hugs[0]
        
        educative2 = Educative()
        educative2.ken = ken1
        educative2.hug = hugs[0]
        
        educative3 = Educative()
        educative3.ken = ken1
        educative3.hug = hugs[1]
        
        educative4 = Educative()
        educative4.ken = ken2
        educative4.second_ken = second_ken
        educative4.hug = hugs[1]
        
        score = constraint.calculate_score([educative1, educative2, educative3, educative4], seminar)
        self.assertEquals(score, 70)

if __name__ == '__main__':
    unittest.main()