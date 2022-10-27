#include <iostream>
#include<conio.h>

using namespace std;

#define arr 5
 
int main()
{
    int numbers[arr], i ,j ,temp;

	cout<<"Simple C++ Example Program for Sorting (Asending Order) In Array\n";

	
    for (i = 0; i < arr; i++)
    {
		cout<<"Enter the Number : "<< (i+1) <<"  : ";
        cin>>numbers[i];
    }
        
    
    for (i = 0; i < arr; ++i)
    {
        for (j = i + 1; j < arr; ++j)
        {
            if (numbers[i] > numbers[j])
            {
                temp =  numbers[i];
                numbers[i] = numbers[j];
                numbers[j] = temp;
            }
        }
    }
    
    cout<<"Sorting Order Array: \n";
    for (i = 0; i < arr; ++i)
        cout<<numbers[i]<<endl;
        
	getch();
    return 0;
}



