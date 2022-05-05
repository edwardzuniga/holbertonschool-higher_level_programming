#!/usr/bin/python3.4
if __name__ == "__main__":
    from sys import argv

if len(argv) == 1:
    print("0 arguments.")
if len (argv) == 2:
    print("1 argument:")
    print("1 {:s}".format(argv[1]))

elif len(argv) > 2:

    print("{:d} arguemnts:".format(len(argv) -1))
    for i in range (1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))
