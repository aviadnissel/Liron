from liron.sort.constraints import RandomSoftConstraint, HardConstraint
from liron.pojos.constants import *

class VegetarianHardConstraint(HardConstraint):
    def is_valid(self, last_educative, educatives, hugs):
        if last_educative.hug != None :
            if last_educative.food == VEGETARIAN and last_educative.hug.food != VEGETARIAN:
                return False
        return True

class MadrichHardConstraint(HardConstraint):
    def is_valid(self, last_educative, educatives, hugs):
        hug = last_educative.hug
        educative_ken = last_educative.ken
        if hug != None:
            for madrich in hug.madrichim:
                if madrich.ken == educative_ken:
                    return False
        return True
            
        
class GenderRandomSoftConstraint(RandomSoftConstraint):
    def calculate_score(self, educatives, hugs):
        total_score = 0
        for hug in hugs:
            educatives_count = hug.get_educative_count()
            male_count = hug.get_male_count()
            gender_score = (male_count ** 2) * self.score
            female_count = educatives_count - male_count
            gender_score += (female_count ** 2) * self.score
            total_score += gender_score
        return total_score

class SizeRandomSoftConstraint(RandomSoftConstraint):
    def calculate_score(self, educatives, hugs):
        total_score = 0
        for hug in hugs:
            educative_count = hug.get_educative_count()
            total_score += (educative_count ** 2) * self.score
        return total_score


class KenRandomSoftConstraint(RandomSoftConstraint):
    def calculate_score(self, educatives, hugs):
        total_score = 0
        score = self.score
        for hug in hugs:
            for ken, count in hug.get_kens_count().iteritems():
                total_score += (count ** 2) * score
            for second_ken, count in hug.get_second_kens_count().iteritems():
                if second_ken != None:
                    total_score += (count ** 2) * score
        return total_score