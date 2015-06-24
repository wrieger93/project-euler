# This should be self-explanatory.

# Output:

from eulerutils import prime_gen

if __name__ == "__main__":
    count = 0
    for p in prime_gen():
        count += 1
        if count == 10001:
            print(p)
            break
