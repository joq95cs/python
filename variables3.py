x = "dancing like crazy"

def testFunction():
    print("Zela is so green and loves", x)

y = "slap women"

def myFunction():
    #global y
    y = "have money"
    global z
    z = "Hello girls"
    print("Milena loves to", y)

testFunction()
myFunction()
print(y)
print(z)