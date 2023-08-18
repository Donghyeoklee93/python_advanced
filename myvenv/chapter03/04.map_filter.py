# 1. map function
# Reason to use
# When making new list by modifying original list
print(map(int, ["3", "4", "5", "6"]))
print(list(map(int, ["3", "4", "5", "6"])))


items = ["  mouse  ", "  keyboard  "]

# 1) for
for i in range(len(items)):
    items[i] = items[i].strip()
print(items)


# 2) map
def strip_all(x):
    return x.strip()


items = list(map(strip_all, items))
print(items)

# 3) lambda
items = list(map(lambda x: x.strip(), items))
print(items)


# 2. filter
# Reason to use
# When you want to extract elements that satisfy a condition from an existing list...


def func(x):
    return x < 0


print(filter(func, [-3, -2, 0, 5, 7]))
print(list(filter(func, [-3, -2, 0, 5, 7])))


animals = ["cat", "tiger", "dog", "bird", "monkey"]

# 1) for
result = []
for i in animals:
    if len(i) <= 3:
        result.append(i)
print(result)


# 2) filter
def word_check(x):
    return len(x) <= 3


result = list(filter(word_check, animals))
print(result)

# 3) lambda
result = list(filter(lambda x: len(x) <= 3, animals))
print(result)
