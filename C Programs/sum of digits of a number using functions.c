#include <stdio.h>
int demo();
int main()
{
		int result;
		result=demo();
		printf("The value returned by sum is %d",result);
		return 0;
}
int demo()
{
		int a,sum=0;
		printf("Enter a number:");
		scanf("%d",&a);
		while(a!=0)
		{
		sum=sum+(a%10);
		a=a/10;
		}
		return sum;
}

