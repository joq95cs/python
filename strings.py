a = """Hello a todos
Lady Gaga
lanzó una canción fea"""

print(a)
print(a[6])

for i in a:
    print(i)

print(len(a))
print("Gaga" in a)

if "Lady" in a:
    print("Lo tiene!")
else:
    print("No!")

print("Lola" not in a)

if "Lola" not in a:
    print("No lo tiene!")
else:
    print("Sí!")

print(a[0:45]) #del 0 al 45
print(a[:45]) #del inicio al 45
print(a[0:]) #del 0 al final
print(a[-5:-2])

print(a.upper())
print(a.lower())
print(a.strip()) #delete spaces at the beggining or end
print(a.replace("H", "K"))
print(a.replace("Lady", "Bruja fea"))
print(a.split(" "))