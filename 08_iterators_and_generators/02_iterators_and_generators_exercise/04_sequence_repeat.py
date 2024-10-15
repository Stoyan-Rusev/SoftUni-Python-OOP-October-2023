class SequenceRepeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.number:
            raise StopIteration
        first_letter = self.sequence[:1]
        self.sequence = self.sequence[1:] + first_letter
        self.counter += 1
        return first_letter


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
print()

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
