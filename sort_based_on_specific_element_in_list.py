# sort_based_on_specific_element_in_list
# https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr = sorted(arr,key=lambda x:x[k])
    for i in range(n):
        for j in range(m):
            print(arr[i][j],end=" ")
        print()
