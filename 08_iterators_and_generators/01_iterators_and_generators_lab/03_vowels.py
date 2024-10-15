class Vowels:
    def __init__(self, string: str):
        self.string = string
        self.vowels = ('a', 'i', 'e', 'o', 'u', 'y')
        self.string_vowels = [ch for ch in self.string if ch.lower() in self.vowels]
        self.start_i = 0
        self.end_i = len(self.string_vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_i > self.end_i:
            raise StopIteration
        i = self.start_i
        self.start_i += 1
        return self.string_vowels[i]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
