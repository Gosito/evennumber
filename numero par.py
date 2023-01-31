
numero = int(input("Dame un número entre 1 y 1000: "))
if numero % 2 == 0:
    print("Es un número par")
else:
    while numero % 2 != 0:
        numero = int(input("Es un número impar. ¿Puedes añadir otro?: "))
if numero % 2 == 0:
    print("Es un número par")
