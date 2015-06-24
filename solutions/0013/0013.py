# This should be self-explanatory

# Output: 5537376230

import os
import sys

if __name__=="__main__":
    with open(sys.argv[1]) as f:
        tot = 0
        for line in f:
            tot += int(line)
    print(str(tot)[:10])
