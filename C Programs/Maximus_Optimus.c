#include <stdio.h>
#include <math.h>
int main () {
    int a , b , c  ;
scanf("%d %d %d", &a , &b , &c);
int n ;
scanf("%d", &n);
int sum1 = 0, sum2 = 0, sum3 = 0;
for (int i = 0 ; i >= n ; i++) {
    if (a > b && a > c){
        for (int j = 0 ; j >= b ; j--){
            sum1 = sum1 + j ;
        }
    }
    
    else if (b > c && b > a) {
            for ( int k = 0 ; k >= n ; k--) {
                 sum2 = sum2 + k ;
            }
           
        }
        
    else if (c > b && c > a){
            for (int l = 0 ; l>= c ; l--) {
            sum3 = sum3 + l ;
            }
        }
    }
max(sum1 , sum2) , max (sum1, sum3) , max(sum2,sum3) ;

    printf("%d", sum);
    return 0 ;
}    