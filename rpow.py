#!/usr/bin/env python -*-coding:utf-8-*-
""" rpow.py -- compute x^n in O(n) time """

def power(x:float, n:int)-> float:
    """Compute the exponent recursively in O(n) time.

    This is taking the easy way out; observe that

        x^n = x * x(n-1)
        x^0 = 1
    """
    if n == 0:
        return 1
    return x * power(x,n-1)

if __name__ == "__main__":
    print("Compute x^n recursively the easy O(n) way")
    x = float(input("Enter the base x: "))
    n = int(input("Enter the exponent n: "))
    print(f"{int(x)}^{n} = {int(power(x,n))}")
    print("Done.")
          
