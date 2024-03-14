def do_sets():
    a_spaces = input().split()
    n = int(input())

    input_sets = []
    for i in range(n):
        input_sets.append(input().split())

    set_a = set(a_spaces)
    sets_other = []
    for input_set in input_sets:
        sets_other.append(set(input_set))

    for subset in sets_other:
        if not set_a.issuperset(subset):
            return False

    return True


if __name__ == '__main__':
    print(do_sets())