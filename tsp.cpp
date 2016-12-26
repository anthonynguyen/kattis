#include <algorithm>
#include <cmath>
#include <ctime>
#include <iostream>
#include <string>

using namespace std;

#define square(a) ((a)*(a))

int main() {
	int num, idist;
	double dist;
	cin >> num;

	clock_t begin = clock();
	clock_t now;

	int dists[num][num];
	double points[num][2];
	int path[num];

	// read all points in
	for (int i = 0; i < num; i++) {
		cin >> points[i][0];
		cin >> points[i][1];

		// initialize our path permutation array
		path[i] = i;
	}

	// precompute distance matrix
	for (int i = 0; i < num; i++) {
		for (int j = 0; j < num; j++) {
			dist = sqrt(square(points[i][0] - points[j][0]) + square(points[i][1] - points[j][1]));
			idist = (int)round(dist);
			dists[i][j] = idist;
			dists[j][i] = idist;
		}
	}

	int min_path[num];
	int total;

	int bf_min_path[num];
	int bf_total = -1;

	int gr_min_path[num], gr_used[num] = {0};
	int gr_total = 0, best;

	int slow = 0;

	int iter = 0;
	
	// (brute force) try all permutations -- this solution is too slow
	// but it is fast enough for 12 points or fewer with:
	// -g -O2 -static -std=gnu++11

	do {
		iter++;
		idist = 0;
		for (int i = 0; i < num-1; i++) {
			idist += dists[path[i]][path[i+1]];
		}
		if (idist < bf_total || bf_total == -1) {
			copy(path, path + num, bf_min_path);
			bf_total = idist;
		}

		// run the brute force solution until 1.95 seconds,
		// then compare the best brute force result with the greedy result
		// only check time every 1000 iterations to avoid too much slowdown
		if (iter % 1000 == 0) {
			now = clock();
			if ((double(now - begin) / CLOCKS_PER_SEC) > 1.95) {
				slow = 1;
				break;
			}
		}
	} while (next_permutation(path + 1, path + num));

	if (slow) {
		// try the greedy solution if we're too slow
		// greedy solution - this solution should usually be wrong
		gr_min_path[0] = 0;
		gr_used[0] = 1;
		idist = 0;
		for (int i = 1; i < num; i++) {
			best = -1;
			for (int j = 0; j < num; j++) {
				if (!gr_used[j] && (best == -1 || dists[gr_min_path[i-1]][j] < dists[gr_min_path[i-1]][best])) {
					best = j;
				}
			}
			gr_min_path[i] = best;
			gr_total += dists[gr_min_path[i-1]][best];
			gr_used[best] = 1;
		}
	} else {
		gr_total = bf_total + 1;
	}


	if (gr_total < bf_total) {
		copy(gr_min_path, gr_min_path + num, min_path);
		total = gr_total;
	} else {
		copy(bf_min_path, bf_min_path + num, min_path);
		total = bf_total;
	}

	for (int i = 0; i < num; i++) {
		cout << to_string(min_path[i]) << endl;
	}
}
