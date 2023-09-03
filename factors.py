#!/usr/bin/python3
from sys import argv
import math

def main():
    with open(argv[1], encoding="utf-8") as file_:
        for i in file_.readlines():
            num = int(i)
            mod = 2
            if(num % mod == 0):
                print("{}={}*{}".format(num, int(num / mod), mod))
            else:
                sqrt_ = int(math.sqrt(num)) + 1
                for mod in range(3, sqrt_, 2):
                    if(num % mod == 0):
                        print("{}={}*{}".format(num, int(num / mod), mod))
                        break
                    if(num % (sqrt_ + mod) == 0):
                            print("{}={}*{}".format(num, int(num / (sqrt_ + mod)), sqrt_ + mod))
                            break
                    if(num % (sqrt_ - mod) == 0):
                        print("{}={}*{}".format(num, int(num / (sqrt_ - mod)), sqrt_ - mod))
                        break
main()
