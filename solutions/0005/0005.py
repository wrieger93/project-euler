# This should be self-explanatory.

# Output:

import functools

from eulerutils import lcm

if __name__ == "__main__":
    print(functools.reduce(lambda a,b: lcm(a,b), range(1,21)))
