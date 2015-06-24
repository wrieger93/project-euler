# This should be self-explanatory.

# Output:

from eulerutils import num_divisors

if __name__ == "__main__":
    n = 1
    while num_divisors(n*(n+1)//2) < 500:
        n += 1
    print(n*(n+1)//2)
