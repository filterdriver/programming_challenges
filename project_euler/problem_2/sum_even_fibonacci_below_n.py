import logging
import sys

log = logging.getLogger(__name__)

def sum_of_even_fibonacci(n):
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
		log.debug("New fibonacci is: " + str(next_num))
		if (next_num%2 == 0):
			sum += next_num
		first = second
		second = next_num
	return sum
			
		
if __name__ == "__main__":
	logging.basicConfig(level = logging.DEBUG)
	input = int(sys.argv[1])
	log.info("Lets sum the even fibonacci numbers not greater than : " + str(input))
	output = sum_of_even_fibonacci(input)
	log.info("Sum of even fibonacci numbers not greater than : " + str(input) + " is : " + str(output))
