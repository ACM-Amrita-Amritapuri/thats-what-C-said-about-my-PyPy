/*Check if a repeated subsequence is present in a string or not */
#include<stdio.h>
#include<string.h>
int main()
{
	char a[100];
	scanf("%[^\n]s",a);
	int i,j,p=0,k,n;
	n=strlen(a);
	for(i=0;i<n;i++)
	{
		for(j=i+1;j<n;j++)
		{
			for(k=j+1;k<n;k++)
			{
				if(((a[i]==a[j])&&(a[k]==a[i+k]))||((a[i]==a[k])&&(a[j]==a[i+k])))
				{
					p=p+1;
				}
			}
		}
	}
	if(p>=1)
	{
		printf("There is repeated subsequence");
	}
	else
	{
		printf("There is no repeated subsequence");
	}
}