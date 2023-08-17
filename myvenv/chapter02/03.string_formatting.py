# list method
fruits = ["apple", "orange", "mango"]
del fruits[1]
print(fruits)

# list sort
numbers = [5, 1, 2, 8, 3]
numbers.sort()
print(numbers)

# enumerate
titles = ["attendance", "verifying attendance", "require attendance"]

# index = 1
# for title in titles:
#     print(index, title)
#     index = index + 1

for index, title in enumerate(titles):
    print(index + 1, title)

for index, title in enumerate(titles, 1):
    print(f"This it the {index} post. Title : {title}")
