# Ejercicio #25: Hallar la suma de los primeros 10 números enteros naturales.




print("-----------------------------------------")
print("----------Suma Números Enteros-----------")
print("-----------------------------------------")

# input

N = int(input("Digite la cantidad de numeros que quiere sumar: "))

A = 1
sum = 0

# processing

while A <= N:
    sum = sum + A
    A = A + 1

# output


print("El resultado de la suma de los" + str(N) + " numeros enteros es: " + str(sum))

