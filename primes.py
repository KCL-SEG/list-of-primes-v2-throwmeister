"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError
    list = []
    prime_number_holder = 1
    count = 0
    while count < number_of_primes:
        if is_prime(prime_number_holder, list):
            count += 1
            list.append(prime_number_holder)
        prime_number_holder += 1
    return list

def is_prime(num, p_list):
    if num == 1:
        return False
    if num == 2:
        return True
    for n in p_list:
        if num%n == 0:
            return False
    return True