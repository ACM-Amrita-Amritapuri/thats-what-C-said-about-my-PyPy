#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin>>n;
    string word;
    int ans=0;
    int size,q;
    int flag=0;
    for(int i=0;i<n;i++){
        size=0;
        flag=0;
        cin>>word;
        size=word.size();
        q=size;
        if(size==1){
            ans+=1;
            continue;
        }
        
        else{
           
            for(int o=0;o<size;o++){
                q=q-1;
                if(word[o]==word[q]){
                    flag=1;
                }
                else{
                    flag=0;
                    break;
                }
                
            }
            
        }
        if(flag==1){ans=ans+size;}
    }
    cout<<ans;
    return 0;
}
