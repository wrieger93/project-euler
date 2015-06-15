# This should be self-explanatory.

# Output: 906609

if __name__ == "__main__":
    max_prod = 0
    for a in range(100, 1000):
        for b in range(a, 1000):
            prod = a * b
            if str(prod) == str(prod)[::-1] and prod > max_prod:
                max_prod = prod
    print(max_prod)
