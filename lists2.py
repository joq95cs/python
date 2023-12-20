fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
vegetables = []

for each in fruits:
    if "a" in each:
        vegetables.append(each)

print(vegetables)

objects = [x for x in vegetables if "a" in x]
print(objects)

newList = [x for x in range(10)]
print(newList)

newList = [x for x in range(10) if x < 3]
print(newList)

newList = [x.upper() for x in fruits]
print(newList)

newList = [x if x != "banana" else "orange" for x in fruits]
print(newList)

newList = ['hello' for x in fruits]
print(newList)