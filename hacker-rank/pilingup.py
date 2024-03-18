import sys


def check_side_lengths(blocks):
    num_blocks = len(blocks)
    mid_idx = num_blocks // 2

    left_idx = 0
    right_idx = num_blocks - 1

    while left_idx < mid_idx < right_idx:
        left, right = blocks[left_idx], blocks[right_idx]

        next_left = blocks[left_idx + 1]
        next_right = blocks[right_idx - 1]

        if (not check_length_choice(left, next_left, next_right)
                or not check_length_choice(right, next_left, next_right)
        ):
            return 'No'

        left_idx += 1
        right_idx -= 1

    return 'Yes'


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
        print(check_side_lengths(blocks))
