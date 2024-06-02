Principle_Amount=int(input("Enter Principle amount: "))

rate_of_interest=int(input("Enter rate of interest: "))

Years=int(input("Enter the Number if years, Default year is 1: "))

# Python3 program to find compound
# interest for given values.

def compound_interest(Principle_Amount, rate_of_interest, Years):

	# Calculates compound interest
	Amount = Principle_Amount * (pow((1 +  Principle_Amount/ 100), Years))
	CI = Principle_Amount - Principle_Amount
	print("Compound interest is", CI)


