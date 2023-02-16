import sympy as sym #Calculo simbolico
from sympy import *
import numpy as np
import matplotlib.pyplot as plt


x = symbols('x') # La variable simbolica para realizar los caálculos correspondientes
#m: Coordenadas en x
#z: Coordenadas en y
def ddn(m, z):
    #Obtencion de diferencias divididas
    #Se crea una matriz para añadir los vectores de x y de y
    a = []
    for g in range(len(m)+1):
        aux = []
        for e in range(len(m)):
            aux.append(0)
        a.append(aux)


    for s in range(len(m)):
        a[0][s] = (m[s])
        a[1][s] = (z[s])
        b = 1
        c = 1
        d = 1
    for i in range(len(a[0])):
        for j in range(len(a[0])-b):
            a[c+1][j] = ((a[c][j+1]-a[c][j])/(a[0][j+d]-a[0][j])) #Formula de las diferencias divididas, los resultados que se guardaran en la matriz
        b+= 1
        c+= 1
        d+= 1
    print("\n Valores de los terminos: ")
    for l in range(len(a[0])):
        print("a[", l, "]=", a[l + 1][0])

    print("\n")
    matrix = np.array(a)
    matrix_t = np.transpose(matrix)
    print(matrix_t)

    # se obtiene todo el polinomio
    p=0
    w=0

    for t in range(len(a[0])):
        terminos=1
        for r in range(w):
            terminos*=(x-a[0][r])
        w+=1
        p+= a[t+1][0]*terminos
        pol=simplify(p)
    print("\n Polinomio: ")
    print(pol)
    return pol




    #Prueba
#m= [-2,-1,0,2,3,6]
#z= [-18,-5,-2,-2,7,142]

    #Prueba 2
#m=[1,3,5,6]
#z=[0.6666666667,1,-1,0]

m=[1,3,4,8]
z=[2,3,2,10]

px = sym.lambdify(x,ddn(m,z)) #Transforma la expresion en una funcion lambda
pxi=np.linspace(-10,10,100)
pfi = px(pxi)
np.set_printoptions(precision = 4)
plt.plot(m,z,'o', label = 'Puntos')
plt.plot(pxi,pfi, label = 'Polinomio')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Diferencias Divididas - Newton')
plt.show()




