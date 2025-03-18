PREGUNTAS TEÓRICAS - CHECKPOINT5
# 1. Condicionales en Python
Los condicionales son estructuras de control que permiten que un programa tome decisiones basadas en ciertas condiciones.
Estas sentencias nos permiten evaluar expresiones y ejecutar diferentes bloques de código dependiendo de si estas expresiones son verdaderas o falsas.
En Python, los condicionales se implementan principalmente a través de las instrucciones if, elif
if
La instrucción if se utiliza para ejecutar un bloque de código si una condición es verdadera. La sintaxis básica es la siguiente:
if condicion:
    bloque de código si la condición es verdadera
Por ejemplo, podemos utilizar un if para verificar si un número es mayor que 10:
numero = 15

if numero > 10:
    print("El número es mayor que 10")
En este caso, como la condición numero > 10 es verdadera, se ejecutará el print y veremos en la salida “El número es mayor que 10”.
else
La condición else se utiliza para ejecutar un bloque de código cuando la condición en el if es falsa. La sintaxis es la siguiente:
if condicion:
     bloque de código si la condición es verdadera
else:
     bloque de código si la condición es falsa
Siguiendo el ejemplo anterior, voy a agregar un else para ver el caso en que el número no sea mayor que 10:
numero = 5

if numero > 10:
    print("El número es mayor que 10")
else:
    print("El número es menor o igual a 10")
En este caso, como numero es 5 y la condición numero > 10 es falsa, se ejecutará el bloque de código dentro del else y veremos en la salida “El número es menor o igual a 10”.
elif
La función elif se utiliza para evaluar múltiples condiciones de manera secuencial.
La sintaxis es la siguiente:
if condicion_1:
    bloque de código si la condicion_1 es verdadera
elif condicion_2:
   bloque de código si la condicion_1 es falsa y la condicion_2 es verdadera
else:
     bloque de código si todas las condiciones anteriores son falsas
Un ejemplo :
numero = 5

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")
En este caso, como numero es 5 y es mayor que 0, se ejecutará el primer bloque de código y veremos en la salida “El número es positivo”.
Condiciones múltiples
También es posible combinar múltiples condiciones utilizando los operadores and, or y not. Estos operadores nos permiten construir condiciones más complejas:
and: devuelve True si ambas condiciones son verdaderas.
or: devuelve True si al menos una de las condiciones es verdadera.
not: devuelve True si la condición es falsa.
Por ejemplo:
x = 10
y = 5
z = 0

if x > y and y > z:
    print("Todas las condiciones son verdaderas")
En este caso, las tres condiciones son verdaderas (x > y, y > z y x > z), por lo tanto, se ejecutará el print.

# 2. Bucles

Las estructuras de control de flujo nos permiten crear repeticiones en el código. Existen dos tipos de bucles:

A. While

Sirve para crear bucles con un número indeterminado de iteraciones, donde simplemente necesitamos que se cumpla una determinada condición para que el bucle siga ejecutándose n veces.

 Ejemplo: Para calcular la raíz cuadrada de un número

import math   para poder utilizar sqrt

Pedimos un número al usuario
numero = int(input("Introduzca un número:"))

Indicamos una condición
while numero < 0:
    print("Error, debería ser un número positivo")
    numero = int(input("Introduzca un número positivo:"))

Mostramos el resultado
print(f"\nSu raíz cuadrada es: {math.sqrt(numero):.2f}")

Este bucle se ejecutará siempre y cuando la condición se cumpla. Cuando la condición deje de cumplirse, saldremos del bucle y nos dará la raíz cuadrada. El bucle puede ejecutarse n veces o no ejecutarse ninguna vez.


Ejemplo 1: Bucle `while`
Queremos mostrar un mensaje 10 veces, es decir, un número determinado de veces:
i = 0 while i < 10: print("Hola Txufi") i += 1
**Salida:**
Hola Txufi
Hola Txufi 
Hola Txufi 
Hola Txufi 
Hola Txufi 
Hola Txufi
 Hola Txufi 
Hola Txufi 
Hola Txufi 
Hola Txufi

Si lo que queremos es mostrar los números del 0 al 9:

print(i)

B.  Bucle `for`

El bucle `for` se utiliza cuando sabemos cuántas veces se va a repetir el bucle. Se usa con colecciones, y tendremos un iterador que recorrerá los elementos de una colección (lista, tupla, diccionario, etc.).

 Ejemplo 1:

for i in [1, 2, 3, 4, 5]: print("Hola Txufi")

**Salida:**

Hola Txufi 
Hola Txufi 
Hola Txufi 
Hola Txufi 
Hola Txufi

La variable iteradora (i) recorre la colección (la lista) elemento por elemento. Como hay 5 elementos en la colección, el bucle se repite 5 veces.

 Ejemplo 2: Lista diferente

Podría ser una lista como esta:

[2, 10, "Olatz", 8, 12]

Para ver mejor cómo cambia la variable iteradora `i`, podemos hacer lo siguiente:

for i in [2, 10, "Olatz", 8, 12]: print(f"Elemento: {i}")

**Salida:**

Elemento: 2 
Elemento: 10
Elemento: Olatz 
Elemento: 8 
Elemento: 12

Ejemplo 3: Recorrer un diccionario (clave, valor)

coleccion = {"Olatz": 25, "Maria": 32, "Rosa": 14, "Luis": 45}
for i in coleccion: print(f"Elemento: {i}")

**Salida:**

Olatz
Maria 
Rosa 
Luis
La variable iteradora recorre las claves del diccionario. Si queremos obtener los valores, podemos hacer lo siguiente:

for i in coleccion: print(f"{coleccion[i]}")

**Salida:**

25 
32 
14 
45

Ejemplo 4: Recorrer un string

Los elementos de un string son sus caracteres:

coleccion = "Olatz" for i in coleccion: print(f"{i}")

**Salida:**

O
 l 
a 
t
 z

Si quieres que los caracteres aparezcan en la misma línea:

for i in coleccion: print(f"{i}", end="")

Instrucciones `break` y `continue`

Dentro de los bucles en Python, también podemos utilizar las instrucciones `break` y `continue` para controlar el flujo de ejecución.

Instrucción `break`

La instrucción `break` termina el bucle y ejecuta el bloque de código que está después del bucle.

Ejemplo con `break`:

frutas = ["manzana", "banana", "cereza", "sandía", "uva"]
for fruta in frutas: print(fruta) if fruta == "sandía": break

En este caso, el bucle `for` imprimirá cada fruta de la lista hasta que llegue a "sandía", momento en el cual se ejecutará `break` y el bucle se interrumpirá.

Instrucción `continue`

La sentencia `continue` se utiliza para saltarse el resto del código en una iteración y continuar con la siguiente.

 Bucles con `else`

En Python, los bucles también pueden tener una cláusula `else`, que se ejecuta cuando el bucle termina sin haber sido interrumpido por un `break`. 
Ejemplo con `else`:

numeros = [1, 2, 3, 4, 5]
for numero in numeros: if numero == 0: break else: print("El bucle ha terminado sin encontrar el número 0")

En este caso, como no hay ningún 0 en la lista `numeros`, el bucle se ejecutará completamente y al final se imprimirá:

El bucle ha terminado sin encontrar el número 0

Bucle `for` con `range`

Con la función `range` indicamos cuántas veces debe repetirse el bucle:

for i in range(0, 5): print("Hola, el número de i es:", i)

**Salida:**

Hola, el número de i es: 0 Hola, el número de i es: 1 Hola, el número de i es: 2 Hola, el número de i es: 3 Hola, el número de i es: 4

La función `range` nos permite controlar el número de ciclos que queremos dentro del `for`.

 Ejemplo 2: Para conocer el valor de `i`:

print("Inicio")
n = 5
for i in range(n): print(i, "Hola")
print("Fin")

La función `range` establece un rango e `i` va tomando valores dentro de ese rango.
 
Podemos indicar los valores de inicio, fin y paso:
for i in range(2, 8): # Donde 2 es el valor de inicio y 8 el de fin print(i)
También podemos indicar un tercer parámetro, que es el paso (por ejemplo, 2):
for i in range(2, 8, 2): # El 2 significa que la variable dará saltos de 2 en 2 print(i)

Último Ejemplo: Tabla de multiplicar

Queremos mostrar la tabla de multiplicar del número que introduzca el usuario. El número que nos dé el usuario será fijo, y el que irá variando es el multiplicador, que irá de 0 a 9.
Solicitar al usuario que ingrese un número:
n = int(input("Ingrese un número: "))
Ahora hacemos las iteraciones:
for i in range(10): resultado = i * n print(i, "x", n, "=", resultado)
Si en lugar de la tabla de multiplicar de un solo número, queremos la tabla de multiplicar de todos los números del 1 al 9:

for n in range(1, 10): for i in range(10): resultado = i * n print(i, "x", n, "=", resultado)

3. # Qué es una lista por comprensión en Python?

Las listas por comprensión ofrecen una forma eficaz y concisa de generar listas en Python. Pueden simplificar el código y hacerlo más legible al reemplazar varias líneas de código de bucle con una sola línea de listas por comprensión.

Ejemplos de Listas por Comprensión:
Creando una lista de cuadrados
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [x ** 2 for x in numbers]
print(squares)
# Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Filtrar elementos
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(even_squares)
# Salida: [0, 4, 16, 36, 64]



# 4. Argumentos y Parámetros en Python
En Python, un argumento es un valor que se pasa a una función cuando se llama a esa función. Los argumentos permiten que las funciones reciban datos y los utilicen para realizar operaciones o cálculos.
 Ejemplo de uso de un argumento:
def saludar(nombre): print(f"¡Hola, {nombre}!")
Llamada a la función con un argumento
saludar("María") En este ejemplo, nombre es un argumento de la función saludar. Cuando llamamos a la función con saludar("María"), el valor "María" se pasa como argumento y se utiliza dentro de la función para imprimir el saludo.
Tipos de argumentos en Python
En Python, existen varios tipos de argumentos que se pueden pasar a una función:
1. Argumentos Posicionales
Los argumentos posicionales se pasan a la función en el orden en que se definen.
2. Argumentos Nombrados (o Keyword Arguments)
Los argumentos nombrados se pasan a la función con un nombre específico, lo que permite cambiar el orden de los argumentos.
3. Argumentos por Defecto
Los argumentos por defecto son aquellos que tienen un valor predeterminado. Si no se proporciona un valor al llamar a la función, se utilizará el valor por defecto.
4. Argumentos Variables
Los argumentos variables permiten pasar un número variable de argumentos a una función. Se utilizan:
args para argumentos posicionales.
kwargs para argumentos nombrados. 

Ejemplo con varios tipos de argumentos: def informacion_persona(nombre, edad=30, *args, **kwargs): print(f"Nombre: {nombre}") print(f"Edad: {edad}")
for arg in args:
    print(f"Argumento adicional: {arg}")

for key, value in kwargs.items():
    print(f"{key}: {value}")

Llamada a la función con diferentes tipos de argumentos
informacion_persona("Juan", 25, "Bilbao", "España", ocupacion="Ingeniero", hobby="Ciclismo") Parámetros en Python Los parámetros de una función son variables que podemos pasarle a la función al invocarla, para que las use. Los parámetros permiten que las funciones sean más flexibles y reutilizables.
Sintaxis básica de una función con parámetros: def nombre_de_la_funcion(parametro1, parametro2, ...):

Ejemplo con parámetros: def saludar(nombre): print("Hola", nombre)
Llamando a la función con un argumento
saludar("Luis")
Salida: Hola Luis
Aquí definimos una función llamada saludar que toma un parámetro llamado nombre. Dentro de la función, se imprime un saludo “Hola” seguido del nombre que se pasa como argumento.
Tipos de parámetros en Python
Parámetros Posicionales: Los parámetros posicionales son los parámetros más comunes. Se definen en el orden en que aparecen en la lista de parámetros de la función y se pasan a la función en el mismo orden.
def suma(a, b): resultado = a + b return resultado
Llamada a la función con parámetros posicionales
resultado_suma = suma(5, 3) print(resultado_suma)
Salida: 8
Parámetros con valores predeterminados: Podemos asignar valores predeterminados a los parámetros, lo que permite llamar a la función sin necesidad de proporcionar un valor para ese parámetro.
def saludar(nombre, mensaje="Hola"): print(f"{mensaje}, {nombre}")
Llamada con un valor predeterminado
saludar("Luis")
Salida: Hola, Luis
Llamada con un valor proporcionado
saludar("Luis", "Buenos días")
Salida: Buenos días, Luis
Parámetros de longitud variable: Python permite definir funciones que aceptan un número variable de parámetros utilizando *args y **kwargs.
*args: Se utiliza para pasar una lista de argumentos posicionales. def suma_numeros(*args): resultado = sum(args) return resultado
Llamada a la función con una cantidad variable de argumentos
resultado_suma = suma_numeros(1, 2, 3, 4, 5) print(resultado_suma)
Salida: 15
**kwargs: Se utiliza para pasar un diccionario de argumentos de palabra clave (keyword arguments). def imprimir_info(**kwargs): for clave, valor in kwargs.items(): print(clave + ":", valor)
Llamada a la función con argumentos con nombre
imprimir_info(nombre="Jacobo", edad=32, ciudad="Getxo")
Salida:
nombre: Jacobo edad: 32 ciudad: Getxo
# 5. Qué es una función Lambda en Python?
Funciones Lambda en Python
Las funciones lambda, también conocidas como funciones anónimas, son una forma alternativa y concisa de definir funciones. Las funciones lambda no tienen nombre. Son funciones pequeñas y se emplean en contextos donde se necesita una función de forma temporal, como cuando se utilizan como parámetros de otras funciones.
Sintaxis Básica de Funciones Lambda
En Python, las funciones lambda se definen utilizando la palabra clave lambda seguida de una lista de parámetros, seguida de dos puntos : y una expresión.
Sintaxis
lambda parametros: expresion
Ejemplo de función lambda
Podemos definir una función lambda que calcule el cuadrado de un número de la siguiente forma:

suma = lambda x: x * x
Esta función lambda:
Toma un argumento x
Retorna el resultado de x * x

Funciones Lambda con Múltiples Argumentos
En este ejemplo, suma es una función lambda que toma dos argumentos x e y y devuelve la suma de ambos.

suma = lambda x, y: x + y
print(suma(3, 5)) 
Salida: 8

Suma de dos números
suma = lambda x, y: x + y
print(suma(3, 5)) 
Salida: 8

Filtrado de una lista
lista = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares)  
Salida: [2, 4]

Ordenación de una lista de tuplas
tuplas = [(1, 3), (2, 1), (4, 2)]
ordenadas = sorted(tuplas, key=lambda x: x[1])
print(ordenadas)  
Salida: [(2, 1), (4, 2), (1, 3)]


# 6.  Qué es un paquete pip?
pip es un sistema de gestión de paquetes para Python. 
Con pip, podemos instalar, actualizar y desinstalar paquetes de Python de manera sencilla.
Los paquetes son colecciones de módulos y funciones que pueden ser distribuidos y utilizados por otros programadores.

