#!/usr/bin/python3
def no_c(my_string):
    remov = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            remov += char
            return remov
