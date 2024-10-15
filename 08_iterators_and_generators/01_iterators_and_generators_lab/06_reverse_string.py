def reverse_text(string: str):
    start_i = len(string) - 1
    for i in range(start_i, -1, -1):
        yield string[i]


for char in reverse_text("step"):
    print(char, end='')
