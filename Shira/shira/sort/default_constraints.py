from shira.sort.constraints import RandomSoftConstraint

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
            ken_score = 0
            for ken, count in hug.get_kens_count().iteritems():
                ken_score += (count ** 2) * score
            for second_ken, count in hug.get_second_kens_count().iteritems():
                if second_ken != None:
                    ken_score += (count ** 2) * score
            total_score += ken_score
        return total_score