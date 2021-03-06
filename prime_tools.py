#!/usr/bin/python

#Collection of useful tools for working with prime numbers

import math

def sieve(n):
    #creates a Sieve of Eratosthenes from 2 to n-1
    #Sieve is a dictionary where True indicates prime and False indicates nonprime
    sv = dict.fromkeys(range(2, n), True)
    for num in xrange(2, int(math.sqrt(n))):
        if sv[num]:
            #print "checking multiples of %d" %(num)
            for i in xrange(2, n/num + 1):
                #print "     %d is not prime, marking False" %(num * i)
                sv[num * i] = False
    return sv

def isprime(num):
    #Brute force check if a number is prime by checking divisibility
    for d in xrange(2, int(math.sqrt(num))+1):
        if num % d == 0:
            return False
    return True

def find_2_factors(num):
    #helper function for brute force factoring, finds the lowest prime factor of a number
    for d in xrange(2, int(math.sqrt(num))):
        if num % d == 0:
            return [num/d, d]