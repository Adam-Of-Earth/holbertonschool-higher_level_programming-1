#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for i in my_list:
        try:
            if a < x:
                print(i, end="")
                a += 1
        except IndexError:
            pass
    print()
    return a
