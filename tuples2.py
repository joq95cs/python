nombres = ("Joqsan", "Lehabim", "Ruth Mandarina")

(n1, n2, n3) = nombres #Unpacking

print(n1)
print(n2)
print(n3)

(p1, *p) = nombres #p* es una lista que toma valores a partir del segundo elemento

print(p1)
print(p)

(*c, c1) = nombres

print(c)
print(c1)