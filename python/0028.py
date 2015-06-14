# This should be self-explanatory.

# Output: 669171001

# the sum of the diagonal values on the nth square, with n=1 the center
def nth_square_sum(n):
    if n == 1:
        return 1
    m = 2*n-1
    # upper right
    a = m*m
    # upper left
    b = m*m - 2*n + 2
    # lower left
    c = m*m - 4*n + 4
    # lower right
    d = m*m - 6*n + 6
    return a + b + c + d

if __name__ == "__main__":
    tot = 0
    for i in range(1, 1001//2+2):
        tot += nth_square_sum(i)
    print(tot)
