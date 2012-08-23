#!/usr/bin/env python


def main():
    numlist = []
    for i in range(1, 1000):
        #print i
        if i % 3 == 0:
            numlist.append(i)
        if i % 5 == 0:
            numlist.append(i)
    print "%s" % (sum(numlist))

if __name__ == '__main__':
    main()
