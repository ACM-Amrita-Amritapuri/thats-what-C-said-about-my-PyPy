#include <stdio.h>
void read_array(int *a,int n)
{
    int i;
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
}
void print_array(int *a,int n)
{
    int i;
    for(i=0;i<n;i++)
        printf("%d ",a[i]);
    printf("\n");
}
void find_small(int *a,int n,int pos)
{
    int i,small=a[0];
    for(i=1;i<n;i++)
        if(a[i]<small)
            {
                small=a[i];
                pos=i+1;
            }
    printf("num:%d\nind:%d",small,pos);
}
int main()
{
    int a[10],n,pos;
    printf("Enter the number of elements: ");
    scanf("%d",&n);
    read_array(a,n);
    print_array(a,n);
    find_small(a,n,pos);
    return 0;
}
