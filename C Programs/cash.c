#include <stdio.h>
#include <math.h>

int main()
{
    int r,cents;
    float dollars;

    while(cents<=0)
    {
        printf("Enter change owed: ");
        scanf("%f",&dollars);
        r= (int)dollars;
        dollars-=r;
        cents = round(dollars * 100);
    }
    
    int quarters = cents / 25;
    int dimes = (cents % 25) / 10;
    int nickels = ((cents % 25) % 10) / 5;
    int pennies = ((cents % 25) % 10) % 5;

    printf("%d \n", quarters + dimes + nickels + pennies);
}