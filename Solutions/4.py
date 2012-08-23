#!/usr/bin/env python


def main():
    stranswer = 0
    for i in range(1, 1000):
        for x in range(1, 1000):
            answer = i * x
            answer_rev = int(str(answer)[::-1])
            if str(answer_rev) == str(answer):
                if answer > stranswer:
                    stranswer = answer
    print stranswer

if __name__ == '__main__':
    main()
