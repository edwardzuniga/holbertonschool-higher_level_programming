#!/usr/bin/python3
for alfabeto in range(97, 123):
    if alfabeto == 101 or alfabeto == 113:
        continue
    print('{:c}'.format(alfabeto), end="")
