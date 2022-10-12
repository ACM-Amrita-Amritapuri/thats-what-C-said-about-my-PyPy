#include <bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin>>n;
	if(n%2==0){
        for(int i=n;i>0;i--){
            cout<<i<<" ";
        }
	}
    else
        cout<<-1;
}