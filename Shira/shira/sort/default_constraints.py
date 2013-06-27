from shira.sort.constraints import RandomSoftConstraint

class GenderRandomSoftConstraint(RandomSoftConstraint):
    def calculate_score(self, educatives, hugs):
        total_score = 0
        for hug in hugs:
            educatives_count = hug.get_educative_count()
            gender_score = (hug.get_male_count() ** 2) * self.score
            gender_score += ((educatives_count - hug.get_male_count()) ** 2) * self.score
            total_score += gender_score
        return total_score

class SizeRandomSoftConstraint(RandomSoftConstraint):
    def calculate_score(self, educatives, hugs):
        total_score = 0
        for hug in hugs:
            total_score += (hug.get_educative_count() ** 2) * self.score
        return total_score


class KenRandomSoftConstraint(RandomSoftConstraint):
    def calculate_score(self, educatives, hugs):
        total_score = 0
        for hug in hugs:
            ken_score = 0
            for ken, count in hug.get_kens_count().items():
                ken_score += (count ** 2) * self.score
            for second_ken, count in hug.get_second_kens_count().items():
                if second_ken != None:
                    ken_score += (count ** 2) * self.score
            total_score += ken_score
        return total_score