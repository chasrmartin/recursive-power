double rpow(double num, int exponent){
    double temp;
    if (exponent == 0)
        return 1;
    if (exponent == 1)
        return num;
    if ((exponent % 2) == 0){
        temp = rpow(num, exponent/2);
        return temp * temp;
    } else {
        return num * rpow(num, exponent-1);
    }
            
}
