class ReverseIiter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start_i = len(self.iterable) - 1
        self.end_i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_i < self.end_i:
            raise StopIteration
        current_i = self.start_i
        self.start_i -= 1
        return self.iterable[current_i]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
