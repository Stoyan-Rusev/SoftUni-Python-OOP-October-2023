def even_numbers(function):
    def wrapper(numbers):
        even_only = [num for num in numbers if num % 2 == 0]
        result = function(even_only)
        return result
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
