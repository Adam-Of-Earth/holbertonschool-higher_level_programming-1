#!/usr/bin/python3
for i in range(26):
    if i == 4 or i == 16:
        print("", end="")
    else:
        print(chr(97 + i), end="")
