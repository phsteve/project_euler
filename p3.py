#Project Euler #3

#What is the largest prime factor of the number 600851475143?
#Answer: 6857

import math
import time

import prime_tools

#Compare a brute force method vs a method that uses a sieve of Eratosthenes to

num = 600851475143

# def find_2_factors(num):
#     for d in range(2, int(math.sqrt(num))):
#         if num % d == 0:
#             return [num/d, d]

def brute_factor(num):
    prime_factors = []
    found_factors = [num]
    while found_factors:
        current_factor = found_factors.pop()
        factors = prime_tools.find_2_factors(current_factor)
        if factors:
            prime_factors.append(factors[1])
            found_factors.append(factors[0])
        else: #current_factor is prime
            prime_factors.append(current_factor)
    return prime_factors

def sieve_factor(num):
    t3 = time.time()
    s = prime_tools.sieve(int(math.sqrt(num)) + 1)
    primes = [p for p in s.keys() if s[p]]
    prime_factors = []
    for prime in primes:
        if num % prime == 0:
            prime_factors.append(prime)
    return prime_factors

def main():
    t1 = time.time()
    print max(brute_factor(num))
    #answer = 6857
    print " ".join(["brute_factor took", str(time.time() - t1), "seconds"])

    t2 = time.time()
    print max(p for p in sieve_factor(num))
    print " ".join(["sieve_factor took", str(time.time() - t2), "seconds"])

main()
