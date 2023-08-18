def minus_one(a):
    return a - 1


# lambda
lambda a: a - 1

# call lambda 1
print((lambda a: a - 1)(10))

# call lambda 2
minus_one_2 = lambda a: a - 1
print(minus_one_2(100))


# lambda using if
def is_positive_number(a):
    if a > 0:
        return True
    else:
        return False


# lambda
lambda a: True if a > 0 else False

print((lambda a: True if a > 0 else False)(2))
print((lambda a: True if a > 0 else False)(-1))

is_positive_number = lambda a: True if a > 0 else False
print(is_positive_number(2))
print(is_positive_number(-1))
