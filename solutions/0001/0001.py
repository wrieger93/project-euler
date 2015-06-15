# This should be self-explanatory.

# Output: 233168

if __name__ == "__main__":
    print(sum(x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0))
