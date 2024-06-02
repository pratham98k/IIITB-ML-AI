def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    :param principal: The initial amount of money
    :param rate: The annual interest rate (in percentage)
    :param time: The time the money is invested for (in years)
    :return: The simple interest
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest

def calculate_compound_interest(principal, rate, time, n):
    """
    Calculate compound interest.

    :param principal: The initial amount of money
    :param rate: The annual interest rate (in percentage)
    :param time: The time the money is invested for (in years)
    :param n: The number of times that interest is compounded per year
    :return: The compound interest
    """
    amount = principal * (1 + (rate / (100 * n))) ** (n * time)
    compound_interest = amount - principal
    return compound_interest

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in percentage): "))
    time = float(input("Enter the time (in years): "))
    n = int(input("Enter the number of times interest is compounded per year (for compound interest): "))

    simple_interest = calculate_simple_interest(principal, rate, time)
    compound_interest = calculate_compound_interest(principal, rate, time, n)

    print(f"Simple Interest: {simple_interest}")
    print(f"Compound Interest: {compound_interest}")

if __name__ == "__main__":
    main()
