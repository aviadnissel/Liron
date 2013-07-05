# -*- coding: utf-8 -*-

import random
import time
from liron.pojos.persons import Educative
from liron.pojos.persons import Person
from liron.pojos.seminar import *

MAX_TIME = 1 #* 60 # One minute
MAX_GENDER_SCORE = 5000
MAX_SIZE_SCORE = 100000
MAX_KEN_SCORE = 1000
MAX_MAHOZ_SCORE = 500

class Sorter():
    def __init__(self, soft_constraints, hard_constraints):
        self.soft_constraints = soft_constraints
        self.hard_constraints = hard_constraints
        
    def assign_educatives_with_constant_score(self, educatives, seminar):
        for educative in educatives:
            best_hug = self.find_best_hug(educative, educatives, seminar)
            educative.hug = best_hug

    def find_best_hug(self, current_educative, educatives, seminar):
        min_score = 2 ** 100
        best_hug = None
        previous_hug = current_educative.hug
        for camp in seminar.camps:
            for hug in camp.hugs:
                current_educative.hug = hug
                is_valid = self.check_is_valid(current_educative, educatives, seminar)
                if is_valid:
                    score = self.calculate_score(educatives, seminar)
                    if score < min_score:
                        min_score = score
                        best_hug = hug
        current_educative.hug = previous_hug
        return best_hug
    
    def check_is_valid(self, current_educative, educatives, seminar):
        hugs = []
        for camp in seminar.camps:
            hugs += camp.hugs
        for constraint in self.hard_constraints:
            if not constraint.is_valid(current_educative, educatives, hugs):
                return False
        return True
    
    def calculate_score(self, educatives, seminar):
        hugs = []
        for camp in seminar.camps:
            hugs += camp.hugs
        score = 0
        for constraint in self.soft_constraints:
            score += constraint.calculate_score(educatives, hugs)
        return score
