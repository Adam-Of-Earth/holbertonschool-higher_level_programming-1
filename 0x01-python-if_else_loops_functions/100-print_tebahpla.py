#!/usr/bin/python3
for i in range(-122, -96):
    print("{:c}".format(abs(i) - 32 if abs(i) % 2 != 0 else abs(i)), end="")
