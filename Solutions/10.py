#!/usr/bin/env python


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    listvar = []
    for i in range(1, 2000001):
        if isPrime(i):
            listvar.append(i)
    print sum(listvar)

if __name__ == '__main__':
    main()
