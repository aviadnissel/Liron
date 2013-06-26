# -*- coding: utf-8 -*-

import random
import time
import math
from shira.pojos.persons import Educative
from shira.pojos.persons import Person
from shira.pojos.seminar import Hug, Ken

MAX_TIME = 1 #* 60 # One minute
MAX_GENDER_SCORE = 5000
MAX_SIZE_SCORE = 100000
MAX_KEN_SCORE = 1000
MAX_MAHOZ_SCORE = 500

class Scorer():
    def __init__(self, gender_score, size_score, ken_score, mahoz_score):
        self.gender_score = gender_score
        self.size_score = size_score
        self.ken_score = ken_score
        self.mahoz_score = mahoz_score
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        string = "מנקד\n"
        string += "ניקוד מין:" + str(self.gender_score) + "\n"
        string += "ניקוד גודל:" + str(self.size_score) + "\n"
        string += "ניקוד קן:" + str(self.ken_score) + "\n"
        string += "ניקוד מחוז:" + str(self.mahoz_score) + "\n"
        return string

    def calculate_standard_deviation(self, values):
        n = float(len(values))
        average = sum(values) / n
        varience = sum([(x - average) ** 2 for x in values]) / n
        deviation = math.sqrt(varience)
        return deviation
    
    def calculate_deviations(self, hugs):
        pass
    
    def calculate_score(self, hugs):
        total_score = 0
        for hug in hugs:
            educatives_count = hug.get_educative_count()
            gender_score = (hug.get_male_count() ** 2) * self.gender_score
            gender_score += ((educatives_count - hug.get_male_count()) ** 2) * self.gender_score
            total_score += gender_score
            size_score = (educatives_count ** 2) * self.size_score
            total_score += size_score
            ken_score = 0
            for ken, count in hug.get_kens_count().items():
                ken_score += (count ** 2) * self.ken_score
            for second_ken, count in hug.get_second_kens_count().items():
                if second_ken != None:
                    ken_score += (count ** 2) * self.ken_score
            total_score += ken_score
        return total_score

class Sorter():
    
    def create_random_scorer(self):
        gender_score = random.randint(MAX_GENDER_SCORE / 100, MAX_GENDER_SCORE)
        size_score = random.randint(MAX_SIZE_SCORE / 100, MAX_SIZE_SCORE)
        ken_score = random.randint(MAX_KEN_SCORE / 100, MAX_KEN_SCORE)
        mahoz_score = random.randint(MAX_MAHOZ_SCORE / 100, MAX_MAHOZ_SCORE)
        return Scorer(gender_score, size_score, ken_score, mahoz_score)

    def weighted_choice(self, hugs):
       total = sum(w for c, w in hugs)
       r = random.uniform(0, total)
       upto = 0
       for c, w in hugs:
          if upto + w > r:
             return c
          upto += w
       assert False, "Shouldn't get here"

    def get_best_hug(self, educative, hugs, scorer):
        min_score = 2 ** 100
        best_hug = None
        previous_hug = educative.hug
        for hug in hugs:
            educative.hug = hug
            score = scorer.calculate_score(hugs)
            educative.hug = previous_hug
            if score < min_score:
                min_score = score
                best_hug = hug
        return best_hug

    def assign_educatives_constant_score(self, educatives, hugs, scorer):
        for educative in educatives:
            best_hug = self.get_best_hug(educative, hugs, scorer)
            educative.hug = best_hug
            
    def assign_educatives_random_score(self, educatives, hugs):
        iterations = 0
        min_score = 2 ** 100
        min_scorer = None
        start_time = time.time()
        scorer = self.create_random_scorer()
        #while time.time() - start_time < MAX_TIME:
        while iterations == 0:
            iterations += 1
            self.assign_educatives_constant_score(educatives, hugs, scorer)
            score = scorer.calculate_score(hugs)
            if score < min_score:
                min_score = score
                min_scorer = scorer
        self.assign_educatives_constant_score(educatives, hugs, min_scorer)
        
