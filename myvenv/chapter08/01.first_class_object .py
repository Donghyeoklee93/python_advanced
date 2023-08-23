# 1. It can be used like data.


# 1) function can be assigned to variables
def func(x, y):
    return x + y


add = func
print(add(3, 4))


# 2) it can assigned to list(tuple, dictionary)
def mul(x, y):
    return x * y


def div(x, y):
    return x / y


calculator = [mul, div]
print(calculator[0](5, 6))


# 2. It can be passed as a parameter.
def inputData():
    data = input("data >>>")
    return data


def start(func):
    print("entered data is", func())


start(inputData)


# 3. It can be used as a return value.
def plusTen(a):
    return a + 10


def func(x):
    return plusTen(x)


print(func(5))
