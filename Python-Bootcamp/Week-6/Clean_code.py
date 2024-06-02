def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest


def calculate_compound_interest(principal, rate, time, n=1):
    amount = principal * (1 + rate / (100 * n)) ** (n * time)
    compound_interest = amount - principal
    return compound_interest


P = 1000  # Principal amount
R = 5  # Annual interest rate
T = 2  # Time in years
n = 4  # Compounding quarterly

si = calculate_simple_interest(P, R, T)
ci = calculate_compound_interest(P, R, T, n)

print(f"Simple Interest: {si}")
print(f"Compound Interest: {ci}")
