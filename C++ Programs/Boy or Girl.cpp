#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;



int main() {
    string arr;
    cin>>arr;
    int count=0;
    sort(arr.begin(),arr.end());
    for(int i=0;i<arr.size();i++){
        if(arr[i]!=arr[i+1]){
            count++;
        }
    }
    if(count%2==0){
        cout<<"CHAT WITH HER!";
    }
    else{cout<<"IGNORE HIM!";}
    return 0;
}