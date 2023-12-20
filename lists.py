girls = ["Kimera", "Zela", "Madonna"]

print(girls)
print(len(girls))

guys = list(("Sansón", "Simbel", "Alex"))
print(guys)

if "Kimera" in girls:
    print("Fabulous")

if "Kimera" not in guys:
    print("Still fabulous")

guys[0] = ["Minsk"]

print(guys)

guys[0:2] = ["Sansón", "Dominic"] #El segundo índice no se sustituye

print(guys)

guys[1:2] = ["Fernando", "Miguel", "Juanito"]

print(guys)

guys[1:3] = ["Chenoa"]

print(guys)

guys.insert(1, "Manoa") #Inserta sin reemplazar

print(guys)

girls.append("Emma")

print(girls)

guys.extend(girls)

print(guys)

fruits = ("strawberry", 125, 85.6)

girls.append(fruits)

print(girls)

girls.remove(fruits)

print(girls)

girls.pop(0)

print(girls)

girls.pop()

print(girls)

del girls[0]

print(girls)

girls.clear()

print(girls)

