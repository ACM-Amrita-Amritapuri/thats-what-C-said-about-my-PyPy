#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int tests,inp;
    cin>>tests;
    
    for(int i=0;i<tests;i++){
        
        int size;
        cin>>size;
        
        vector <int> array;
        
        for(int j=0;j<size;j++){
            cin>>inp;
            array.push_back(inp);
        }
        
        int h=0;
        for(int g=0;g<size;g++){
        h=g;
        while (h!=size){
            for(int j=g;j<=h;j++){
                cout<<array[j]<<" ";
            }
            cout<<endl;
            h=h+1;
        }
       }
    }
    return 0;
}
