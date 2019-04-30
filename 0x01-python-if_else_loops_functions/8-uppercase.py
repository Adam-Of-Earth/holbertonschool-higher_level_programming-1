#!/usr/bin/python3
def uppercase(str):
    g = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            x = ord(i) - 32
            y = chr(x)
            g = g + y
        else:
            j = i
            g = g + j
    print(g)
