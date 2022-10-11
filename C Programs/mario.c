#include<stdio.h>

int main()
{

printf("Enter the height of the pyramid : \n");
int h;
scanf("%d", &h);
int f=h;
for(int i=0;i<=h;++i)
{ 
    for(int j=0;j<f;++j)
    {
        printf(" "); 
    }
    for(int k=0;k<i;++k)
    {
        printf("#");
    }
    f--;
    printf("\n");
}
}