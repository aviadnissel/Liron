from liron.pojos.model import *
from liron.sort.sorter import *
from liron.pojos.constants import *
from liron.sort.default_constraints import *

def create_small_educatives_and_seminar():
    misgav = Ken()
    misgav.name = 'Misgav'
    
    karmiel = Ken()
    karmiel.name = 'Karmiel'
    
    aviad = Educative()
    aviad.gender = MALE
    aviad.first_name = "Aviad"
    aviad.ken = misgav
	
    naama = Educative()
    naama.gender = FEMALE
    naama.first_name = "Naama"
    naama.ken = karmiel
	
    inbar = Educative()
    inbar.gender = FEMALE
    inbar.first_name = "Inbar"
    inbar.ken = misgav
	
    alon = Educative()
    alon.gender = MALE
    alon.first_name = "Alon"
    alon.ken = karmiel
	
    seminar = Seminar()
    camp = Camp()
    camp.seminar = seminar
    
    hug1 = Hug()
    hug1.name = "Hug1"
    hug1.camp = camp
    hug2 = Hug()
    hug2.name = "Hug2"
    hug2.camp = camp
	
    return [aviad, naama, inbar, alon], seminar
    
def create_large_educatives_and_seminar():
    import random
    NUMBER_OF_KENS = 50
    NUMBER_OF_EDUCATIVES = 900
    NUMBER_OF_HUGS = 45
    NUMBER_OF_VEGETARIAN_HUGS = 8
    
    kens = []
    for i in xrange(NUMBER_OF_KENS):
        ken = Ken()
        ken.name = "Ken " + str(i)
        kens.append(ken)
        
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
    
    seminar = Seminar()
    seminar.name = 'Seminar'
    
    camp1, camp2, camp3 = Camp(), Camp(), Camp()
    camp1.name = 'Camp 1'
    camp2.name = 'Camp 2'
    camp3.name = 'Camp3'
    seminar.camps += [camp1, camp2, camp3]
    
    hugs = []
    for i in xrange(NUMBER_OF_HUGS):
        hug = Hug()
        hug.name = "Hug " + str(i)
        hug.camp = seminar.camps[i % 3]
        if i < NUMBER_OF_VEGETARIAN_HUGS:
            hug.food = VEGETARIAN
        hugs.append(hug)
        for j in xrange(random.randint(1, 2)):
            madrich = Madrich()
            madrich.first_name = "Madrich"
            madrich.last_name = str(j)
            madrich.ken = kens[random.randint(0, NUMBER_OF_KENS - 1)]
            hug.madrichim.append(madrich)
    
    return educatives, seminar
    
def create_soft_constraints():
    gender = GenderRandomSoftConstraint(10, 10, 10)
    size = SizeRandomSoftConstraint(100, 100, 100)
    ken = KenRandomSoftConstraint(1, 1, 1)
    return [gender, size, ken]

def create_hard_constraints():
    vegetarian = VegetarianHardConstraint()
    madrich = MadrichHardConstraint()
    return [vegetarian, madrich]
    
def sanity_check():
    educatives, seminar = create_small_educatives_and_seminar()
    hard_constraints = create_hard_constraints()
    soft_constraints = create_soft_constraints()
    Sorter(soft_constraints, hard_constraints).assign_educatives_with_constant_score(educatives, seminar)
    print "Sanity check:"
    print seminar.camps[0].hugs[0].educatives
    print seminar.camps[0].hugs[1].educatives
    assert(educatives[0].hug != educatives[1].hug)
    assert(educatives[2].hug != educatives[3].hug)
    assert(len(seminar.camps[0].hugs[0].educatives) == len(seminar.camps[0].hugs[1].educatives))

def stress_test():
    import time
    educatives, seminar = create_large_educatives_and_seminar()
    hard_constraints = create_hard_constraints()
    soft_constraints = create_soft_constraints()
    print "Started stress test at " + time.ctime()
    Sorter(soft_constraints, hard_constraints).assign_educatives_with_constant_score(educatives, seminar)
    print "Ended stress test at " + time.ctime()
    return educatives, seminar