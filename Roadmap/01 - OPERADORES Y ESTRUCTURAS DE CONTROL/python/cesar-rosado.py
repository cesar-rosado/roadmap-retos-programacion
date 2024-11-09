# 01 OPERADORES Y ESTRUCTURAS DE CONTROL

# EJERCIO 1: TIPOS DE OPERADORES
print("#### EJERCIO 1: TIPOS DE OPERADORES ####")
# Operadores Aritméticos
print("")
print("*** Operadores Aritméticos ***")
print(f"La suma de 5 + 10 es: {5 + 10}")
print(f"La resta de 10 - 5 es: {10 - 5}")
print(f"La multiplicación de 3 * 5 es: {3 * 5}")
print(f"La división de 10 / 2 es: {10 / 2}")
print(f"La división entera de 10 // 3 es: {10 // 3}")
print(f"El módulo 14 % 4 es: {14 % 4}")
print(f"2 elevado al cubo es: {2 ** 3}")
print("")

# Operadores Lógicos
print("*** Operadores Lógicos ***")
operador_and = 5 > 6 and 2 < 10
operador_or = 10 > 12 or 2 + 2 == 4
operador_not = not ("a" == "b")
print(f"Operador AND: {operador_and}")
print(f"Operador OR: {operador_or}")
print(f"Operador NOT: {operador_not}")
print("")

# Operadores de comparación
print("*** Operadores de comparación ***")
print(f"100 es igual a 100:     {100 == 100}")
print(f"5 es diferente a 10:    {5 != 10} ")
print(f"3 es mayor 6:           {3 > 6}")
print(f"3 es mayor o igual 2:   {3 >= 2}")
print(f"3 es menor 6:           {3 < 6}")
print(f"3 es menor o igual 2:   {3 <= 2}")
print("")

# Operadores de asignación
print("*** Operadores de asignación ***")
num = 5
print(f"Variable num = {num}")
print(f"Operador '=': asigna un valor a una varible 'x = {num}' ")
num += 1
print(f"Operador '+=': suma el valor asignado (1) a la variable num' {num}'")
num = 5
num -= 1
print(f"Operador '-=': resta el valor asignado (1) a la variable num '{num}' ")
num = 5
num *= 2
print(f"Operador '*=': multiplica el valor asignado (2) a la variable num '{num}'")
num = 10
print(f"Ahora num = {num}")
num /= 2
print(f"Operador '/=': divide el valor asignado (2) a la variable num '{num}'")
num = 10
num %= 2
print(f"Operador '%=': Aplica el módulo asignado (2) a la variable num '{num}'")
num = 10
num //= 2
print(
    f"Operador '//=': Aplica la división entera asignada (2) a la variable num '{num}' "
)
num = 10
num **= 2
print(f"Operador '**=': Potencia la variable num al valor asignado (2) '{num}'")
print("")

# Operadores de identidad
print("*** Operadores de identidad ***")
a = [9, 11, 2]
b = a
c = [2, 9, 11]
print(f"a = {a}\nb = {b}\nc = {c}")
print(f"a is b = {(a is b)}")
print(f"a is c = {(a is c)}")
print("")

# Operadores de pertenencia
print("*** Operadores de pertenencia ***")
print(f"11 se encuentra en la lista 'a': {(11 in a)}")
print(f"7 se encuentra en 'a': {(7 in a)}")
print(f"20 no se encuentra en 'a': {(20 not in a)}")
print("")

# Operadores de bits
a = 5
b = 8
print(f"a = {a}\nb = {b}")
print(f"AND: {a & b}")
print(f"OR: {a | b}")
print(f"XOR: {a ^ b}")
print(f"NOT: {~a}")
print(f"Desplazamiento a la izquierda: a << 1 = {a << 1}")
print(f"Desplazamiento a la derecha: a >> 1 = {a >> 1}")
print("")

# EJERCICIO 2: TIPOS DE ESTRUCTURA DE CONTROL
print("### EJERCICIO 2: TIPOS DE ESTRUCTURA DE CONTROL ####")
print("")
