//WAP to declare an array of size 5 AND PRINT IT.

#include<stdio.h>
int main()
{
    int a[5],i;
    for(i=0;i<=4;i++)
    {
        printf("enter  number %d",i+1);

        scanf("%d",&a[i]);
    }
    for(i=0;i<=4;i++)
    {
        printf("%d\t",a[i]);
    }

}
