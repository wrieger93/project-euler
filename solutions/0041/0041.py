# This should be self-explanatory.

# Output: 7652413

import itertools
from eulerutils import is_prime

if __name__ == "__main__":
    # it can't be 8 or 9 digits since any 8 or 9 digit pandigital is
    # divisble by 3
    perms = itertools.permutations(range(1,8)[::-1])
    for perm in perms:
        num = int("".join(str(x) for x in perm))
        if is_prime(num):
            print(num)
            break
