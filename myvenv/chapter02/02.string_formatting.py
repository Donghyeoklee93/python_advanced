# if there is not formatting?
# Lee, there are 7 days left in the course period.

name = "lee"
duration = 7

message = name + ", there are " + str(duration) + " days left in the course period."
print(message)

# string formatting
message_format = f"{name}, there are {duration} days left in the course period."
print(message_format)

# format method
a = "Hello {2} {1} {0}".format("apple", "pineapple", "pen")
print(a)

b = "Hello {} {} {}".format("apple", "pineapple", "pen")
print(b)

# f-string
name1 = "apple"
name2 = "pineapple"
name3 = "pen"

c = f"Hello {name1} {name2} {name3}"
print(c)
