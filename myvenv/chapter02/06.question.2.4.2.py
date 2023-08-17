list = ["omega3", None, "vitaminC500", None, "red ginseng extract slice"]
print(list)

result = [i if i != None else "" for i in list]
print(result)
