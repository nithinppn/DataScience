import unittest
from math_quiz import AssignNumbers, AssignOperator, MathQuestion


class TestMathGame(unittest.TestCase):

    def test_AssignNumbers(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = AssignNumbers(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_AssignOperator(self):
        # TODO
        pass

    def test_MathQuestion(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 6, '-', '8 - 6', 2),
                (7, 3, '*', '7 * 3', 21)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                pass

if __name__ == "__main__":
    unittest.main()
