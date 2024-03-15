class Insert:
    def perform(self, *arguments):
        if len(arguments) != 3:
            raise RuntimeError('Insert requires 3 arguments')
        lst, index, value = arguments
        lst.insert(index, value)


class Print:
    def perform(self, lst):
        print(lst)


class Remove:
    def perform(self, *arguments):
        if len(arguments) != 2:
            raise RuntimeError('Remove requires 2 arguments')
        lst, value = arguments
        lst.remove(value)


class Append:
    def perform(self, *arguments):
        if len(arguments) != 2:
            raise RuntimeError('Append requires 2 arguments')
        lst, value = arguments
        lst.append(value)


class Sort:
    def perform(self, lst):
        lst.sort()


class Pop:
    def perform(self, lst):
        lst.pop()


class Reverse:
    def perform(self, lst):
        lst.reverse()


class NoCommand:
    def perform(self, *arguments):
        print(f'No command found with that name args: {arguments}')


commands = {
    'insert': Insert(),
    'print': Print(),
    'remove': Remove(),
    'append': Append(),
    'sort': Sort(),
    'pop': Pop(),
    'reverse': Reverse()
}
if __name__ == '__main__':

    a = []

    n = int(input())

    for i in range(n):
        line = input().split()
        num_args = len(line)
        cmd = line[0]
        f = commands.get(cmd, NoCommand())

        if num_args > 1:
            args = [a]
            varargs = line[1:]
            args.extend(list(map(int, varargs)))
            f.perform(*args)
        else:
            f.perform(a)
