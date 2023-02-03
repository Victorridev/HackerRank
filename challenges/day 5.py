#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    te10 = 10
    n_tabuada = [i for i in range(1,te10)]
    

for i in n_tabuada:
    resultado = n * i
    print("{} x {} = {}".format(n , i , resultado))
