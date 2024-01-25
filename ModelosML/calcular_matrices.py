import numpy as np

"""
arr = np.array([[ 1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print (arr)
newarr = np.array_split(arr , 2)
print (newarr)
newarr = np.array_split(arr , 3, axis=1)
print(newarr)"""

"""
#bloque 1 
arr1[0,0] * arr2[0,0] + 
arr1[0,1] * arr2[1,0] + 
arr1[0,2] * arr2[2,0]

arr1[0,0] * arr2[0,1] + 
arr1[0,1] * arr2[1,1] + 
arr1[0,2] * arr2[2,1]


#bloque 2
arr1[1,0] * arr2[0,0] + 
arr1[1,1] * arr2[1,0] + 
arr1[1,2] * arr2[2,0]

arr1[1,0] * arr2[0,1] + 
arr1[1,1] * arr2[1,1] + 
arr1[1,2] * arr2[2,1]
"""

arr1 = np.array([[0, 1, 2], 
                [10, 11, 12]])

arr2 = np.array([[0, 1], 
                 [2, 10], 
                 [11, 12]])

def calcular_matrices(a, b):
    filas_a = np.shape(a)[0]
    columnas_a = np.shape(a)[1]
    columnas_b = np.shape(b)[1]

    if filas_a != columnas_b:
        return ("Error: al calcular matrices distintas")
    else:
        newarray = np.zeros((filas_a, columnas_b), dtype="i4")

        for x in range(columnas_b):
            for i in range(filas_a):
                suma = 0
                for j in range(columnas_a):
                    suma += a[i][j] * b[j][x]
                    #print(a[i][j], "x", b[j][x], " = ", a[i][j]* b[j][x])
                #print(suma)
                newarray[i][x] = suma
        return newarray

#print(calcular_matrices(arr1, arr2))
#print(np.dot(arr1,arr2))

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc(x)))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()