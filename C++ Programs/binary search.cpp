#include <bits/stdc++.h>
using namespace std;
int search(int key,int l,int r,vector<int> lst){
    int mid=int((r+l-1)/2);
    if(key==lst[mid])
        return (mid);
    else if(key<lst[mid])
        return search(key,l,mid-1,lst);
    else if(key<lst[mid])
        return search(key,mid+1,r,lst);
    return -1;
}
int main(){
    vector<int> a{12,32,41,56,69,73};
    int l =a.size();
    cout<<"element found at index: "<<search(41,0,l-1,a);
}