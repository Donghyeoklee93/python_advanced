# for i in "123":
#     print(i)

# for i in [10, 20, 30]:
#     print(i)


# print(type([10, 20, 30].__iter__))
iter_obj = [10, 20, 30].__iter__()
print(iter_obj)
print(dir(iter_obj))
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())

for i in iter_obj:
    print(i)
