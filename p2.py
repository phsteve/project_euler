#!/usr/bin/python

#Project Euler problem #2

#Find the sum of all even terms in the Fibonacci sequence that do not exceed four million
#answer = 4613732

import time

def brute_fibo(n):
    #brute force method of calculating the nth Fibonacci number
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return brute_fibo(n-1) + brute_fibo(n-2)

memo = {}

def memoized_fibo(n):
    #memoized method of calculating the nth Fibonacci number by recalling previously
    #calculated Fibonacci numbers in memo
    if n == 0:
        memo[0] = 0
        return memo[0]
    if n == 1:
        memo[1] = 1
        return memo[1]
    if n-1 in memo.keys() and n-2 in memo.keys():
        memo[n] = memo[n-2] + memo[n-1]
        return memo[n]
    return memoized_fibo(n-2) + memoized_fibo(n-1)

def calc_memo():
    #calculate answer using memoized_fibo
    memoized_total = 0
    fibo_number = 0
    i = 0
    while fibo_number < 4000001:
        fibo_number = memoized_fibo(i)
        if fibo_number % 2 == 0:
            memoized_total += fibo_number
        i += 1
    return memoized_total

def calc_brute():
    #calculate answer using brute_fibo
    brute_total = 0
    fibo_number = 0
    i = 0
    while fibo_number < 4000001:
        fibo_number = brute_fibo(i)
        if fibo_number % 2 == 0:
            brute_total += fibo_number
        i += 1
    return brute_total

t1 = time.time()
print calc_memo()
print "Memoization took %f seconds" %(time.time()-t1)

t2 = time.time()
print calc_brute()
print "Brute force took %f seconds" %(time.time()-t2)
#memoization is faster by about 3 orders of magnitude

