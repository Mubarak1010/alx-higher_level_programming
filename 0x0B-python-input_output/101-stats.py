#!/usr/bin/python3
"""module"""


def print(size, status):
    """Prints accumulated metrics.

    Args:
    size (int): the read file size
    status (dict): the count of status code
    """

    print("File size: {}".format(size))
    for key in sorted(status):
        print("{}: {}".format(key, status[key]))

        if __name__ == "__main__":
            import sys

            size = 0
            status = {}
            valid = ['200', '301', '400', '401', '403', '404', '405', '500']
            count = 0

            try:
                for line in sys.stdin:
                    if count == 10:
                        print_stats(size, status)

                        count = 1
                    else:
                        count += 1
                    line = line.split()

                    try:
                        size += int(line[-1])
                    except (IndexError, ValueError):
                        pass

                    try:
                        if status.get(line[-2], -1) == -1:
                            status[line[-2]] = 1
                        else:
                            status[line[-2]] += 1
                    except IndexError:
                        pass
                    print_stats(size, status)

                    except KeyboardInterrupt:
                        print_stats(size, status)
                        raise
