import logging
import sys
import math


log = logging.getLogger(__name__)


def is_palindrome(n):
	strn = str(n)
	num_digits = len(strn)
	i = 0
	while (i < num_digits/2):
		if strn[i] != strn[num_digits - i - 1]:
			return False
		i += 1
	return True

def largest_palindromic_product_2(n):
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
	log.debug(str(base) + "," + str(num))
	while (n1 > base*num):
		log.debug("start again: %s %s", n1, n2)
		while (n2 > base*num):
			if ((n2%10 == 7 and n1%10 == 7) or
			    (n2%10 == 3 and n1%10 == 3) or
			    (n2%10 == 1 and n1%10 == 9) or
			    (n2%10 == 9 and n1%10 == 1)):
				log.debug("%s %s", n1, n2)
				res = n1*n2
				if (is_palindrome(res)):
					return res
			n2 -= 2
		n1 -= 2
		n2 = k
		log.debug("end again: %s %s", n1, n2)
	if (len(palindromes) == 0):
		return None
	log.debug(palindromes)
	palindromes.sort()
	log.debug(palindromes)
	return palindromes[len(palindromes) - 1]

def largest_palindromic_product(n):
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
			log.debug(str(n1) + " times " + str(n2) + " = " + str(res))
			if (is_palindrome(res)):
				palindromes.append(res)
				break
			n2 -= 1
		n1 -= 1
		n2 = k
	log.debug(palindromes)
	palindromes.sort()
	log.debug(palindromes)
	return palindromes[len(palindromes) - 1]



if __name__ == "__main__":
	logging.basicConfig(level = logging.DEBUG)
	input = int(sys.argv[2])
	log.info("Lets find the largest palindromic product of 2 " + str(input) + "-digit numbers")
	try:
		output = largest_palindromic_product_2(input)
		log.info("The largest palindromic product of 2 " + str(input) + "-digit numbers is: " + str(output))
	except Exception as e:
		log.exception("Error finding largest palindromic product with msg: " + e.message)
