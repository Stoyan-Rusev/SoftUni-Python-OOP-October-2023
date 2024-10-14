n = int(input())


def print_rhombus(n_: int):
    for i in range(n, 0, -1):
        print(' ' * (i - 1), end='')
        print((n - (i - 1)) * '* ')
    for i in range(1, n):
        print(' ' * i, end='')
        print((n - i) * '* ')


print_rhombus(n)
