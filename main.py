#1
data = {"Ali": 85, "Vali": 90, "Sami": 78}

max_key = max(data, key=data.get)

print(max_key)

#2
data = {"a": 10, "b": 20, "c": 30}

total = sum(data.values())

print(total)
