class Math:
    # static method
    # method that doesn't need to create instance

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y


print(Math.add(3, 4))
print(Math.sub(3, 4))
