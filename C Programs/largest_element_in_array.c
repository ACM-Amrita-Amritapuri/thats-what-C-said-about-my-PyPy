#include <stdio.h>
int main ()   {
int i , arr[10] ;
printf("Enter 10 elements:"); 
for(i=0; i<10; i++)  {
    scanf("%d",&arr[i]);
    }  
        
    //Initialize max with first element of array.    
int max = arr[0];    
    // Length of array is 10 as 10 inputs were asked for it 
    //Loop through the array    
for (int i = 0; i < 10; i++) {     
        //Compare elements of array with max    
    if(arr[i] > max)    
        max = arr[i];    
    }      
printf("Largest element present in given array: %d\n", max);    
return 0;    
}    
