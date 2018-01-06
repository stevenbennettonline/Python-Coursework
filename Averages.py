"""
Opens a text file and calculates the mean and standard deviation for integers in the text "StatNum.txt" file.
There is no limit to the number of integers in the text file but each one must be on a new line. 
"""

import math

# Calculates sum
def sumIntegers(integers, size, mean = None):
	total = 0
	i = 0
	for integer in integers:
		if mean:
			total += (integers[i] - mean)**2
			i+=1
		else:
			total = sum(integers) 
	return total

def main():
	integers = []
	number = " "

	# Opens text file
	filename = "StatNum.txt"
	with open(filename) as file:
		for line in file:
			line = line.strip()
			integers.append(line) 
	file.close()

	for i in range(len(integers)):
		integers[i] = int(integers[i])

	size = len(integers)
	total = sumIntegers(integers, size)
	mean = total/size
	sum_mean_difference = sumIntegers(integers, size, mean)
	standard_deviation = math.sqrt(sum_mean_difference / (size - 1))

	dp = input("How many decimal places would you like the mean?\n")

	print("The sum is: ", total, "The average is: ", round(mean,int(dp)), "The standard deviation is: ", round(standard_deviation,int(dp)))

if __name__ == "__main__":
	main()
