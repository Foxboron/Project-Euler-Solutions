#!/usr/bin/env

def main(n, e):
    num = pow(n,e)
    listvar = [int(i) for i in str(num)]
    print sum(listvar)

if __name__ == '__main__':
    main(2, 1000)
