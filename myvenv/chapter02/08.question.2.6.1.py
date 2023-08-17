time = input("Please enter time>>>")
# 1. only minute
# 2. only hour
# 3. hour and minute

if time.find("hour") == -1:
    result = int(time.split("minute")[0])
else:
    if time.find("minute") == -1:
        result = int(time.split("hour")[0]) * 60
    else:
        sub = time.split()
        hour = int(sub[0].split("hour")[0]) * 60
        minute = int(sub[1].split("minute")[0])
        result = hour + minute

print(result)
