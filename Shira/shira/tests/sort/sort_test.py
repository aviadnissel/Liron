from shira.pojos.model import *
from shira.sort.sorter import *
from shira.pojos.constants import *

def create_small_educatives_and_hugs():
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
	
    hug1 = Hug()
    hug1.name = "Hug1"
    hug2 = Hug()
    hug2.name = "Hug2"
	
    return [aviad, naama, inbar, alon], [hug1, hug2]

def create_large_educatives_and_hugs():
    import random
    NUMBER_OF_KENS = 50
    NUMBER_OF_EDUCATIVES = 900
    NUMBER_OF_HUGS = 45
    kens = []
    for i in xrange(NUMBER_OF_KENS):
        ken = Ken()
        ken.name = "Ken " + str(i)
        kens.append(ken)
        
    educatives = []
    for i in xrange(NUMBER_OF_EDUCATIVES):
        educative = Educative()
        if random.randint(0, 1) == 0:
            educative.gender = MALE
        else:
            educative.gender = FEMALE
        educative.first_name = "educative"
        educative.last_name = str(i)
        educative.ken = kens[random.randint(0, NUMBER_OF_KENS - 1)]
        educatives.append(educative)
    
    hugs = []
    for i in xrange(NUMBER_OF_HUGS):
        hug = Hug()
        hug.name = "Hug " + str(i)
        hugs.append(hug)
    
    return educatives, hugs
    
def create_soft_constraints():
    from shira.sort.default_constraints import *
    gender = GenderRandomSoftConstraint(10, 10, 10)
    size = SizeRandomSoftConstraint(100, 100, 100)
    ken = KenRandomSoftConstraint(1, 1, 1)
    return [gender, size, ken]
    
def sanity_check():
    educatives, hugs = create_small_educatives_and_hugs()
    hard_constraints = []
    soft_constraints = create_soft_constraints()
    Sorter(soft_constraints, hard_constraints).assign_educatives_with_constant_score(educatives, hugs)
    print "Sanity check:"
    print hugs[0].educatives
    print hugs[1].educatives
    assert(educatives[0].hug != educatives[1].hug)
    assert(educatives[2].hug != educatives[3].hug)
    assert(len(hugs[0].educatives) == len(hugs[1].educatives))

def stress_test():
    import time
    educatives, hugs = create_large_educatives_and_hugs()
    hard_constraints = []
    soft_constraints = create_soft_constraints()
    print "Started stress test at " + time.ctime()
    Sorter(soft_constraints, hard_constraints).assign_educatives_with_constant_score(educatives, hugs)
    print "Ended stress test at " + time.ctime()