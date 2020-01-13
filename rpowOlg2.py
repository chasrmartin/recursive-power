#!/usr/bin/env python -*-coding:utf-8-*-
""" rpow.py -- compute x^n in O(lg n) time """

def even_p(n:int)-> bool:
    """Return True if n is even, otherwise False
    uses a trick with bitwise operations to make the test quick.

    Just for swank, nrmally I'd just return (n%2)==0.
    """
    return not (n&1)

def power(x:float, n:int)-> float:
    """Compute the exponent in O(lg n) time.

    The trick here is that for even n, x^n = x^(n//2)**2, which can be
    proven using associativity fo multiplication.  For odd n, n-1 is
    guaranteed to be even, so it reduces to x * x^{n-1}. And since
    we're using Python3 integer division (//), we can test for when
    n==0, and of course x*0 is 1.

    To show time is O(lg n), simply observe that for any n, you can
    repeatedly divide n by 2 log_2 times.

    """
    if n == 0: return 1
    if even_p(n):
        return power(x,n//2)**2
    else:
        return x * power(x,n-1)

if __name__ == "__main__":
    print("Compute x^n")
    x = float(input("Enter the base x: "))
    n = int(input("Enter the exponent n: "))
    print(f"{int(x)}^{n} = {int(power(x,n))}")
    print("Done.")
          
