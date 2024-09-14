fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort()

print(fruits)

numbers = [-26.5, 24e78, 0.005, -45, 4]
numbers.sort()
print(numbers)

numbers.sort(reverse = True)
print(numbers)

def funcion(n):
    return abs(n - 600)

numeros = [1000, 14, 250, 800, 100, 200, 300]
numeros.sort(key = funcion)
print(numeros)

nombres = ["Joqsan", "Adalid", "angel", "soanna"]
nombres.sort()
print(nombres)

nombres.sort(key = str.lower) #Case insensitive
print(nombres)

nombres.reverse()
print(nombres)