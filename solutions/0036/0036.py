# This should be self-explanatory.

# Output: 872187

if __name__ == "__main__":
    tot = 0
    for i in range(1, 1000000):
        base10digits = str(i)
        base2digits = str(bin(i))[2:]
        if (base10digits == base10digits[::-1] and
                base2digits == base2digits[::-1]):
            tot += i
    print(tot)
