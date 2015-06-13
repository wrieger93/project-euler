# This should be self-explanatory.

# Output: 100

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

if __name__ == "__main__":
    tot_numerator = 1
    tot_denominator = 1
    for numerator in range(10, 100):
        for denominator in range(numerator+1, 100):
            n1 = numerator // 10
            n2 = numerator % 10
            d1 = denominator // 10
            d2 = denominator % 10
            frac = numerator/denominator
            # non-trivial means you have to cancel diagonally
            if ((n1 == d2 and n2/d1 == frac) or
                    (d2 != 0 and n2 == d1 and n1/d2 == frac)):
                tot_numerator *= numerator
                tot_denominator *= denominator
    print(tot_denominator//gcd(tot_numerator, tot_denominator))
