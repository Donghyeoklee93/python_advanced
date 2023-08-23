import re

# 1. re module method

str = "love people around you. love your work, love yourself"

# 1) match : Searching from the beginning of the string (result: 1 match object)
result = re.match("love", str)
print(result)


# 2) search : Searching the entire string (result: 1 match object)
result = re.search("people", str)
print(result)


# 3) findall : Searching the entire string (result: string object)
results = re.findall("love", str)
print(results)


# 4) finditer : Searching the entire string (result: match object iterator
results = re.finditer("love", str)
print(results)

for result in results:
    print(result)

# 5) fullmatch : Checking if the pattern and the string match perfectly.
str2 = "Hey Guys, read books"
result = re.fullmatch(".*", str2)
print(result)

# 2. match object method
result = re.search("people", str)

print(result.group())

print(result.start())

print(result.end())

print(result.span)
