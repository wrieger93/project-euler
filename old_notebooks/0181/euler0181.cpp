#include <iostream>
#include <iterator>

/*
 * It's a simple DP problem. We can represent an element in a partition as the tuple
 * (black, white). Suppose we have a list ls of length L of every possible tuple that
 * could be used. We create the function p(black, white, k) that returns the total
 * number of partitions of the set (black, white) using the first k elements of lst.
 * We can set up the recursion p(b, w, k) = p(b, w, k-1) + p(b - list[k].black,
 * w - list[k].white, k). The first terms corresponds to when the partition doesn't use
 * list[k] (in which case it's just the number of partitions using up to l[k-1]) and
 * the second case corresponds to when it does use l[k] (in which case we subtract it from
 * b and w). We then compute p(B, W, (B+1)*(W+1)), where B and W are the total number
 * of black and white objects respectively. (B+1)*(W+1) is the total number of tuples
 * that could be used in the partition. Using dynamic programming this can be solved in
 * O(B^2W^2) time.
 *
 */

const int M = 60;
const int N = 40;
const int TOTPAIRS = (M+1)*(N+1);

int main() {
    /* The list that contains all possible tuples to use. */
    int pairs[TOTPAIRS][2];
    /* The results for the current and previous iterations of the outermost for loop */
    long long memo_curr[M+1][N+1];
    long long memo_prev[M+1][N+1];

    /* Initialize 'pairs'. */
    int k = 0;
    for(int m = 0; m <= M; ++m) {
        for(int n = 0; n <= N; ++n) {
            pairs[k][0] = m;
            pairs[k][1] = n;
            ++k;
        }
    }

    /* Iterate over every possible p(m, n, k). */
    for(int k = 0; k < TOTPAIRS; ++k) {
        /* Copy the current results to the previous results array. */
        std::copy(std::begin(memo_curr), std::end(memo_curr), std::begin(memo_prev));
        for(int m = 0; m <= M; ++m) {
            for(int n = 0; n <= N; ++n) {
                /* If there are no objects, there's one way to partition them. */
                if(m == 0 && n == 0) {
                    memo_curr[m][n] = 1LL;
                }
                /* If we can't use any tuples from the list, there's no ways. */
                else if(k == 0) {
                    memo_curr[m][n] = 0LL;
                }
                else {
                    /* This is p(m, n, k) = p(m, n, k-1). */
                    memo_curr[m][n] = memo_prev[m][n];
                    /* This is the other part. */
                    int mdiff = m - pairs[k][0];
                    int ndiff = n - pairs[k][1];
                    if(mdiff >= 0 && ndiff >= 0) {
                        memo_curr[m][n] += memo_curr[mdiff][ndiff];
                    }
                }
            }
        }
    }

    /* Our answer is p(M, N, (M+1)*(N+1)), which is [M][N] in our last result array. */
    std::cout << memo_curr[M][N] << "\n";
    return 0;
}
