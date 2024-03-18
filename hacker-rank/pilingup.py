import sys
from collections import deque


def check_side_lengths(blocks):
    d = deque(blocks)

    stacked = []

    # Choose left until 1 element remains, and it is >= the next choice to the right
    while len(d) > 1 and d[0] >= d[1]:
        stacked.append(d.popleft())

    # Choose right until 1 element remains, and it is >= the next choice to the left
    while len(d) > 1 and d[-1] >= d[-2]:
        stacked.append(d.pop())

    # if we have a single element left, we have stacked all the boxes
    if len(d) <= 1:
        print('Yes')
    else:
        print('No')


def check_length_choice(choice, next_left, next_right):
    return choice > next_left and choice > next_right


if __name__ == '__main__':

    t = int(input())
    blocks_list = []
    for _ in range(t):
        n = int(input())
        blocks_line = list(map(int, input().split()))
        if len(blocks_line) != n:
            print('Invalid number of side lengths')
            sys.exit(1)

        blocks_list.append(blocks_line)

    for blocks in blocks_list:
        check_side_lengths(blocks)
