import unittest
from bmi import get_user_stats, calc_user_bmi, user_birth_year

class testUserStats(unittest.TestCase):

    def test_get_user_stats(self):
        age = 24
        height = 173
        weight = 60
        result = get_user_stats(age, height, weight)
        self.assertEqual(result, [24, 173, 60])

    def test_user_bmi(self):
        height = 167
        weight = 50
        result = calc_user_bmi(height, weight)
        self.assertEqual(result, 17)

    def test_user_birth_year(self):
        age = 26
        result = user_birth_year(age)
        self.assertEqual(result, 1992)
    
