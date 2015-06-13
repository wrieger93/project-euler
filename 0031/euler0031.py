# This is a classic DP problem. Instead of using an array
# I use python's build-in memoization.

# Output: 73682

import functools

coins = [1, 2, 5, 10, 20, 50, 100, 200]

# the number of ways to do it using only the first k coins
@functools.lru_cache(maxsize=None)
def ways(n, k):
    if n < 0:
        return 0
    if n == 0 or k == 0:
        return 1
    return ways(n, k-1) + ways(n - coins[k], k)

if __name__ == "__main__":
    print(ways(200, len(coins)-1))
