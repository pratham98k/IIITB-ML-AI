n = int(input('Enter the end numbeer you want to print prime number500: '))

def generate_prime(n):
    """Generate the list of prime number up to n using the Siven Eratosthenes"""
    sieve = [True] * (n+1)
    prime = []
    for p in range(2, n+1):
        if sieve[p]:
            prime.append(p)
            for i in range(p*p, n+1,p):
                sieve[i] = False
    return prime

print(f"Prime number up to {n}: {generate_prime(n)}")