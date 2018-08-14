#!/usr/bin/python

"""

Boilerplate code that takes integer input from a user. Will I ever use this?

"""


def main():
    try:
        numberOfElements=int(raw_input())
    except ValueError:
        print "Enter an integer"

if __name__=="__main__":
    main()