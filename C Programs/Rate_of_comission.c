// rate of commisson ques
#include <stdio.h>
int main () {
    int n ;
    printf("The sales amount is :",n);
    scanf(" %d", &n);
    if (n <= 10000) {
        printf("Commission rate is 2  percent ");
    }
    else if (n > 10000 && n <= 20000) {
        printf("Commission rate is 3  percent ");
    }
    else if (n > 20000 && n <= 50000) {
        printf("Commission rate is 5 percent ");
    }
    else if (n > 50000 && n <= 70000){
        printf("Commission rate is 9 percent");
    }
    else if (n > 70000) {
        printf("Commission rate is 12 percent");
    }
    return 0;
}
