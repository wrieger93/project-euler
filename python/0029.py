# This should be self-explanatory.

# Output: 9183

max_num = 100
if __name__ == "__main__":
    print(len(set(a**b for a in range(2,max_num+1) for b in range(2,max_num+1))))
