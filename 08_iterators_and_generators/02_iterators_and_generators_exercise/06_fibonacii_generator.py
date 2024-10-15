def fibonacci():
    current_num = 0
    next_num = 1
    while True:
        yield current_num
        helping_num = current_num
        current_num = next_num
        next_num += helping_num


generator = fibonacci()
for i in range(5):
    print(next(generator))
print()

generator = fibonacci()
for i in range(1):
    print(next(generator))
