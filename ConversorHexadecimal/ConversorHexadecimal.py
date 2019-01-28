import math

print("                BIENVENIDO AL CONVERTIDOR A HEXADECIMAL")
print("                                DE MARIO")
print("Escribe el número decimal que deseas convertir a hexadecimal:")
dividendo = int(input())
resto = []
numero_veces = 0
for numero_veces in range(100000):
    resto.append(dividendo%16)
    dividendo//=16
    if dividendo <= 0:
       break
for elemento in reversed(resto):
    if int(elemento) == 10:
        print("a", end="")
    if int(elemento) == 11:
        print("b", end="")
    if int(elemento) == 12:
        print("c", end="")
    if int(elemento) == 13:
        print("d", end="")
    if int(elemento) == 14:
        print("e", end="")
    if int(elemento) == 15:
        print("f", end="")
    if elemento <=9:
        print(int(elemento), end="")
print()
input("Presiona una tecla para dejar de usar esta maravillosa aplicación")