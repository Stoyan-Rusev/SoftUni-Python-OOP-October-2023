def vowel_filter(function):
    def wrapper():
        chars = function()
        return [ch for ch in chars if ch.lower() in 'aoueiuy']
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
