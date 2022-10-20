/*TRIANGLE*/
#include <stdio.h>
#include <math.h>        /*for sqrt and pow function*/
int main()
{
	  float x1,x2,x3,y1,y2,y3,a,b,c,s,Area,circ;
	  printf("Enter coordinates x1,y1 : ");
	  scanf("%f%f",&x1,&y1);
	  printf("Enter coordinates x2,y2 : ");
	  scanf("%f%f",&x2,&y2);
	  printf("Enter coordinates x3,y3 : ");
	  scanf("%f%f",&x3,&y3);
	  a =sqrt(pow((x1-x2),2)+pow((y1-y2),2));
	  b =sqrt(pow((x2-x3),2)+pow((y2-y3),2));
	  c =sqrt(pow((x3-x1),2)+pow((y3-y1),2));
	  circ = a+b+c;
	  s = (a+b+c)/2;
	  Area = sqrt(s*(s-a)*(s-b)*(s-c));
	  printf("LENGTHS:\n Side 1=%f \n Side 2=%f\n Side 3=%f",a,b,c);
	  printf("\nCircumference of triangle = %f",circ);
	  printf("\nArea of triangle = %f",Area);
	  return 0;
}

