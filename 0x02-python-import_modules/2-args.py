#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    index = len(sys.argv)
    if index > 1:
        if index == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(index - 1))

        for i in range(1, index):
            print("{}: {}".format(i, sys.argv[i]))

    else:
        print("0 arguments.")
