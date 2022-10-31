#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void PrintArray(int arr[], int n){
  for(int i=0; i<n; i++){
    cout<<" "<<arr[i];
  }
}

void MoveZeros(int arr[],int n){
    int nonZero = 0;
    for(int i=0; i<n;i++){
      if(arr[i]!=0){
        swap(arr[i], arr[nonZero]);
        nonZero++;
      }
    }
  }


int main() {
  int arr[] = {0,1,0,3,12};
  int n = sizeof(arr)/sizeof(arr[0]);
    MoveZeros(arr, n);
    PrintArray(arr, n);
  return 0;
}
