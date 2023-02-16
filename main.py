import sympy as sym
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
x = symbols('x')
np.set_printoptions(precision = 4)

def ddn(m, z):
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
            a[c+1][j] = ((a[c][j+1]-a[c][j])/(a[0][j+d]-a[0][j]))
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

px = sym.lambdify(x,ddn(m,z))
pxi=np.linspace(-100,100,1000)
pfi = px(pxi)
plt.plot(m,z,'o', label = 'Puntos')
##for i in range(0,n,1):
##    plt.axvline(xi[i],ls='--', color='yellow')
plt.plot(pxi,pfi, label = 'Polinomio')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Diferencias Divididas - Newton')
plt.show()


#Grafica de polinomio °°
#polinomio =[]
#polinomio = ddn(m,z)
#print("polinomio: ", polinomio)
#crea un arreglo de valores para el eje x
#y=np.linspace(-5,5,100)
#d=np.linspace(-5,5,100)
#evalua el polinomio en cada valor de x
#y= np.polyval(ddn(m,z), d)

#ddn(m,z)
#Grafica el polinomio
#plt.plot(d,ddn(m,z))
#plt.plot("Diferencias divididas y Polinomio de Newton")
#plt.xlabel("x")
#plt.ylabel("y")
#plt.show()

