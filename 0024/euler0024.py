# This should be self-explanatory.

# Output: 2783915460

def factorial(n):
    if n < 2:
        return 1
    tot = 1
    for i in range(2, n):
        tot *= i
    return tot

# the kth permutation of lst (k=0 is the first)
# find the first element and recursively find the permutation of the rest of the list
def permutation(lst, k):
    if len(lst) == 1:
        return lst
    idx = k // factorial(len(lst))
    return [lst[idx]] + permutation(lst[:idx] + lst[idx+1:], k % factorial(len(lst)))

if __name__ == "__main__":
    print("".join([str(x) for x in permutation(list(range(10)), 1000000-1)]))
