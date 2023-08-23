# generator
# A function that creates iterators.


def season_generator(*args):
    for arg in args:
        yield arg


g = season_generator("spring", "summer", "autumn", "winter")

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())


def func():
    print("first work is processing....")
    yield 1

    print("second work is processing....")
    yield 2

    print("third work is processing....")
    yield 3


ge = func()
data = ge.__next__()
print(data)
