
import math
import numpy as np
from numpy import matrix , linalg

def identidad(n):
    m=[[0]*n]*n
    i=0
    while i<n:
        m[i][i]=1
        i+=1
    return m

def zeros(n):
    matriz = [None] * n
    for i in range(n):
        matriz[i] = [None] * n
    return matriz

def copia(m):
    result=[]
    for f in m:
        result.append(f[:])
    return result

def cambiarfila(m,a,b):
    i=m[a]
    m[a]=m[b]
    m[b]=i
    return m
#trabajo labo 1
def det(m): 
    orden=len(m[0])
    if orden==2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    else:
        j=0
        for i in range(orden):
            n=copia(m) 
            for k in range(orden):
                n[k].pop(i)
            n.pop(0)
            j=j+m[0][i]*(-1)**(i+k)*det(n)
    return j

#trabajo labo2
def cramer(m,b):
  c=copia(m)
  x=[]
  for i in range(0,len(b)):
      for j in range(0,len(b)):
          c[j][i]=b[j]
          if i>0:
              c[j][i-1]=A[j][i-1]
      x.append(round(det(c)/det(m),1))
  for i in range(len(b)):
    print (x[i])
  return x


#trabajo labo3
def det_por_propiedad(m):
    imprimir(m)
    print ("")
    orden=len(m[0])
    perm=0
    det=1
    noreg=0
    for col in range(0,orden):
        nocero=0
        a=col
        while((nocero==0) and (a<orden)):
            if(m[a][col]!=0):
                nocero=1
            else:
                a+=1
        if(a>orden):
            noreg=1
            break
        elif(a!=col):
            perm+=1
        pivot=m[a][col]
        for c1 in range(0,orden):
            v1=m[a][c1]
            m[a][c1]=m[col][c1]
            m[col][c1]=v1
        imprimir(m)
        print ("")
        for c2 in range(0,orden):
            v1=m[c2][col]
            for c1 in range(col,orden):
                m[c2][c1]=m[c2][c1]-((v1/pivot)*m[col][c1])
    
    for c2 in range(0,orden):
        det=det*m[c2][c2]
    a=perm
    if(a%2==1):
        det=-det
    if(noreg==1):
        det=0
    print ("El determinante de la matriz es: ", det)
    return m


#trabajo labo4
def inversa_cof(m):
    orden=len(m[0])
    inver=zeros(orden)
    detx=det(m)
    if(detx==0):
        print("la matriz no tiene inversa")
        return
    else:
        Adj=m_adjunta(m)
        for i in range(orden):
            for j in range(orden):
                inver[i][j]=Adj[i][j]/detx

    imprimir(inver)
    return inver



def cofactor(m,a,b):
    orden=len(m[0])
    i=0 
    j=0
    temp=zeros(orden-1)
    for row in range(orden):
        for col in range(orden):
            if(row!=a and col!=b):
                temp[i][j]=m[row][col]
                j+=1
                if(j>=(orden-1)):
                    j=0
                    i+=1
    return (-1.0)*(a+b)*det(temp)

def m_cofactor(m):
    orden=len(m[0])
    cof=zeros(orden)
    for i in range(orden):
        for j in range(orden):
            cof[i][j]=cofactor(m,i,j)
    imprimir(cof)
    return cof

def traspuesta(m):
    orden=len(m[0])
    for i in range(1,orden):
        for j in range(0,i):
            temp=m[i][j]
            m[i][j]=m[j][i]
            m[j][i]=temp
    return m

def m_adjunta(m):
    orden=len(m[0])
    temp=m_cofactor(m)
    adj=zeros(orden)
    for i in range(orden):
        for j in range (orden):
            adj[j][i]=temp[i][j]
    return adj


def inversa_elemental(m):
    if(det_por_propiedad(m)==0):
        print("la matriz no tiene inversa")
        return
    else:
        orden=len(m[0])
        I=identidad(orden)
        for i in range(0,orden):
            if(m[i][i]!=0):
                m[i][i]/=m[i][i]
            else:
                m=cambiarfila(m,i,i+1)

            m[i+1]-=(m[i+1][i])*m[i]
    return m



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
    elif(flag==1):
        print("Linealmente Dependiente")




def imprimir_v(x):
    a=""
    for i in range(len(x)):
        a+=str(x[i])+','
    print (a)



#escalonar( M )

#for rw in M:
#  print (', '.join( (str(rv) for rv in rw) ) )

#resolver_gauss(M,b)
LI_LD(M,b)
