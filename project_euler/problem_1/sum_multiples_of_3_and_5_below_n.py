import logging
import sys

log = logging.getLogger(__name__)

def sum_of_multiples(n):
	sum = 0
	for i in range(1,n):
		log.debug("Evaluating " + str(i))
		if (i%3 == 0):
			sum += i
		elif (i%5 == 0):
			sum += i
	return sum
			
		
if __name__ == "__main__":
	logging.basicConfig(level = logging.DEBUG)
	input = int(sys.argv[1])
	log.info("Lets sum the multiples of 3 and 5 below : " + str(input))
	output = sum_of_multiples(input)
	log.info("Sum of multiples of 3 and 5 below : " + str(input) + " is : " + str(output))
