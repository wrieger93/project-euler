# This should be self-explanatory

# Output: 5537376230

import os
import sys

if __name__=="__main__":
    path = os.path.join(os.path.dirname(sys.argv[0]), "nums.txt")
    with open(path) as f:
        tot = 0
        for line in f:
            tot += int(line)
    print(str(tot)[:10])
