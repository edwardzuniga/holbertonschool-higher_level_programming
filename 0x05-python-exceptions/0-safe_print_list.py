#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cont = 0
    for index in my_list[:x]:
        try:
            print(index, end='')
            cont = cont + 1
        except IndexError:
            break
    print()
    return cont
