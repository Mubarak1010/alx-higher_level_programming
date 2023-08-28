#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    j = 0
    for i in my_list:
        count = count + 1

    try:
        if x < count or x == count:
            for j in range(x):
                print("{:d}".format(my_list[j]), end="")

    except IndexError:
        print("list index out of range")

    print()
    return (x)
