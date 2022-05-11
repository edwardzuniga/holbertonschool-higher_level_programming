#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_element = my_list.copy()
    if idx < 0 or idx > (len(my_list) - 1):
        return new_element
    new_element[idx] = element
    return new_element
