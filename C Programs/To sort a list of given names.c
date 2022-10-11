#include <stdio.h>
#include <string.h>
int main()
{
	int n;
	char str[100][100],temp[100];
	printf("Enter number of names :\n");
	scanf("%d",&n);
	printf("Enter names in any order:\n");
	for(int i=0;i<n;i++)
	{
		scanf("%s",str[i]);
	}
	for(int i=0;i<n;i++)
	{
		for(int j=i+1;j<n;j++)
		{
			if(strcmp(str[i],str[j])>0)
			{
				strcpy(temp,str[i]);
				strcpy(str[i],str[j]);
				strcpy(str[j],temp);
			}
		}
	}
	printf("\nThe sorted order of names are:\n");
	for(int i=0;i<n;i++)
	{
		printf("%s ",str[i]);
	}
	return 0;
}
