/*
9!*8 is 7 digits, which is the largest possible sum for 8 digits, so there can
be at most 7 digits. we try all of them.
*/

#include <iostream>

using std::cout;

// thanks mathematica
int facts[10] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};

int factdigits(int n) {
    int tot = 0;
    while(n > 0) {
        tot += facts[n%10];
        n = n/10;
    }
    return tot;
}

int main() {
    int tot = 0;
    for(int i = 10; i < 10000000; ++i) {
        if(factdigits(i) == i) {
            tot += i;
        }
    }
    cout << tot << "\n"; // answer is 40730
}
