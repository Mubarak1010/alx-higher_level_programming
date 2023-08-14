#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    index = len(my_list)
    if idx < 0 or idx > index - 1:
        return my_list
    else:
        new_list = [x for x in my_list]
        new_list[idx] = element
        return new_list
