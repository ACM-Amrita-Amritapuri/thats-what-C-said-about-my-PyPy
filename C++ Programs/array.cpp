 
#include <bits/stdc++.h>
using namespace std;
 
bool checkArr(int arr1[], int arr2[],
                 int n, int m)
{
    if (n != m)
        return false;
 
    sort(arr1, arr1 + n);
    sort(arr2, arr2 + m);
 
    for (int i = 0; i < n; i++)
        if (arr1[i] != arr2[i])
            return false;
 
    return true;
}
 
int main()
{
    int arr1[] = { 1, 2, 3, 4, 5 };
    int arr2[] = { 5, 4, 3, 2, 1 };
    int N = sizeof(arr1) / sizeof(int);
    int M = sizeof(arr2) / sizeof(int);
 
    if (checkArr(arr1, arr2, N, M))
        cout << "Equal";
    else
        cout << "Not Equal";
    return 0;
}