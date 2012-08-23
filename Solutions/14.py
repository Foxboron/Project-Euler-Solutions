#!/usr/bin/env Python

num = 0
chain = []
for n in range(1, 14):
    a = n
    l = []
    while True:
        if a == 1:
            if len(l) > len(chain):
                chain = l
                num = n
            break
        elif a % 2 == 0:
            a = a / 2
            l.append(a)
        elif a % 2 == 1:
            a = 3 * a + 1
            l.append(a)
print num
print chain
