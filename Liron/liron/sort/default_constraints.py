from liron.sort.constraints import RandomSoftConstraint, HardConstraint
from liron.models.constants import *
from liron.models import session
from liron.models.persons import Educative
from sqlalchemy.sql.expression import func

class VegetarianHardConstraint(HardConstraint):
    def is_valid(self, last_educative, educatives, seminar):
        if last_educative.hug != None :
            if last_educative.food == VEGETARIAN and last_educative.hug.food != VEGETARIAN:
                return False
        return True

class MadrichHardConstraint(HardConstraint):
    def is_valid(self, last_educative, educatives, seminar):
        hug = last_educative.hug
        educative_ken = last_educative.ken
        if hug != None:
            for madrich in hug.madrichim:
                if madrich.ken == educative_ken:
                    return False
        return True


class GenderRandomSoftConstraint(RandomSoftConstraint):
    def calculate_score(self, educatives, seminar):
        total_score = 0
        for camp in seminar.camps:
            for hug in camp.hugs:
                educatives_count = session.query(Educative).filter(Educative.hug == hug).count()
                male_count = session.query(Educative).filter(Educative.hug ==
                            hug).filter(Educative.gender == MALE).count()
                gender_score = (male_count ** 2) * self.score
                female_count = educatives_count - male_count
                gender_score += (female_count ** 2) * self.score
                total_score += gender_score
        return total_score

class SizeRandomSoftConstraint(RandomSoftConstraint):
    def calculate_score(self, educatives, seminar):
        total_score = 0
        for camp in seminar.camps:
            for hug in camp.hugs:
                educatives_count = session.query(Educative).filter(Educative.hug == hug).count()
                total_score += (educatives_count ** 2) * self.score
        return total_score


class KenRandomSoftConstraint(RandomSoftConstraint):
    def calculate_score(self, educatives, seminar):
        total_score = 0
        score = self.score
        for camp in seminar.camps:
            for hug in camp.hugs:
                kens_count = session.query(Educative.ken_id, func.count(Educative.ken_id)).filter(Educative.hug_id == hug.id).group_by(Educative.ken_id).all()
                for ken in kens_count:
                    count = ken[1]
                    total_score += (count ** 2) * score
                second_kens_count = session.query(Educative.second_ken_id, func.count(Educative.second_ken_id)).filter(Educative.hug_id == hug.id).group_by(Educative.second_ken_id).all()
                for second_ken in second_kens_count:
                    if second_ken is not None:
                        total_score += (second_ken[1] ** 2) * score
        return total_score