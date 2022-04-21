#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def getMedian(count,d):
    median = 0
    if d%2==0:
        first = d//2
        second = d//2+1
        freq=0
        for i in range(201):
            freq=freq+count[i]
            if freq>=first:
                first=i
                break

        freq=0
        for i in range(201):
            freq=freq+count[i]
            if freq>=second:
                second=i
                break
                
        #print("Case 1",count, first,second)
        return (first+second)/2
    else:
        first = d//2+1
        freq=0
        for i in range(201):
            freq=freq+count[i]
            if freq>=first:
                #print("Case 2",count)
                return i      


def activityNotifications(expenditure, d):
    # Write your code here
    count = [0 for i in range(201)]
    for i in range(d):
        count[expenditure[i]]=count[expenditure[i]]+1
    
    result = 0
    for i in range(d,len(expenditure)):
        if expenditure[i]>=2*getMedian(count,d):
            a = [x for x in expenditure[i-d:i]]
            a.sort()
            #print("Found:",i,a,getMedian(count,d))
            result=result+1
        count[expenditure[i-d]]=count[expenditure[i-d]]-1
        count[expenditure[i]]=count[expenditure[i]]+1
    return result


if __name__ == '__main__':
    f = open("data.txt")

    first_multiple_input = f.readline().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, f.readline().split()))

    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')

    f.close()
