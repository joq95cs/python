x = ("Fresa", "Mandarina", "Repollo") #Es tupla
y = list(x) #Se crea una lista en base a la tupla
y[2] = "Toronja"
x = tuple(y) #Se regresa a tupla

print(x)
print(type(x))

y = list(x)
y.append("Platano")
x = tuple(y)

print(x)
print(type(x))

z = ("Coco", "Melon")
x += z

print(x)
print(type(x))

y = list(x)
y.remove("Fresa")
x = tuple(y)

print(x)
print(type(x))

del x #Borra la tupla al final