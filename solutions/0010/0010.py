# This should be self-explanatory.

# Output:

from eulerutils import prime_gen

if __name__ == "__main__":
    tot = 0
    for p in prime_gen():
        if p > 2000000:
            break
        tot += p
    print(tot)
