double rpow(double num, int exponent){
    if (exponent == 0)
        return 1;
    if (exponent == 1)
        return num;
    return num * rpow(num, exponent - 1);
}
