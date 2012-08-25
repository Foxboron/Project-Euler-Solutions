#!/usr/bin/env pyton


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
    num = 600851475143
    listnum = []
    divnum = 2
    run = True
    while run or num == 0:
        if isPrime(divnum):
            if num % divnum == 0:
                num = num / divnum
                if isPrime(num):
                    listnum.append(num)
                    run = False
                listnum.append(divnum)
        divnum += 1
    print max(listnum)


if __name__ == '__main__':
    main()
