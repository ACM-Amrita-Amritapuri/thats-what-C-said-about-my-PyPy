#include<stdio.h>
int main()
{
	int s;
	scanf("%d",&s);
	int a[s],i,j,temp;
	for(i=0;i<s;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<s;i++)
	{
		for(j=0;j<s-i-1;j++)
		{
			if(a[j]>a[j+1])
			{
				temp=a[j];
				a[j]=a[j+1];
				a[j+1]=temp;
			}
		}
	}
	for(i=0;i<s;i++)
	{
		printf("%d ",a[i]);
	}
	return 0;
}
