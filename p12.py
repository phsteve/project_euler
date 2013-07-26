#Triangle numbers are created by adding the sequence of natural numbers.
#i.e. 7th triangle number is 1+2+3+4+5+6+7=28. So the first ten terms of the
#triangle number sequence are 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
#Look at the divisors for the first seven:
#1: 1 = 1
#3: 1, 3 = 2
#6: 1, 3, 6 = 3
#10: 1, 2, 5, 10 = 4
#15: 1, 3, 5, 15 = 4
#21: 1, 3, 7, 21 = 4
#28: 1, 2, 4, 7, 14, 28 = 6
#36: 1, 2, 3, 4, 6, 9, 12, 18, 36 = 9
#45: 1, 3, 5, 15, 45 = 5

#Whats the first triangle number that has more than 500 divisors?

import math


def is_prime(n):
    for i in xrange(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def prime_numbers():
    #generator that yields prime numbers
    yield 2
    current = 3
    yield current
    while True:
        current += 2
        if is_prime(current):
            yield current
        
def tri_numbers():
    #generator that yields triangle numbers
    current = 1
    count = 0
    while True:
        yield current + count
        count = count + 1
        current = current + count

#tri_nums = tri_numbers()
#for i in range(10):
#    print next(tri_nums)
#primes = prime_numbers()
#for i in range(20):
#    print next(primes)

def find_2_factors(n):
    #helper function for prime_factors
    #for d in xrange(2, int(math.sqrt(n))+1):
    for d in range(2, 1000):
        if n % d == 0: #==>d is always prime, I think
            return [n/d, d]

def prime_factors(n):
    #returns a list of all (possibly repeated) prime factors of n
    prime_factors = []
    found_factors = [n]
    while found_factors:
        current_factor = found_factors.pop()
        factors = find_2_factors(current_factor)
        if factors:
            prime_factors.append(factors[1])
            found_factors.append(factors[0])
        else: #current factor is prime
            prime_factors.append(current_factor)
    return prime_factors

def all_divisors(n):
    #brute force method of checking all integers up to n/2 + 1 to see if they divide
    #returns a list of all factors of n (including n, excluding 1)
    divisors = []
    for d in xrange(2, n/2+1):
        if n % d == 0:
            divisors.append(d)
    divisors.append(n)
    return divisors

def freq_dist(lst):
    #returns a dictionary, keys are the unique elements of lst,
    #values are how many times they occur in lst
    #should I do this with a dict comprehension?
    freq_dist = {}
    for item in lst:
        if item in freq_dist:
            freq_dist[item] += 1
        else:
            freq_dist[item] = 1
    return freq_dist

def choose(n, k):
    #returns n choose k, i.e. the number of ways to choose k items from a group of n items
    #guaranteed to be an integer
    return math.factorial(n)/(math.factorial(k) * math.factorial(n - k))

def combinations(n):
    #returns the number of possible ways to combine n elements in groups of 1 up to n
    result = 0
    for k in xrange(1, n+1):
        result += choose(n, k)
    return result

def powers_of_factors(freq_dist):
    #returns a list of factors that are powers of unique factors
    #eg prf({2:2, 3:3, 5:1}) = [2, 4, 3, 9, 5]
    result = []
    for p_f in freq_dist:
        for i in range(1, freq_dist[p_f] + 1):
            result.append(p_f * i)
    return result



#test = [1, 2, 3, 3, 4, 7, 5, 5, 8, 5, 6, 3, 3]
#print freq_dist(test)


def combinatoric_divisors(n):
    #first find all prime factors, then use combinatorics to find the number of divisors
    #finding each divisor is not necessary
    # prime_factors = prime_factors(n)
    # freq_dist = freq_dist(prime_factors)
    # repeats = {key:freq_dist[key] for key in freq_dist if freq_dist[key]>1}
    # num_primes = len(prime_factors) #n in notes
    # num_unique_primes = len(freq_dist) #m in notes

    # return num_unique_primes + combinations(num_primes) - #duplicate factors

    p_f = prime_factors(n)
    f_d = freq_dist(p_f)
    p_o_f = powers_of_factors(f_d)
    print p_o_f
    k = len(p_o_f)
    return combinations(k) + 1
#print combinatoric_divisors(36)
#print "hello"

def product_of_values(d):
    #returns the product of values of key, value pairs in d
    result = 1
    for k in d:
        result *= d[k]
    return result

def num_divisors(n):
    p_f = prime_factors(n)
    f_d = freq_dist(p_f)
    #print n, p_f, f_d
    num_multi_factors = product_of_values(f_d)
    return len(p_f) + num_multi_factors + 1

#tri_nums = tri_numbers()
#for i in range(10):
#    print num_divisors(next(tri_nums))
#print num_divisors(45)



def better_main(n):
    tri_nums = tri_numbers()
    count = 0
    for tn in tri_nums:
        nd = num_divisors(tn)
        count += 1
        if count % 10 == 0:
            print tn, nd
        if nd > n:
            return tn

#print better_main(100)
#print better_main(100)
#print better_main(500)

#n = 2 **497*(2**498+1)
#print prime_factors(n)
#print num_divisors(2**497*(2**498+1))

#for n in range(2, 149):
#    num = 2**n*(2**(n+1)+1)
#    if num_divisors(num) >= 500:
#        print n, num_divisors(num), num
    #print num
n = 134
print num_divisors(2**n * (2**(n+1)+1))
    #print n, num_divisors(2**n * (2**(n+1)+1))


#print prime_factors(28)
#print all_divisors(28)
def main(n):
    #brute force method, chokes about n=~200 ish
    #what's the complexity? O(n^2) probably?
    #for loop in main with for loop in all_divisors
    tri_nums = tri_numbers()
    for tn in tri_nums:
        if len(all_divisors(tn))>n:
            return tn
#print main(100)


    f_d = freq_dist(p_f)
    #print n, p_f, f_d
    num_multi_factors = product_of_values(f_d)
    return len(p_f) + num_multi_factors + 1

#tri_nums = tri_numbers()
#for i in range(10):
#    print num_divisors(next(tri_nums))
#print num_divisors(45)



def better_main(n):
    tri_nums = tri_numbers()
    count = 0
    for tn in tri_nums:
        nd = num_divisors(tn)
        count += 1
        if count % 10 == 0:
            print tn, nd
        if nd > n:
            return tn

#print better_main(100)
#print better_main(100)
#print better_main(500)

#n = 2 **497*(2**498+1)
#print prime_factors(n)
#print num_divisors(2**497*(2**498+1))

#for n in range(2, 149):
#    num = 2**n*(2**(n+1)+1)
#    if num_divisors(num) >= 500:
#        print n, num_divisors(num), num
    #print num
n = 134
print num_divisors(2**n * (2**(n+1)+1))
    #print n, num_divisors(2**n * (2**(n+1)+1))


#print prime_factors(28)
#print all_divisors(28)
def main(n):
    #brute force method, chokes about n=~200 ish
    #what's the complexity? O(n^2) probably?
    #for loop in main with for loop in all_divisors
    tri_nums = tri_numbers()
    for tn in tri_nums:
        if len(all_divisors(tn))>n:
            return tn
#print main(100)

