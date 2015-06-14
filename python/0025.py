# This should be self-explanatory.

# Output: 4782

if __name__ == "__main__":
    a, b = 1, 1
    idx = 1
    while len(str(b)) < 1000:
        a, b = a+b, a
        idx += 1
    print(idx)
