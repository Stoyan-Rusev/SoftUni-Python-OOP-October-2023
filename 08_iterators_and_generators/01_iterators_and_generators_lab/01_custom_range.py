class CustomRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        current_num = self.start
        self.start += 1
        return current_num


c = custom_range(1, 5)
for num in c:
    print(num)
