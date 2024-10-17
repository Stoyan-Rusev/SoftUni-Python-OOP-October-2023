class store_results:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        with open('07_read.txt', 'a') as file:
            file.write(f"Function '{self.function.__name__}' was called. "
                       f"Result: {self.function(*args, **kwargs)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
