#!/usr/bin/python3
def safe_print_division(a, b):
    totality = 0
    try:    
        totality = a / b
        return totality
    except ZeroDivisionError:
        totality = None
        return totality
    finally:
        print("Inside result: {}".format(totality))
