#!/usr/bin/env python


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def main():
    prime = 0
    count = 0
    number = 1
    while True:
        if isPrime(number) == True:
            prime = number
            count += 1
        number += 1
        if count >= 10001:
            return prime


if __name__ == '__main__':
    print main()
