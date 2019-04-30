#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        i = ord(ch)
        print("{:c}".format(i - 32 if 97 <= i <= 122 else i), end="")
    print()
