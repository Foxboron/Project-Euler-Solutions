#!/usr/bin/env python


def main():
    a = 1
    b = 2
    listnum = []
    listsum = []
    while True:
        listnum.append(a)
        a, b = b, a + b
        if a >= 4000000:
            break
    for i in listnum:
        if i % 2 == 0:
            listsum.append(i)
    print "Answer: %s" % (sum(listsum))

if __name__ == '__main__':
    main()
