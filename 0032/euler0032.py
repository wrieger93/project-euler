# This should be self-explanatory.

# Output: 45228

import itertools

if __name__ == "__main__":
    prods = set()
    for perm in itertools.permutations(str(x) for x in range(1,10)):
        # (2-digit) * (3-digit) = (4-digit)
        a = int("".join(perm[:2]))
        b = int("".join(perm[2:5]))
        c = int("".join(perm[5:9]))
        if a * b == c:
            prods.add(c)

        # (1-digit) * (4-digit) = (4-digit)
        a = int("".join(perm[:1]))
        b = int("".join(perm[1:5]))
        c = int("".join(perm[5:9]))
        if a * b == c:
            prods.add(c)

    print(sum(prods))
