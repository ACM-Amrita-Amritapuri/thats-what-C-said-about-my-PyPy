//Converts number from hexadecimal to decimal

#include <stdio.h>
#include <string.h>
#include <math.h>
 
int main()
{
    char hex[32];
    int  deci,i,count,dig;   
    printf("Enter Hexadecimal value: ");
    scanf("%s",hex);
    count=0;
    deci=0;
    for(i=(strlen(hex)-1);i>=0;i--)
    {
        switch(hex[i])                       
        {
            case 'A':
                dig=10; 
                break;
            case 'B':
                dig=11; 
                break;
            case 'C':
                dig=12; 
                break;
            case 'D':
                dig=13; 
                break;
            case 'E':
                dig=14; 
                break;
            case 'F':
                dig=15; 
                break;
            default:
                dig=hex[i]-48;
        }
        deci= deci+ (dig)*pow((double)16,(double)count);
        count++;
    }
 
    printf("Decimal value is: %d",deci);
    return 0;
}
J
