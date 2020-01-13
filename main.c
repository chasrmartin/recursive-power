#include <stdio.h>
double rpow(double num, int exponent);

int main(int argc, char * argv[]){
    double num;
    int exponent;

    printf( "Enter the base: ");
    scanf(  "%lf", &num);
    printf( "Enter the exponent: ");
    scanf(  "%d", &exponent);
    printf( "%.0lf to the power of %d is: %.0lf\n",
            num, exponent, rpow(num, exponent));
    return 0;
}
