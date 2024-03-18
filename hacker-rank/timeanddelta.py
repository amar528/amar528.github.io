#!/bin/python3
import datetime
import os
import time

# Sun 10 May 2015 13:54:36 - 0700
FORMAT = '%a %d %b %Y %H:%M:%S - %z'


# Complete the time_delta function below.
def time_delta(t1, t2):
    t1_strip = time.strptime(t1, FORMAT)
    t2_strip = time.strptime(t2, FORMAT)

    t1_offset = t1_strip.tm_gmtoff

    return 0


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta + '\n')
