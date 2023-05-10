#!/usr/bin/python3
for d in range(0, 10):
    for e in range((d+1), 10):
        if (d != 8) or (e != 9):
            print("{}{}, ".format(d, e), end="")
        else:
            print("{}{}".format(d, e))
