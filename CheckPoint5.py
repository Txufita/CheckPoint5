
# Ejercicio 1
autores = ['Oscar', 'Hermann', 'Joseph', 'Charles']

for autor in autores:
    print(autor)

# Ejercicio 2
def sum(num1, num2, num3):
    return num1 + num2 + num3

a = 5
b = 7
c = 9
print(sum(a, b, c))

# Ejercicio 3
sum = lambda x, y, z: x + y + z
print(sum(1, 2, 3))

# Ejercicio 4
nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

for i in lista_nombre:
    if i == nombre:
        print('True')
        break
else:
    print('False')
