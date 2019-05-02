#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv
    a = argv[1]
    b = argv[3]
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] == "+":
        print("{} + {} = {}".format(a, b, add(int(a), int(b))))
    elif argv[2] == "-":
        print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
    elif argv[2] == "*":
        print("{} * {} = {}".format(a, b, sub(int(a), int(b))))
    elif argv[2] == "/":
        print("{} / {} = {}".format(a, b, sub(int(a), int(b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
