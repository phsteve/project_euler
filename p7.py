#!/usr/bin/python

#Project Euler #7

#What's the 10001st prime number?
#answer = 104743

import math

import prime_tools

def main():
    count = 1
    num = 2

    while count < 10001:
        num += 1
        if prime_tools.isprime(num):
            count += 1

    print num

main()