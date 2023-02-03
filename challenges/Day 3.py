#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    
    while 1<= N <= 100:

        if N % 2 == 0 is False:
            print("Weird")
        elif 2<=N<=5:
            print("Not Weird")
        elif 6<=N<=20:
            print("Not Weird")
        else: 
            break