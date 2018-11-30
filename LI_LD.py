
import math
import numpy as np
from numpy import matrix , linalg

def imprimir(m):
    a=""
    orden=len(m[0])
    for i in range(orden):
        for j in range(orden):
            a+=str(m[i][j])+'\t'
        print (a)
        a=""

def escalonar( M):
    if not M: return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        M[r] = [ mrx / float(lv) for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
        lead += 1
 
 
M = [
   [ 2,1,1],
   [ 1,2,1],
   [ 1,1,2],]

b = [0,0,0]


def susti_regresiva(M,b):
    n=len(M)
    x = [0.0] * n
    i=n-1
    while(i>=0):
        x[i] = b[i]/M[i][i]
        j=i-1
        while(j>=0):
            b[j]=b[j]-M[j][i]*x[i]
            j=j-1
        i=i-1
    return b

def resolver_gauss(A,b):
    n = len(A)
    M = A
    i = 0
    for x in M:
        x.append(b[i])
        i += 1

    for k in range(n):
        #print ("Iteracion ", k)
        for i in range(k,n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i],M[k]
            else:
                pass

   # Imprimir luego del cambio de filas
        #for row in M:
        #    print (row)
        #print ("")

        for j in range(k+1,n):
            q = M[j][k] / M[k][k]
            for m in range(k, n+1):
                M[j][m] +=  q * M[k][m]

       # Imprimir luego de multiplicacion de columnas
        #for row in M:
        #    print (row)
        #print ("")

    x = [0 for i in range(n)]

    print ("n = ", n)
    print ("x = ", x)
    for row in M:
        print (row)

    x[n-1] =(M[n-1][n])/M[n-1][n-1]
    for i in range (n-1,-1,-1):
        z = 0
        for j in range(i+1,n):
            z = z  + (M[i][j])*x[j]
        x[i] = (M[i][n] - z)/M[i][i]
    print (x)
    return x

def LI_LD(A,b):
    x=resolver_gauss(A,b)
    flag = 0 #0 = LD 1 = LI
    suma = 0
    #comprobando que las soluciones sean diferentes a 0 
    #sol trivial
    for i in range(len(x)):
        flag=flag + x[i]

    if(flag!=0):
        for i in range(len(A)):
            for j in range(len(A)):
                suma=suma+A[i][j]
            if(suma==0):
                flag = 1
                break
            else:
                suma=0

    if(flag==0):
        print("Linealmente Independiente")
    elif(flag!=1):
        print("Linealmente Dependiente")

#LI_LD(M,b)

A = np.array([[ 1,0,0],
   [ 0,1,0],
   [ 0,0,1]])

b = np.array([0,0,0])

def linealmente(A,b):
    x=np.linalg.solve(A,b)
    flag = 0 #0 = LD 1 = LI
    suma = 0

    #comprobando que las soluciones sean diferentes a 0 
    #sol trivial
    for i in range(len(x)):
        flag=flag + x[i]
    if(flag!=0):
        for i in range(len(A)):
            for j in range(len(A)):
                suma=suma+A[i][j]
            if(suma==0):
                flag = 1
                break
            else:
                suma=0
    print ("A:",A)
    print ("x",x)
    v=np.dot(A,x)
    print ("COMPROBACION A*x",v)
    print ("=b",b)

    if(flag==0):
        print("Linealmente Independiente")
    elif(flag!=0):
        print("Linealmente Dependiente")
    if(v.all()==b.all() and flag==0):#si es LI y A*x=b
        print ("A es base de b")
    else:
        print ("A NO es base de b")

def imprimir_v(x):
    a=""
    for i in range(len(x)):
        a+=str(x[i])+','
    print (a)



#escalonar( M )

#for rw in M:
#  print (', '.join( (str(rv) for rv in rw) ) )



linealmente(A,b)
