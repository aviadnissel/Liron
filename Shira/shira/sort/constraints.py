import random

class HardConstraint(Object):
    def is_valid(self, educatives, hugs):
        raise NotImplementedError

class SoftConstraint(Object):
    def __init__(self, score):  
        self.score = score
    
    def calculate_score(self, educatives, hugs):
        raise NotImplementedError

class RandomSoftConstraint(SoftConstraint):
    def __init__(self, min_score, max_score):
        self.score = -1
        self.min_score = min_score
        self.max_score = max_score
        
    def calculate_random_score(self, educatives, hugs):
        self.score = random.randint(self.min_score, self.max_score)
        return self.calculate_score(self.score, educatives, hugs)
