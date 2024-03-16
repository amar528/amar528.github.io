def contains(func_name, s):
    for c in s:
        func = getattr(c, func_name)
        if func():
            return True
    return False


if __name__ == '__main__':
    s = input()

    print(contains(s.isalnum.__name__, s))
    print(contains(s.isalpha.__name__, s))
    print(contains(s.isdigit.__name__, s))
    print(contains(s.islower.__name__, s))
    print(contains(s.isupper.__name__, s))
