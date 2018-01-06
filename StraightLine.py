""" 
Calculates the Chi-Squared values for guess EA and A values in order to find the optimal one that minimises the Chi-Squared value. 
"""
import math

# Chi Squared calculations
def chi_squared(expected, observed):
	chi_squared = 0
	for i in range(len(observed)):
		chi_squared += ((observed[i]-expected[i])**2)/ expected[i]
	del expected[:]
	return chi_squared
# Calculates expected values of k for the inputted EA and A
def expected_calculated(T, ea, a, expected_k):
	for i in range(len(T)):
		expected_k.append(a*math.exp(-(ea*1e3)/(8.3145*T[i])))
	return expected_k

def main():
	expected_k = []
	T = [700, 730, 760, 790, 810, 840, 910, 1000]
	observed_k = [0.011, 0.035, 0.105, 0.343, 0.789, 2.17, 20.0, 145]
	ea = 0.0
	a = 0.0
	change_ea = 10.0
	change_a = 0.1e12
	chi_squared_min = 0.0
	a_min = 0.0
	ea_min = 0.0

	ea = float(input("Please enter starting guess of EA?"))
	a = float(input("Please enter starting guess of A?  (in e12) "))

	a*=1e12
	while (change_ea > 1 ):
		chi_squared_1 = chi_squared(expected_calculated(T, ea, a, expected_k), observed_k)
		chi_squared_2 = chi_squared(expected_calculated(T, ea + change_ea, a, expected_k), observed_k)
		#print(chi_squared_2)
		if chi_squared_1 > chi_squared_2:
			ea += change_ea
			ea_min = ea
			chi_squared_min = chi_squared_2
		else:
			change_ea /= 2

			while (change_a > 0.1e11):
				chi_squared_1 = chi_squared(expected_calculated(T, ea, a, expected_k), observed_k)
				chi_squared_2 = chi_squared(expected_calculated(T, ea, a + change_a, expected_k), observed_k)

				if chi_squared_1 > chi_squared_2:
					a += change_a
					a_min = a
					chi_squared_min = chi_squared_2
				else:
					change_a /= 2

	print("The minimum Chi Squared value is: ", chi_squared_min)
	print("This is for the EA value: ", ea_min, " kJ mol^-1")
	print("This is for the A value: ", a_min, " L mol^-1 s^-1")


if __name__ == "__main__":
	main()
