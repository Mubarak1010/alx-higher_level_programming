#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    index = len(my_list)
    num = index - 1
    for i in range(index):
        print("{:d}".format(my_list[num]))
        num = num - 1
