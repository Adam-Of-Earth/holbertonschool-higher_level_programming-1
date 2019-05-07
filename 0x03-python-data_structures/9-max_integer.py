#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return
    else:
        x = 0
        for i in my_list:
            if i is None:
                return
            if i > x:
                x = i
        return x
