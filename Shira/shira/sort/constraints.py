import random

class HardConstraint(Object):
    """
    A hard constraint is a boolean constraint - either it is valid, or not.
    An abstract class. Each hard constraint should inherit from it.
    """
    def is_valid(self, educatives, hugs):
        """
        Decides, based on the given educatives and hugs, if they are valid.
        Should be implemented by the inheriting class.
        """
        raise NotImplementedError

class SoftConstraint(Object):
    """
    A soft constraint is a constraint which returns a value - the higher the value, the worse it is.
    An abstract class. Each soft constraint should inherit from it.
    """
    def __init__(self, score):  
        self.score = score
    
    def calculate_score(self, educatives, hugs):
        raise NotImplementedError

class RandomSoftConstraint(SoftConstraint):
    """
    A soft constraint that allows random score in a certain range.
    """
    def __init__(self, constant_score, min_score, max_score):
        self.score = constant_score
        self.constant_score = constant_score
        self.min_score = min_score
        self.max_score = max_score
    
    def reset_score(self):
        self.score = self.constant_score
        
    def calculate_random_score(self, educatives, hugs):
        self.score = random.randint(self.min_score, self.max_score)
        return self.calculate_score(self.score, educatives, hugs)
