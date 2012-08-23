#!/usr/bin/env python


def main():
    sum1 = 0
    sum2 = 0
    natnum = [i for i in range(1, 101)]
    for i in natnum:
        sum1 += i * i
    for i in natnum:
        sum2 += i ^ 2
    print "Answer: %s" % ((sum2 * sum2) - sum1)

if __name__ == '__main__':
    main()
