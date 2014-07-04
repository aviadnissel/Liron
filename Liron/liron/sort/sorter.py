# -*- coding: utf-8 -*-

import random
HUGS_CHOICE_PERC = 0.5
MIN_CHOICE_HUGS = 3

class Sorter():
    def __init__(self, soft_constraints, hard_constraints):
        self.soft_constraints = soft_constraints
        self.hard_constraints = hard_constraints
        
    def assign_educatives_with_constant_score(self, educatives, seminar):
        for educative in educatives:
            print "Assigning educative", educative
            best_hug = self.find_best_hug(educative, educatives, seminar)
            educative.hug = best_hug

    def find_best_hug(self, current_educative, educatives, seminar):
        min_score = 2 ** 100
        best_hug = None
        previous_hug = current_educative.hug
        hugs = []
        for camp in seminar.camps:
            hugs += camp.hugs
        chosen_hugs = ()
        hugs_to_choose = int(max(len(hugs) * HUGS_CHOICE_PERC, MIN_CHOICE_HUGS))
        for i in xrange(hugs_to_choose):
            if len(hugs) > 0:
                chosen_hug = random.choice(hugs)
                chosen_hugs += (chosen_hug,)
                hugs.remove(chosen_hug)
        for hug in chosen_hugs:
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
        for constraint in self.hard_constraints:
            if not constraint.is_valid(current_educative, educatives, seminar):
                return False
        return True
    
    def calculate_score(self, educatives, seminar):
        score = 0
        for constraint in self.soft_constraints:
            score += constraint.calculate_score(educatives, seminar)
        return score
