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
        input = 20
        log.info("Problem5: Find the lowest common multiple of the first " + str(input) + " numbers")
        try:
            output = self.mm.get_lcm_n(input)
            log.info("Problem5: The lowest common multiple of the first " + str(input) + " numbers is : " + str(output))
        except Exception as e:
            log.exception("Problem5: Error find the lowest common multiple with msg: " + e.message)
            raise

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

    def test_problem_8(self):
        large_num = "73167176531330624919225119674426574742355349194934"\
                    "96983520312774506326239578318016984801869478851843"\
                    "85861560789112949495459501737958331952853208805511"\
                    "12540698747158523863050715693290963295227443043557"\
                    "66896648950445244523161731856403098711121722383113"\
                    "62229893423380308135336276614282806444486645238749"\
                    "30358907296290491560440772390713810515859307960866"\
                    "70172427121883998797908792274921901699720888093776"\
                    "65727333001053367881220235421809751254540594752243"\
                    "52584907711670556013604839586446706324415722155397"\
                    "53697817977846174064955149290862569321978468622482"\
                    "83972241375657056057490261407972968652414535100474"\
                    "82166370484403199890008895243450658541227588666881"\
                    "16427171479924442928230863465674813919123162824586"\
                    "17866458359124566529476545682848912883142607690042"\
                    "24219022671055626321111109370544217506941658960408"\
                    "07198403850962455444362981230987879927244284909188"\
                    "84580156166097919133875499200524063689912560717606"\
                    "05886116467109405077541002256983155200055935729725"\
                    "71636269561882670428252483600823257530420752963450"
        num_digits = 13

        log.info("Problem8: Finding " + str(num_digits) + " digit sequence in " + str(len(large_num)) + " digit large number with the greatest product")
        output = self.mm.get_greatest_product_sequence(large_num, num_digits)
        log.info("Problem8: Found " + str(num_digits) + " digit sequence with the greatest product as " + output)

    def test_problem_9(self):
        sum_of_abc = 1000
        log.info("Problem9: Finding product of Pythagorean triplet whose sum is: " + str(sum_of_abc))
        abc = self.mm.get_pythagorean_triplet_product_from_sum(sum_of_abc)
        log.info("Problem9: Found product of Pythagorean triplet whose sum is: " + str(sum_of_abc) + " as : " + str(abc))

    def test_problem_10(self):
        n = 2000000
        log.info("Problem10: Finding the sum of primes below " + str(n))
        sum_of_primes = self.mm.get_sum_of_primes(n)
        log.info("Problem10: Found the sum of primes below " + str(n) + " as : " + str(sum_of_primes))


if __name__ == "__main__":
    logging.basicConfig(level = logging.DEBUG)
    unittest.main()


