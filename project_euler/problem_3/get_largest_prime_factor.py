import logging
import sys
import math


log = logging.getLogger(__name__)


def is_prime(n):
	m = 2
	p = int(math.sqrt(float(n)))
	while m <= p:
		if n%m == 0:
			return False
		m += 1
	return True

def largest_prime_factor(n):
	denominator = 2
	quotient = n/denominator
	largest_prime_from_bottom = 1
	while quotient >= denominator:
		log.debug("Evaluating : " + str(quotient))
		if n%quotient == 0:
			log.debug(str(quotient) + " divides " + str(n))
			if is_prime(quotient):
				log.debug("Largest prime so far is : " + str(quotient))
				return quotient
			else:
				if is_prime(denominator):
					largest_prime_from_bottom = denominator
		denominator += 1
		quotient = n/denominator
	if (largest_prime_from_bottom != 1):
		return largest_prime_from_bottom
	else:
		return n


if __name__ == "__main__":
	logging.basicConfig(level = logging.DEBUG)
	input = int(sys.argv[2])
	log.info("Lets find the largest prime factor of : " + str(input))
	try:
		output = largest_prime_factor(input)
		log.info("The largest prime factor of : " + str(input) + " is : " + str(output))
	except Exception as e:
		log.exception("Error finding largest prime factor with msg: " + e.message)
