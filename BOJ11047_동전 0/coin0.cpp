#include<iostream>
using namespace std;

int main() {
    int n, k, ans = 0;
    scanf("%d %d", &n, &k);
    int* a = new int[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    for (int j = n - 1; j >= 0; j--) {
        if (k < a[j])
            continue;
        else {
            ans += (k / a[j]);
            k %= a[j];
            if (k == 0)
                break;
        }
    }
    printf("%d", ans);
    delete a;
    return 0;
}