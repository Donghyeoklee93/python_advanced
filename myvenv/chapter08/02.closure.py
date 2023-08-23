# 1. inner function


def outer(name):
    def inner():
        print(name, "HI")

    return inner


func = outer("startcoding")
# func()


# 2. closure
# A function that can continue to use resources even after it has finished executing.

# Conditions for becoming a closure:
# 1)It must be an inner function.
# 2)It needs to reference variables from the outer function.
# 3)The outer function must return the inner function.


def greeting(name, age, gender):
    def inner():
        print(name, "HI")
        print("age: ", age)
        print("gender: ", gender)

    return inner


closure = greeting("nami", 27, "female")
closure()

# print((closure.__closure__[0]).cell_contents)

for i in closure.__closure__:
    print(i.cell_contents)


# It can be achieved using global variables,
# but minimizing the use of global variables is recommended due to issues like naming conflicts and scope problems.
