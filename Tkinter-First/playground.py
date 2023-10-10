def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(2, 34, 3, 4, 4, 3, 3, 2))


def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)


calculate(add=2, multiply=5)
