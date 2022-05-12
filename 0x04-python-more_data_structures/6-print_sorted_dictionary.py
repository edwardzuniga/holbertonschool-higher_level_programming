#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_order = sorted(a_dictionary)
    for i in new_order:
        print("{}: {}".format(i, a_dictionary[i]))
