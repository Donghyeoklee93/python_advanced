# 1. positional variable length parameter
def print_fruits(*args):
    # print(args)
    for arg in args:
        print(arg)


print_fruits("apple", "orange", "mango", "grape")


# 2. keyword variable length parameter
def comment_info(**kwargs):
    # print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} : {value}")


comment_info(name="python", content="So thanks")
print()

# parameter writing order


def post_info(*tags, title, content):
    print(f"title : {title}")
    print(f"content : {content}")
    print(f"tag : {tags}")


post_info(
    "#python",
    "#function",
    title="Summarizing Python Functions!",
    content="Organizing Various Parameters!",
)

print()


def post_info(title, content, *tags):
    print(f"title : {title}")
    print(f"content : {content}")
    print(f"tag : {tags}")


post_info(
    "Summarizing Python Functions!",
    "Organizing Various Parameters!",
    "#python",
    "#function",
)

print()


def post_info(*tags, title, content, **kwargs):
    print(f"title : {title}")
    print(f"content : {content}")
    print(f"tag : {tags}")


post_info(
    "#python",
    "#function",
    title="Summarizing Python Functions!",
    content="Organizing Various Parameters!",
)

print()
