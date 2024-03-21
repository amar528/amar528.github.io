#!/bin/python3


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    mx = count = 0

    for c in candles:
        if c > mx:
            mx = c
            count = 1
        elif c == mx:
            count += 1

    return count


if __name__ == '__main__':
    candles_count = int(input())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(str(result) + '\n')
