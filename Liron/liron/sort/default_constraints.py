from liron.sort.constraints import RandomSoftConstraint, HardConstraint
from liron.models.constants import *
from liron.models import session
from liron.models.persons import Educative
from sqlalchemy.sql.expression import func

class VegetarianHardConstraint(HardConstraint):
    def is_valid(self, last_educative, educatives, seminar):
        if last_educative.hug is not None :
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
        gender_count = session.query(Educative.hug_id, Educative.gender, func.count(Educative.gender)).group_by(Educative.hug_id, Educative.gender).all()
        for hug_gender in gender_count:
            count = hug_gender[2]
            total_score += (count ** 2) * self.score
        return total_score

class SizeRandomSoftConstraint(RandomSoftConstraint):
    def calculate_score(self, educatives, seminar):
        total_score = 0
        size_count = session.query(Educative.hug_id, func.count(Educative.hug_id)).group_by(Educative.hug_id).all()
        for size in size_count:
            total_score += (size[1] ** 2) * self.score
        return total_score


class KenRandomSoftConstraint(RandomSoftConstraint):
    def calculate_score(self, educatives, seminar):
        total_score = 0
        score = self.score
        ken_count = session.query(Educative.hug_id, Educative.ken_id, func.count(Educative.ken_id)).group_by(Educative.hug_id, Educative.ken_id).all()
        print ken_count
        for ken in ken_count:
            total_score += (ken[2] ** 2) * score
        second_ken_count = session.query(Educative.hug_id, Educative.second_ken_id, func.count(Educative.second_ken_id)).group_by(Educative.hug_id, Educative.second_ken_id).all()
        print second_ken_count
        for second_ken in second_ken_count:
            total_score += (second_ken[2] ** 2) * score
        return total_score