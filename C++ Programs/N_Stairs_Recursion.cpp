#include <iostream>

using namespace std;


int Stair(int n){
  if(n<0)
    return 0;

  if(n==0)
    return 1;

  return Stair(n-2) + Stair(n-1);
}

int main() {
  int n=5;
  cout<<"The Number Is : "<<Stair(n);
  return 0;

}
