class DictionaryIter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.kvp_count = len(self.dictionary)

    def __iter__(self):
        return self

    def __next__(self):
        if self.kvp_count == 0:
            raise StopIteration
        for key, value in self.dictionary.items():
            self.kvp_count -= 1
            del self.dictionary[key]
            return key, value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
print()
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
