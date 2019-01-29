import math
def Programa():
    hexadecimal = input()
    decimal = 0
    for cifra in hexadecimal:
        hexadecimalReves = list(reversed(hexadecimal))
        if cifra.lower() == "a":
            decimal += 10 * math.pow(16,hexadecimalReves.index(cifra))
        elif cifra.lower() == "b":
            decimal += 11 * math.pow(16,hexadecimalReves.index(cifra))
        elif cifra.lower() == "c":
            decimal += 12 * math.pow(16,hexadecimalReves.index(cifra))
        elif cifra.lower() == "d":
            decimal += 13 * math.pow(16,hexadecimalReves.index(cifra))
        elif cifra.lower() == "e":
            decimal += 14 * math.pow(16,hexadecimalReves.index(cifra))
        elif cifra.lower() == "f":
            decimal += 15 * math.pow(16,hexadecimalReves.index(cifra))
        else:
            decimal += int(cifra) * math.pow(16,hexadecimalReves.index(cifra))
    print(int(decimal))

Programa()