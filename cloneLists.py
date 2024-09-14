frutas = ["fresa", "platano", "uva"]
vegetales = frutas.copy()

print(vegetales)

fruits = list(frutas) #También se clona la lista
print(fruits)

vegetables = vegetales + ["zanahoria", "cebolla"]

print(vegetables)

girls = ["Kimera", "Madonna", "Zela"]
people = ["Simbel", "Sansón", "Dominic"]

for i in girls:
    people.append(i)

print(people)

guys = ["Alex", "Gilberto"]
people.extend(guys)

print(people)