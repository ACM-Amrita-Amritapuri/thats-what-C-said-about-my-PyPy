#include<iostream>
using namespace std;

int main()
{
	int i, j, r, c, sum;
	
	cout << "\nPlease Enter the Matrix rows and Columns =  ";
	cin >> i >> j;
	
	int sumRCArray[i][j];
	
	cout << "\nPlease Enter the Matrix Items =  ";
	for(rows = 0; r < i; r++)	{
		for(c = 0; c < i; c++) {
			cin >> s[rows][c];
		}		
	}
	
	for(rows = 0; rows < i; rows++)
  	{
  		sum = 0;
  		for(c = 0; c < j; c++)
  		{
  			sum = sum + s[rows][c];
		}
   		cout << "\nThe Sum of Items in " << rows + 1<< " Row of a Matrix = " << sum ;
  	}

 	for(r = 0; r < i; r++)
  	{
  		sum = 0;
  		for(c= 0; c< j; c++)
  		{
  			sum = sum + s[c][r];
		}
   		cout << "\nThe Sum of Items in Column of a Matrix = " << sum ;
  	}  	

 	return 0;
}

