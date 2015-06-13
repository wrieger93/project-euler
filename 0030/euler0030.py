# 6*9^5 = 354294, so we don't need to check beyond that value.

# Output: 443839

max_num = 354294

if __name__ == "__main__":
    tot = 0
    for i in range(10, max_num):
        if i == sum([int(x)**5 for x in str(i)]):
            tot += i
    print(tot)
