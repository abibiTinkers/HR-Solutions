#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    ltrs = set(list(s))
    counts = {char: 0 for char in ltrs}
    
    for char in s:
        counts[char] +=1
        
    top_three = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:3]
    
    for i in range(3):
        print(f"{top_three[i][0]} {top_three[i][1]}")
