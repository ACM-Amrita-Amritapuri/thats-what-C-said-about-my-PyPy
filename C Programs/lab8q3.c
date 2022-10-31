#include<stdio.h>
int main()
{
 char a[10];
 int b,i;
 printf("enter number of characters in name:");
 scanf("%d",&b);
 printf("enter characters: ");
 for(i=0;i<=b;i++)

 {
  scanf("%s",a);
 }
  a[b]='\0';
  printf("hello");
  for(i=0;i<b+1;i++)
  {

  printf("%c",a[i]);
  }




}

//adrdess of  the first srrsy
