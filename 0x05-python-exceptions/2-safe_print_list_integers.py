#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ret, index = 0, 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
        except (TypeError, ValueError):
            pass
        else:
            ret += 1
        finally:
            index += 1
    print()
    return ret
