#!/usr/bin/python3
def no_c(my_string):
    myString = ""
    for i in my_string:
        if i == "c" or i == "C":
            continue
        else:
            myString += i
    return myString
