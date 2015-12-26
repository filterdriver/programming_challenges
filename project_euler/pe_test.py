import logging
import sys
import math
import unittest
import pe_lib


log = logging.getLogger(__name__)


class ProjectEulerTest(unittest.TestCase):

    def setUp(self):
        self.mm = pe_lib.ProjectEuler()

    def tearDown(self):
        pass

    def test_problem_1(self):
        input = 1000
        log.info("Problem1: Lets sum the multiples of 3 and 5 below : " + str(input))
        output = self.mm.sum_of_multiples(input)
        log.info("Problem1: Sum of multiples of 3 and 5 below : " + str(input) + " is : " + str(output))
    def test_problem_2(self):
        input = 4000000
        log.info("Problem2: Lets sum the even fibonacci numbers not greater than : " + str(input))
        output = self.mm.sum_of_even_fibonacci(input)
        log.info("Problem2: Sum of even fibonacci numbers not greater than : " + str(input) + " is : " + str(output))

    def test_problem_3(self):
        input = 600851475143
        log.info("Problem3: Lets find the largest prime factor of : " + str(input))
        try:
            output = self.mm.largest_prime_factor(input)
            log.info("Problem3: The largest prime factor of : " + str(input) + " is : " + str(output))
        except Exception as e:
            log.exception("Problem3: Error finding largest prime factor with msg: " + e.message)
            raise

    def test_problem_4(self):
        input = 3
        log.info("Problem4: Lets find the largest palindromic product of 2 " + str(input) + "-digit numbers")
        try:
            output = self.mm.largest_palindromic_product_2(input)
            log.info("Problem4: The largest palindromic product of 2 " + str(input) + "-digit numbers is: " + str(output))
        except Exception as e:
            log.exception("Problem4: Error finding largest palindromic product with msg: " + e.message)
            raise

    def test_problem_5(self):
        log.info("Problem5: Not implemented yet")

    def test_problem_6(self):
        input = 100
        log.info("Problem6: Lets find the difference between the square of the sum of the first " + str(input) + " natural numbers and the sum of their squares")
        try:
            output = self.mm.square_of_sum(input) - self.mm.sum_of_squares(input)
            log.info("Problem6: The difference between the square of the sum of the first " + str(input) + " natural numbers and the sum of their squares is : " + str(output))
        except Exception as e:
            log.exception("Problem6: Error finding difference between square and sum with msg: " + e.message)
            raise

    def test_problem_7(self):
        input = 10001
        log.info("Problem7: Finding " + str(input) + "th prime")
        output = self.mm.get_nth_prime(input)
        log.info("Problem7: Found " + str(input) + "th prime as " + str(output))


if __name__ == "__main__":
    logging.basicConfig(level = logging.DEBUG)
    unittest.main()


