"""
suppose an n-digit number 10x+y is a divisor of its right rotation.
x is an (n-1)-digit number and y is a digit. note that y cannot be 0
because then its right rotation would be less than the original number. the
right rotation is easily seen to be 10^(n-1)y+x. in order to be a divisor of
its right rotation, we have 10^(n-1)y+x = k*(10x+y) for some integer k. note
k cannot be 0 and k must be less than 10. solving this equation for x, we have
x = y*(10^(n-1)-k)/(10k-1). thus, we just test 1<=k,y<=9, 2<=n<=100. to test if
a fraction a/b is an integer, we want gcd(a,b) = b. finally we have to make sure
the resulting number 10x+y is the correct number of digits because it might be
the case that it has a leading zero, ie, x is less than n-1 digits.
"""

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

def brute(n):
    tot = 0
    for num in range(10,10**n + 1):
        rrot = (num%10)*10**(len(str(num))-1) + num//10
        if gcd(rrot, num) == num:
            tot += num
            tot = tot % 10**5
    return tot

def smart(n):
    tot = 0
    for digits in range(2,n+1):
        for k in range(1,10):
            for y in range(1,10):
                a = y*(10**(digits-1) - k)
                b = 10*k - 1
                if gcd(a,b) == b:
                    x = a//b
                    if len(str(10*x+y)) == digits:
                        tot += 10*x + y
                        tot = tot%10**5
    return tot

if __name__ == "__main__":
    print(smart(100))
