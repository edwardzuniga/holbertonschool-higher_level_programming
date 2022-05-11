#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        pass
    elif idx >= 0 and idx < len(my_list):
        copi = my_list
        copi[idx] = element
        return copi
    else:
        return my_list
