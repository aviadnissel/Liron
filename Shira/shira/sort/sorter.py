# -*- coding: utf-8 -*-

import random
import time
from shira.pojos.persons import Educative
from shira.pojos.persons import Person
from shira.pojos.seminar import Hug, Ken

MAX_TIME = 1 #* 60 # One minute
MAX_GENDER_SCORE = 5000
MAX_SIZE_SCORE = 100000
MAX_KEN_SCORE = 1000
MAX_MAHOZ_SCORE = 500

class Sorter():
    def __init__(self, soft_constraints, hard_constraints):
        self.soft_constraints = soft_constraints
        self.hard_constraints = hard_constraints
        
    def assign_educatives_with_constant_score(self, educatives, hugs):
        for educative in educatives:
            best_hug = self.find_best_hug(educative, educatives, hugs)
            educative.hug = best_hug

    def find_best_hug(self, current_educative, educatives, hugs):
        min_score = 2 ** 100
        best_hug = None
        previous_hug = current_educative.hug
        for hug in hugs:
            current_educative.hug = hug
            is_valid = self.check_is_valid(current_educative, educatives, hugs)
            if is_valid:
                score = self.calculate_score(educatives, hugs)
                if score < min_score:
                    min_score = score
                    best_hug = hug
        current_educative.hug = previous_hug
        return best_hug
    
    def check_is_valid(self, current_educative, educatives, hugs):
        for constraint in self.hard_constraints:
            if not constraint.is_valid(current_educative, educatives, hugs):
                return False
        return True
    
    def calculate_score(self, educatives, hugs):
        score = 0
        for constraint in self.soft_constraints:
            score += constraint.calculate_score(educatives, hugs)
        return score
