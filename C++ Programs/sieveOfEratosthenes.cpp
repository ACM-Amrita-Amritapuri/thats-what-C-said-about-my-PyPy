#include <iostream>

using namespace std;

bool isPrime[100001];

void sieveOfEratosthenes(int n) {
    for (int  i = 0; i <= n; i++) {
        isPrime[i] = true;
    }
    for (int i = 2; i <= n/2; i++) {
        if (isPrime[i]) {
            for (int j = i * 2; j <= n; j = j + i) {
                isPrime[j] = false;
            }
        }
    }
}
int main() {
    int n;
    cin >> n;
    sieveOfEratosthenes(n);
    for (int i = 2; i < n; i ++) {
        if (isPrime[i]) {
            cout << i << "\n";
        }
    }
}