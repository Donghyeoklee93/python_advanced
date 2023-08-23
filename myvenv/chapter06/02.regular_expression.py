import re

# https://regexr.com/63bls

# 1. Group

# 1) One matching string
# str1 = "010-2343-3333"
# result = re.match("\d{2,3}-\d{3,4}-\d{4}$", str1)
# print(result.group(1))


# 2) Multiple matching strings
str2 = "010-2343-3333,010-2343-1234,010-2343-5678,010-2343-9999,010-2343-2222"
results = re.finditer("\d{2,3}-\d{3,4}-(\d{4})(?=,|$)", str2)

for idx, result in enumerate(results, 1):
    print(f"{idx}. {result.group(1)}")


# 2. Substitution
str3 = "010-2343-3333"
result = re.sub("(?<=\d{3}-\d{4}-)\d{4}", "****", str3)
print(result)
