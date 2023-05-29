#!/usr/bin/python3


def safe_print_division(a, b):
    """
    divides two integers and prints the result
    catches divide by zero exception
    """
    try:
        resu = a / b
    except:
        resu = None
    finally:
        print("Inside result: {}".format(resu))
    return resu
