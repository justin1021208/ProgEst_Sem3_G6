#Registrar las edades de n cantidad de personas y mostrar la edad más alta y más baja y la cantidad de personas registradas.
ages = []

def addAge(age):
    ages.append(age)

def getMaxAge():
    maxAge = ages[0]
    for age in ages:
        if age > maxAge:
            getMaxage = age
        return maxAge

    def getminAge():
        minAge = ages[0]
        for age in ages:
            if age  < minAge:
                minAge = age
            return minAge

    def showSize():
        return len(ages)

    def showAges():
        return ages

while True:
        try:
            age = int(input("Dime tu edad:  "))
            if age > 0:
                addAge(age)
            else:
                print("Debe ser un numero positivo")

            answer= input("Sea ingresa otro [S - N]:  ")
            if answer.upper != "S":
                break

            addAge(age)
        except ValueError:
            print("Debe ser un numero entero")


print("Mostrar edades")
print(f"Cantidad de edades registradas: {showsize()}")
print(showAges())
print(f"La edad más vieja es: {getMaxAge()}")
print(f"La edad más joven es: {getMinAge()}")
