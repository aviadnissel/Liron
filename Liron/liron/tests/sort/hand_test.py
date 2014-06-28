from liron.models.constants import MALE, FEMALE, VEGETARIAN, MEAT
from liron.models.persons import Educative, Madrich
from liron.models.seminar import Ken, Seminar, Camp, Hug
from liron.sort.default_constraints import GenderRandomSoftConstraint, \
    SizeRandomSoftConstraint, KenRandomSoftConstraint, VegetarianHardConstraint, \
    MadrichHardConstraint
import liron.models  # @UnusedImport
from liron.sort.sorter import Sorter
import random
import time
import unittest




def create_soft_constraints():
    gender = GenderRandomSoftConstraint(10, 10, 10)
    size = SizeRandomSoftConstraint(100, 100, 100)
    ken = KenRandomSoftConstraint(1, 1, 1)
    return [gender, size, ken]

def create_hard_constraints():
    vegetarian = VegetarianHardConstraint()
    madrich = MadrichHardConstraint()
    return [vegetarian, madrich]
    
class SortTest():

    @classmethod
    def setUpClass(cls):
        from liron.models import session, engine, Base
        cls.session = session
        Base.metadata.create_all(engine)

    @classmethod
    def tearDown(cls):
        cls.session.rollback()

    @classmethod
    def create_small_educatives_and_seminar(cls):
        misgav = Ken()
        misgav.name = 'Misgav'
        cls.session.add(misgav)

        karmiel = Ken()
        karmiel.name = 'Karmiel'
        cls.session.add(karmiel)

        aviad = Educative()
        aviad.gender = MALE
        aviad.first_name = "Aviad"
        aviad.ken = misgav
        cls.session.add(aviad)

        naama = Educative()
        naama.gender = FEMALE
        naama.first_name = "Naama"
        naama.ken = karmiel
        cls.session.add(naama)

        inbar = Educative()
        inbar.gender = FEMALE
        inbar.first_name = "Inbar"
        inbar.ken = misgav
        cls.session.add(inbar)

        alon = Educative()
        alon.gender = MALE
        alon.first_name = "Alon"
        alon.ken = karmiel
        cls.session.add(alon)

        seminar = Seminar()
        cls.session.add(seminar)

        camp = Camp()
        camp.seminar = seminar
        cls.session.add(camp)

        hug1 = Hug()
        hug1.name = "Hug1"
        hug1.camp = camp
        cls.session.add(hug1)

        hug2 = Hug()
        hug2.name = "Hug2"
        hug2.camp = camp
        cls.session.add(hug2)

        return [aviad, naama, inbar, alon], seminar

    @classmethod
    def create_large_educatives_and_seminar(cls):
        NUMBER_OF_KENS = 5
        NUMBER_OF_EDUCATIVES = 90
        NUMBER_OF_HUGS = 5
        NUMBER_OF_VEGETARIAN_HUGS = 2

        kens = []
        for i in xrange(NUMBER_OF_KENS):
            ken = Ken()
            ken.name = "Ken " + str(i)
            kens.append(ken)
            cls.session.add(ken)

        educatives = []
        for i in xrange(NUMBER_OF_EDUCATIVES):
            educative = Educative()
            if random.randint(0, 2) == 0:
                educative.gender = MALE
            else:
                educative.gender = FEMALE
            if random.randint(0, 9) == 0:
                educative.food = VEGETARIAN
            else:
                educative.food = MEAT
            educative.first_name = "Educative"
            educative.last_name = str(i)
            educative.ken = kens[random.randint(0, NUMBER_OF_KENS - 1)]
            educatives.append(educative)
            cls.session.add(educative)

        seminar = Seminar()
        seminar.name = 'Seminar'
        cls.session.add(seminar)

        camp1, camp2, camp3 = Camp(), Camp(), Camp()
        camp1.name = 'Camp 1'
        camp2.name = 'Camp 2'
        camp3.name = 'Camp3'
        seminar.camps += [camp1, camp2, camp3]
        [cls.session.add(c) for c in seminar.camps]

        hugs = []
        for i in xrange(NUMBER_OF_HUGS):
            hug = Hug()
            hug.name = "Hug " + str(i)
            hug.camp = seminar.camps[i % 3]
            if i < NUMBER_OF_VEGETARIAN_HUGS:
                hug.food = VEGETARIAN
            hugs.append(hug)
            cls.session.add(hug)
            for j in xrange(random.randint(1, 2)):
                madrich = Madrich()
                madrich.first_name = "Madrich"
                madrich.last_name = str(j)
                madrich.ken = kens[random.randint(0, NUMBER_OF_KENS - 1)]
                hug.madrichim.append(madrich)
                cls.session.add(madrich)

        return educatives, seminar

    def test_sanity(self):
        educatives, seminar = self.create_small_educatives_and_seminar()
        hard_constraints = create_hard_constraints()
        soft_constraints = create_soft_constraints()
        Sorter(soft_constraints, hard_constraints).assign_educatives_with_constant_score(educatives, seminar)
        print "Sanity check:"
        print seminar.camps[0].hugs[0].educatives
        print seminar.camps[0].hugs[1].educatives
        assert(educatives[0].hug != educatives[1].hug)
        assert(educatives[2].hug != educatives[3].hug)
        assert(len(seminar.camps[0].hugs[0].educatives) == len(seminar.camps[0].hugs[1].educatives))
    
    def test_stress(self):
        educatives, seminar = self.create_large_educatives_and_seminar()
        hard_constraints = create_hard_constraints()
        soft_constraints = create_soft_constraints()
        print "Started stress test at " + time.ctime()
        self.session.flush()
        Sorter(soft_constraints, hard_constraints).assign_educatives_with_constant_score(educatives, seminar)
        print "Ended stress test at " + time.ctime()
        return educatives, seminar

if __name__ == '__main__':
    t = SortTest()
    t.setUpClass()
    t.test_stress()
    t.tearDown()