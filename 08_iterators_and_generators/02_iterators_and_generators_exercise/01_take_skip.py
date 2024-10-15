class TakeSkip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.num = 0
        self.iterations_counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations_counter >= self.count:
            raise StopIteration
        self.iterations_counter += 1
        current_num = self.num
        self.num += self.step
        return current_num


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
