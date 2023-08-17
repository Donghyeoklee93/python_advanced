# 1. replace

a = "today's weather is cloudy.".replace("cloudy", "clear")
print(a)


# 2. find
b = "hello world".find("world")
print(b)

b = "hello world".find("world2")
print(b)

# 3. split
c = "nike_shoes 265 x1212 78000".split()
print(c)

c = "nike_shoes:265:x1212:78000".split(":")
print(c)

# 4. strip
e = "      yeah      ".lstrip()
print(e)

f = "      yeah      ".rstrip()
print(f)

g = "      yeah      ".strip()
print(g)
