import os
while True:
    try:

        os.system("cls")
        edad = int(input("Edad: "))
        break
    except ValueError:
        print("Ingrese un valor numerico.")
    os.system("pause")


print("Edad registrada:", edad)