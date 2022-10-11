#include <stdio.h>
typedef struct complex {
    float real;
    float imag;
} complex;
void add(complex *n1, complex *n2,complex *result) {
    result->real = n1->real + n2->real;
    result->imag = n1->imag + n2->imag;
}
int main() {
    complex n1, n2, result;
    printf("For 1st complex number ==>\n");
    printf("Enter the real and imaginary parts: ");
    scanf("%f %f", &n1.real, &n1.imag);
    printf("\nFor 2nd complex number ==> \n");
    printf("Enter the real and imaginary parts: ");
    scanf("%f %f", &n2.real, &n2.imag);
    printf("\n");
    add(&n1,& n2,&result);
    printf("Sum = %.1f + %.1fi", result.real, result.imag);
    return 0;
}
