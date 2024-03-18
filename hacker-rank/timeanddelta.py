#!/bin/python3
import time
import datetime

# Sun 10 May 2015 13:54:36 - 0700
FORMAT = '%a %d %b %Y %H:%M:%S %z'


# Complete the time_delta function below.
def time_delta(t1, t2):
    t1_strip = time.strptime(t1, FORMAT)
    t2_strip = time.strptime(t2, FORMAT)

    t1_off = t1_strip.tm_gmtoff
    t2_off = t2_strip.tm_gmtoff

    t1_secs = time.mktime(t1_strip) - t1_off
    t2_secs = time.mktime(t2_strip) - t2_off

    return str(int(abs(t1_secs - t2_secs)))


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)
