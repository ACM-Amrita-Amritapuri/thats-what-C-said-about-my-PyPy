#include <stdio.h>
int main()
{
	int m,n,i,j,x,y,temp;
	printf("enter no of rows of matrix: ");
	scanf("%d",&m);
	printf("enter no of columns of matrix: ");
	scanf("%d",&n);
	int a[m][n];
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("element a[%d][%d]: ",i,j);
			scanf("%d",&a[i][j]);
		}
	}
	printf("interchange row:");
	scanf("%d %d",&x,&y);
	for(j=0;j<n;j++)
	{
		temp=a[x][j];
		a[x][j]=a[y][j];
		a[y][j]=temp;
	}
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("%d\t",a[i][j]);
		}
		printf("\n");
	}
	printf("interchange column:");
	scanf("%d %d",&x,&y);
	for(j=0;j<m;j++)
	{
		temp=a[j][x];
		a[j][x]=a[j][y];
		a[j][y]=temp;
	}
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("%d\t",a[i][j]);
		}
		printf("\n");
	}
return 0;
}
