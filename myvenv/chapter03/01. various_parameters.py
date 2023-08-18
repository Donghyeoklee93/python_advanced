# 1. position parameter


def my_func(a, b):
    print(a, b)


my_func(2, 3)


# 2. default parameter


def post_info(title, content="no content"):
    print("title :", title)
    print("content :", content)


post_info("Attendance")


# 3. keyword parameter


def post_info(title, content):
    print("title :", title)
    print("content :", content)


post_info(content="no", title="how to make girlfriend")
