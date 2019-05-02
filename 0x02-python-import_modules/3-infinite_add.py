#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    count = 0
    for i in range(1, len(argv)):
        count += int(argv[i])
    print(count)
