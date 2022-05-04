#!/usr/bin/python3
for num in range(0, 100):
    digito1 = num / 10
    digito2 = num % 10
    if num == 89:
        print('{:d}'.format(num))
    elif digito1 < digito2:
        print('{:02d}'.format(num), end=", ")
