def squares(n):
    starting_num = 1
    while starting_num <= n:
        yield starting_num * starting_num
        starting_num += 1


print(list(squares(5)))
