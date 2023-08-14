#!/usr/bin/python3
def element_at(my_list, idx):
    index = len(my_list)
    if idx < 0:
        return None
    elif idx > (index - 1):
        return None
    else:
        return my_list[idx]
