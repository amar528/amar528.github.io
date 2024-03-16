commands = {
    'insert': lambda lst, idx, v: lst.insert(idx, v),
    'print': lambda lst: print(lst),
    'remove': lambda lst, v: lst.remove(v),
    'append': lambda lst, v: lst.append(v),
    'sort': lambda lst: lst.sort(),
    'pop': lambda lst: lst.pop(),
    'reverse': lambda lst: lst.reverse()
}

if __name__ == '__main__':

    a = []

    n = int(input())

    for i in range(n):
        line = input().split()
        num_args = len(line)
        cmd = line[0]
        f = commands.get(cmd, None)

        if not f:
            raise RuntimeError(f'Unknown command {cmd}')

        if num_args > 1:
            args = [a]
            varargs = line[1:]
            args.extend(list(map(int, varargs)))
            f(*args)
        else:
            f(a)
