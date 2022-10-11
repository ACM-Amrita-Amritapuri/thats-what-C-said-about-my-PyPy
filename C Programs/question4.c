/*Replacing all occurrences of 0 that are not surrounded by 1 in a binary matrix */
#include<stdio.h>	
int main()
{
	int m,n;
	printf("Enter m,n:\n");
	scanf("%d %d",&m,&n);
	int a[m][n],i,j,b[m][n];
	printf("enter the elements to matrix:\n");
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&a[i][j]);
			b[i][j]=a[i][j];
		}
	}
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			if((i==0||j==0||i==m-1||j==n-1))
			{
				b[i][j]=1;
			}
			else if((a[i][j]==0)&&(a[i-1][j]==1)&&(a[i+1][j]==1)&&(a[i][j-1]==1)&&(a[i][j+1]==1))
			{
				b[i][j]=0;
			}
			else
			{
				b[i][j]=1;
			}
		}
	}
	printf("matrix after changing:\n");
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("%d ",b[i][j]);
		}
		printf("\n");
	}
}