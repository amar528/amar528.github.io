cube = lambda x: x * x * x

fib = [0] * 50
cache = {0: 0, 1: 1}


def fib_recurse(i):
    if i > 50:
        raise RuntimeError('Inout must not exceed 50')

    if i in cache:
        fib[i] = cache[i]
        return cache[i]

    cache[i] = fib_recurse(i - 1) + fib_recurse(i - 2)
    fib[i] = cache[i]

    return cache[i]


def fibonacci(i):
    fib_recurse(i)
    return fib[0:i]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))
    print(list(map(cube, fibonacci(n))))
