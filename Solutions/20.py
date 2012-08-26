#!/usr/bin/env

def main(n):
    listvar = []
    for i in range(1, n+1):
        listvar.append(i)
    num = 1
    for i in listvar:
        num *= i
    sumlist = [int(i) for i in str(num)]
    return sum(sumlist)

if __name__ == '__main__':
    print main(100)
