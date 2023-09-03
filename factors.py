#!/usr/bin/python3
from sys import argv
import math

def main():
    mod = 2;
    with open(argv[1], encoding="utf-8") as file_:
        for i in file_.readlines():
            num = int(i)
            while (num % mod != 0):
                mod += 1
            print("{}={:d}*{}".format(num, int(num / mod), mod))
            mod = 2

main()
