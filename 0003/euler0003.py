from math import sqrt

def factors(n):
    factors = {}
    while n % 2 == 0:
        if 2 not in factors:
            factors[2] = 0
        factors[2] += 1
        n /= 2
    for i in xrange(3, int(sqrt(n)) + 1, 2):
        if i > n:
            break
        while n % i == 0:
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
            n /= i
    if n != 1:
        factors[n] = 1
    return factors

if __name__ == "__main__":
    print max(factors(600851475143).keys())
