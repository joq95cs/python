fruits = ["lemon", "cherry", "orange", "banana"]

for i in fruits:
    print(i)

print()

for i in range(2):
    print(fruits[i])

print()

for i in range(len(fruits)):
    print(fruits[i])

print()

i = 0
while i < len(fruits):
    print(fruits[i])
    i+=1

print()

[print(i) for i in fruits]