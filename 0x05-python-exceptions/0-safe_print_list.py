#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in x:
            print("{:d}".format(my_list[i]))
    except:
        print("Cannot print")

    return (x)
