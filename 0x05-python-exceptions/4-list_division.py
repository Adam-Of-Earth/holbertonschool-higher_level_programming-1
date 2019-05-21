#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    index = 0
    newList = []
    while index < list_length:
        quot = 0
        try:
            quot = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            newList.append(quot)
            index += 1
    return newList
