# This should be self-explanatory.

# Output: 871198282

import functools
import os
import sys

def partial_name_score(name):
    # the 64 is because ord('A') = 65
    return sum([ord(x)-64 for x in name])

if __name__=="__main__":
    line = None
    with open(os.path.join(os.path.dirname(sys.argv[0]), "names.txt")) as f:
        line = f.readline()

    names = sorted([x[1:-1] for x in line.split(',')])
    print(sum([(i+1)*partial_name_score(names[i]) for i in range(len(names))]))
