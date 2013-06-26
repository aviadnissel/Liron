from shira.pojos.model import *
from shira.sort.sorter import *

def create_educatives_and_hugs():
    misgav = Ken()
    misgav.name = 'Misgav'
    karmiel = Ken()
    karmiel.name = 'Karmiel'
	
    aviad = Educative()
    aviad.gender = Person.MALE
    aviad.first_name = "Aviad"
    aviad.ken = misgav
	
    naama = Educative()
    naama.gender = Person.FEMALE
    naama.first_name = "Naama"
    naama.ken = karmiel
	
    inbar = Educative()
    inbar.gender = Person.FEMALE
    inbar.first_name = "Inbar"
    inbar.ken = misgav
	
    alon = Educative()
    alon.gender = Person.MALE
    alon.first_name = "Alon"
    alon.ken = karmiel
	
    hug1 = Hug()
    hug1.first_name = "Hug1"
    hug2 = Hug()
    hug2.first_name = "Hug2"
	
    return [aviad, naama, inbar, alon], [hug1, hug2]

def sanity_check():
	educatives, hugs = create_educatives_and_hugs()
	scorer = Scorer(gender_score = 10, size_score = 100, ken_score = 1, mahoz_score = 2)
	Sorter().assign_educatives_constant_score(educatives, hugs, scorer)
	print hugs[0].educatives
	print hugs[1].educatives
	assert(educatives[0].hug != educatives[1].hug)
	assert(educatives[2].hug != educatives[3].hug)
	assert(len(hugs[0].educatives) == len(hugs[1].educatives))
