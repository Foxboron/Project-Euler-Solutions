#!/usr/bin/env python


def main():
    num = 0
    answer = 0
    ints = [i for i in range(1, 21)]
    while True:
        for i in ints:
            if num % i == 0:
                answer = num
            else:
                answer = 0
                break
        if answer == 0:
            num += 1
            continue
        else:
            print "Answer is: %s" % answer
            break

if __name__ == '__main__':
    main()
