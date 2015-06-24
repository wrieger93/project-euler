import functools
import itertools

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, \
        67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, \
        139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, \
        223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, \
        293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, \
        383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, \
        463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, \
        569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, \
        647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, \
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, \
        839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, \
        941, 947, 953, 967, 971, 977, 983, 991, 997]

def prime_gen():
    for p in primes:
        yield p

    n = primes[-1] + 2
    while True:
        prime = True
        for p in primes:
            if p*p > n:
                break
            if n % p == 0:
                prime = False
                break
        if prime:
            yield n
            primes.append(n)
        n += 1

def is_prime(n):
    if n < 2:
        return False
    gen = prime_gen()
    for p in gen:
        if p*p > n:
            break
        if n % p == 0:
            return False
    return True

def factor(n):
    factors = []
    gen = prime_gen()
    for p in gen:
        if p*p > n:
            factors.append((n, 1))
            return factors
        if n % p == 0:
            i = 0
            while n % p == 0:
                i += 1
                n = n // p
            factors.append((p, i))
        if n == 1:
            return factors

def num_divisors(n):
    factors = factor(n)
    tot = 1
    for p, e in factors:
        tot *= e + 1
    return tot

def divisors(n):
    factors = factor(n)
    args = [range(e+1) for p, e in factors]
    divs = []
    for arg in itertools.product(*args):
        prod = 1
        for (p, e), exp in zip(factors, arg):
            prod *= pow(p, exp)
        divs.append(prod)
    return sorted(divs)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a*b//gcd(a,b)
