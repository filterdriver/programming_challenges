import logging
import sys
import math


log = logging.getLogger(__name__)


class ProjectEuler():

    def is_palindrome(self, n):
        strn = str(n)
        num_digits = len(strn)
        i = 0
        while (i < num_digits/2):
            if strn[i] != strn[num_digits - i - 1]:
                return False
            i += 1
        return True

    def is_prime(self, n):
        if n == 1:
            return False
        m = 2
        p = int(math.sqrt(float(n)))
        while m <= p:
            if n%m == 0:
                return False
            m += 1
        return True

    def get_greatest_product_sequence(self, large_num, n):
        log.debug("Large number = " + large_num)
        log.debug("Num digits  = " + str(n))

        i = 0
        greatest_product = 0
        greatest_prod_str = 0

        str_len = len(large_num)
        while (i <= str_len - n):
            prod_str = large_num[i:i+n]
            log.debug("Current sequence is: " + prod_str)
            product = 1
            j = 0
            while j < n:
                product *= int(prod_str[j])
                j += 1
            log.debug("Current product is: " + str(product))
            if (product > greatest_product):
                greatest_product = product
                greatest_prod_str = prod_str
                log.debug("Greatest product " + str(greatest_product) + " sequence is " + greatest_prod_str)
            i += 1

        return greatest_prod_str

    def get_nth_prime(self, n):
        i = 1
        j = 0
        while j < int(n):
            i += 1
            if (self.is_prime(i)):
                j += 1
        return i

    def sum_of_squares(self, n):
        sum = 0
        for i in range(1, n + 1):
            sum += i*i
        return sum

    def square_of_sum(self, n):
        sum = n*(n+1)/2
        return sum*sum

    def get_lcm_n(self, n):
        i = 1
        lcm_factors = list()
        while (i <= n):
            if (self.is_prime(i)):
                lcm_factors.append(i)
            else:
                res = i
                for lcm_elem in lcm_factors:
                    if (res%lcm_elem == 0):
                        res /= lcm_elem
                        if (res == 1):
                            break
                if res != 1:
                    lcm_factors.append(res)
            i += 1
        lcm = 1
        for lcm_elem in lcm_factors:
            lcm *= lcm_elem
        return lcm

    def largest_palindromic_product_2(self, n):
        if n == 1:
            k, l = 9, 1
        elif n == 2:
            k, l = 99, 10
        elif n == 3:
            k, l = 999, 100
        elif n == 4:
            k, l = 9999, 1000
        else:
            raise Exception("Invalid input")
        n1 = n2 = k

        log.debug("Starting with n1,n2 = %s,%s", n1, n2)
        palindromes = list()
        base = int(math.pow(10, n-1))
        num = n1/base
        while (n1 > base*num):
            while (n2 > base*num):
                if ((n2%10 == 7 and n1%10 == 7) or
                    (n2%10 == 3 and n1%10 == 3) or
                    (n2%10 == 1 and n1%10 == 9) or
                    (n2%10 == 9 and n1%10 == 1)):
                    res = n1*n2
                    if (self.is_palindrome(res)):
                        return res
                n2 -= 2
            n1 -= 2
            n2 = k
        if (len(palindromes) == 0):
            return None
        palindromes.sort()
        return palindromes[len(palindromes) - 1]

    def largest_palindromic_product(self, n):
        if n == 1:
            k, l = 9, 1
        elif n == 2:
            k, l = 99, 10
        elif n == 3:
            k, l = 999, 100
        elif n == 4:
            k, l = 9999, 1000
        else:
            raise Exception("Invalid input")
        n1 = n2 = k

        log.debug("Starting with n1,n2 = %s,%s", n1, n2)
        palindromes = list()
        while (n1 > l):
            while (n2 >= n1):
                res = n1*n2
                if (is_palindrome(res)):
                    palindromes.append(res)
                    break
                n2 -= 1
            n1 -= 1
            n2 = k
        palindromes.sort()
        return palindromes[len(palindromes) - 1]

    def largest_prime_factor(self, n):
        denominator = 2
        quotient = n/denominator
        largest_prime_from_bottom = 1
        while quotient >= denominator:
            if n%quotient == 0:
                if self.is_prime(quotient):
                    return quotient
            else:
                if self.is_prime(denominator):
                    largest_prime_from_bottom = denominator
            denominator += 1
            quotient = n/denominator
        if (largest_prime_from_bottom != 1):
            return largest_prime_from_bottom
        else:
            return n

    def sum_of_even_fibonacci(self, n):
        sum = 0
        first = 1
        second = 2
        sum = second
        while (True):
            if (first >= n):
                break
            if (second >= n):
                break
            next_num = first + second
            if (next_num >= n):
                break
            if (next_num%2 == 0):
                sum += next_num
            first = second
            second = next_num
        return sum

    def sum_of_multiples(self, n):
        sum = 0
        for i in range(1,n):
            if (i%3 == 0):
                sum += i
            elif (i%5 == 0):
                sum += i
        return sum
