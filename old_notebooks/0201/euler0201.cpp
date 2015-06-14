#include <iostream>
#include <vector>

/*
 * It's a DP problem. hits[s][e] is how many times we get
 * the sum 's' with a 'e'-element subset. We iteratively
 * consider each i^2. If we can get a sum of 's' with
 * 'e' elements, then we can get a sum of 's+i^2'
 * with 'e+1' elements, so we do
 * hits[s+i^2,e+1] += hits[s,e]; Also, hits[i^2][1] = 1.
 * We work up from i = 1 to i = 100. We have to store
 * the previous results in hits_copy because otherwise
 * we'd be modifying the array as we're iterating over it.
 */

using std::cout;
using std::vector;

const int SET_SIZE = 100;
const int SUBSET_SIZE = SET_SIZE/2;
const int MAX_SUM = SET_SIZE*(SET_SIZE+1)*(2*SET_SIZE+1)/6;

void copy(int** a1, int** a2, int xmax, int ymax) {
    for(int i = 0; i < xmax; ++i) {
        for(int j = 0; j < ymax; ++j) {
            a2[i][j] = a1[i][j];
        }
    }
}

int main() {
    vector<int> set;
    for(int i = 1; i <= SET_SIZE; ++i) {
        set.push_back(i*i);
    }

    int** hits = new int*[MAX_SUM+1];
    int** hits_copy = new int*[MAX_SUM+1];
    for(int sum = 0; sum <= MAX_SUM; ++sum) {
        hits[sum] = new int[SET_SIZE+1];
        hits_copy[sum] = new int[SET_SIZE+1];
    }
    /* Initialize 'hits' to all 0's. */
    for(int sum = 0; sum <= MAX_SUM; ++sum) {
        for(int subset_size = 0; subset_size <= SET_SIZE; ++subset_size) {
            hits[sum][subset_size] = 0;
        }
    }
    /* Go through each element in the set and update 'hits' accordingly. */
    for(auto elem : set) {
        copy(hits, hits_copy, MAX_SUM+1, SET_SIZE+1);
        for(int sum = 1; sum <= MAX_SUM - elem; ++sum) {
            for(int subset_size = 1; subset_size < SET_SIZE; ++subset_size) {
                if(hits_copy[sum][subset_size] > 0) {
                    hits[sum+elem][subset_size+1] += hits_copy[sum][subset_size];
                }
            }
        }
        hits[elem][1] = 1;
    }

    /* Count up all sums with the proper subset size that only have only hit. */
    int tot = 0;
    for(int sum = 1; sum <= MAX_SUM; ++sum) {
        if(hits[sum][SUBSET_SIZE] == 1) {
            tot += sum;
        }
    }
    cout << tot << "\n";
    return 0;
}
