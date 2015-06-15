# This should be self-explanatory.

# Output: 25164150

if __name__ == "__main__":
    print(sum(range(101))**2 - sum(x**2 for x in range(101)))
