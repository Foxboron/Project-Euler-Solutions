#!/usr/bin/env python
from math import sqrt

def main():
    n  = 1000
    for a in range(1, 500):
        for b in range(1, 500):
            c = pow(a,2) + pow(b,2)
            c = sqrt(c)
            if pow(a,2) + pow(b,2) == pow(c,2) and a + b + c == n:
                print a*b*c
                break

if __name__ == '__main__':
    main()
