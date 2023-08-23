# generator expression
double_generator = (i * 2 for i in range(1, 10))

print(double_generator)

for i in double_generator:
    print(i)


# 3. for using memory efficiently

import sys

list_data = [i * 3 for i in range(1, 10000 + 1)]
generator_data = list_data = (i * 3 for i in range(1, 10000 + 1))

print(sys.getsizeof(list_data))
print(sys.getsizeof(generator_data))
