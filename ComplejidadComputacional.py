#Programar un algoritmo (por ejemplo en python) que dada una lista de números, retorna dos elementos que sumados den un cierto número. 
#En caso de no hallar 2 números que sumen el otro número, retornar 0.

#sumandos_version(numeros, suma)

misNumeros = [1, 2, 3, 4, 5]
miSuma = 5

def sumandos_version(numeros, suma):
    sumandos = 0
    for i in range(len(numeros)):
        i = i + 1
        for j in range(i, len(numeros)):
            if numeros[i] + numeros[j] == suma:
                sumandos =  numeros[i], numeros[j]

    if sumandos == 0:
        print("No se encontraron dos números que sumados de ", suma)
    else:
        print("Los dos números que sumados dan", suma, "son", sumandos)

sumandos_version(misNumeros, miSuma)

