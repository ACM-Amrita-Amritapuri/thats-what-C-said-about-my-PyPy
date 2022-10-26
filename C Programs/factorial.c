//Factorial

#include<stdio.h>

int main() 
{
  int i,n,*p;    
  int fact = 1;
  printf("Enter a number n: ",n);
  scanf("%d",&n);
  p = &n;
  for (i=1;i<=*p;i++)
	{
		fact = fact*i;
	}
	printf("Factorial of %d is %d.",*p,fact);
	return 0;
}
