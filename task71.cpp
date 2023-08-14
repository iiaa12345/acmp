#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int main() {
    int n;
    cin >> n;

    int t;
    vector<int> a;
    for (int i = 0; i < n; i++) {
        cin >> t;
        a.push_back(t);
    }

    int min_diff = numeric_limits<int>::max();

    vector<int> b(n, 0);
    while (true) {
        int sum1 = 0;
        int sum2 = 0;
        for (int i = 0; i < n; i++) {
            if (b[i] == 0) {
                sum1 += a[i];
            } else {
                sum2 += a[i];
            }
        }

        int diff = max(sum1, sum2) - min(sum1, sum2);
        if (diff < min_diff) {
            min_diff = diff;
        }

        int j = n - 1;
        while (j >= 0) {
            if (b[j] == 1) {
                b[j] = 0;
            } else {
                b[j] = 1;
                break;
            }
            j--;
        }
        if (j < 0) {
            break;
        }
    }

    cout << min_diff;

    return 0;
}
