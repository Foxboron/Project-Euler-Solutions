#!/usr/bin/env python


def main():
    a = 1
    b = 2
    listsum = []
    while True:
        a, b = b, a + b
        if a >= 4000000:
            break
        if a % 2 == 0:
            listsum.append(a)
    print "Answer: %s" % (sum(listsum))

if __name__ == '__main__':
    main()
