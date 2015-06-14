# This should be self-explanatory.

# Output: 4613732

max_fib = 4000000
if __name__ == "__main__":
    tot = 0
    a, b = 1, 1
    while b < max_fib:
        a, b = a+b, a
        if b % 2 == 0:
            tot += b
    print(tot)
