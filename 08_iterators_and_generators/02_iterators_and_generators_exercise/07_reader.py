def read_next(*iterables):
    for iterable in iterables:
        if isinstance(iterable, dict):
            for key in iterable.keys():
                yield key
            for value in iterable.values():
                yield value
        else:
            for current in iterable:
                yield current


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
print()
print()

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
