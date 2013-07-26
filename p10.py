#Find the sum of all primes below two million
#Answer: 142913828922

#We compare two methods, the brute force method and the Sieve of Eratosthenes method.
#The Sieve method is an order of magnitude quicker.

import math
import time

import prime_tools

def brute_force_sum_primes():
    return sum(x for x in xrange(2, 2000001) if prime_tools.isprime(x))

def sieve_sum_primes():
    s = prime_tools.sieve(2000001)
    return sum(x for x in s.keys() if s[x])

def main():
    t1 = time.time()
    print brute_force_sum_primes(), "Brute force method took %f seconds." % (time.time()-t1)

    t2 = time.time()
    print sieve_sum_primes(), "Sieve method took %f seconds." % (time.time()-t2)

main()