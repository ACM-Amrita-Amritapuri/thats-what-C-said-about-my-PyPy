/*Find the minimum number possible by doing at-most k swaps*/
#include<stdio.h>
#include<string.h>
int main()
{
	char num[100],temp=' ';
	printf("Enter the number:\n");
	scanf("%[^\n]s",num);
	int i,j,n,k,v=0,l;
	k=strlen(num);
	printf("Enter number of swaps:\n");
	scanf("%d",&n);
	for(i=0;i<k;i++)
	{
		v=i;
		l=num[i];
		for(j=i;j<k;j++)
		{
			if(l>num[j])
			{
				l=num[j];
				v=j;
			}
		}
		if(n!=0&&v!=i)
		{
			temp=num[v];
			num[v]=num[i];
			num[i]=temp;
			n=n-1;
		}
	}
	printf("%s",num);
}