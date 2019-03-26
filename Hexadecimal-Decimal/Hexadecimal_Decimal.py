import math
def Programa():
    hexadecimal = input()
    decimal = 0
    for cifra in reversed(list(hexadecimal)):
        print(list(hexadecimal))
        print(hexadecimal.index(cifra))
        [index for index,i in enumerate(hexadecimal) if i==cifra]
        print(index)
        if cifra.lower() == "a":
            decimal += 10 * math.pow(16,hexadecimal.index(cifra))
        elif cifra.lower() == "b":
            decimal += 11 * math.pow(16,hexadecimal.index(cifra))
        elif cifra.lower() == "c":
            decimal += 12 * math.pow(16,hexadecimal.index(cifra))
        elif cifra.lower() == "d":
            decimal += 13 * math.pow(16,hexadecimal.index(cifra))
        elif cifra.lower() == "e":
            decimal += 14 * math.pow(16,hexadecimal.index(cifra))
        elif cifra.lower() == "f":
            decimal += 15 * math.pow(16,hexadecimal.index(cifra))
        else:
            decimal += int(cifra) * math.pow(16,hexadecimal.rindex(cifra))
    print(int(decimal))

Programa()