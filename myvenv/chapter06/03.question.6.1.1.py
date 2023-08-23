# https://regexr.com/63cii


import re

datas = [
    "2022/08/08",
    "1000/01/01",
    "9999/12/31",
    "900/02/02",
    "12000/10/26",
    "2021/13/01",
    "2023/2/02",
    "2024/06/3",
    "2023/06/35",
]

regex = "^\d{4}/(0[1-9]|1[0-2])/(0[1-9]|1\d|2\d|3[01])$"

# for data in datas:
#     matchObj = re.match(regex, data)
#     print(matchObj)

for data in datas:
    matchObj = re.match(regex, data)
    result = (lambda x: True if x != None else False)(matchObj)
    print(f"{data} {result}")
