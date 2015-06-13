/*
 * This should be self-explanatory.
 *
 * Output: 40730
 */

#include <iostream>

using std::cout;

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
    for(int i = 10; i < 10000000; i++) {
        if(factdigits(i) == i) {
            tot += i;
        }
    }
    cout << tot << "\n";
    return 0;
}
