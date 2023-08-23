# decorator

# logging, cheking authentication


# decorator
def logger(func):
    def wrapper(arg):
        print("function start")
        func(arg)
        print("function end")

    return wrapper


@logger
def print_hello(name):
    print("hello", name)


@logger
def print_bye(name):
    print("bye", name)


print_hello("startcoding")
print_bye("fastcampus")
