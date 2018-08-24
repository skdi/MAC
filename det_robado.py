import math


def determinante(A,filas,cols):
  if(filas!=cols):
  	return
  elif filas==1 and cols==1:
  	return A[0][0]
  elif filas==2 and cols==2:
  	return A[0][0]*A[1][1]-A[1][0]*A[0][1]
  else:
	det = 0
	for i in range (cols):
	    det += ((-1)**(1+i))*A[1][i]*abs(determinante(A,filas-1,cols-1))
  return det

def det(l):
    tamaño=len(l)
    if (tamaño>2):
        i=1
        t=0
        sum=0
        while t<=tamaño-1:
            d={}
            t1=1
            while t1<=tamaño-1:
                m=0
                d[t1]=[]
                while m<=tamaño-1:
                    if (m==t):
                        u=0
                    else:
                        d[t1].append(l[t1][m])
                    m+=1
                t1+=1
            l1=[d[x] for x in d]
            sum=sum+i*(l[0][t])*(det(l1))
            i=i*(-1)
            t+=1
        return sum
    else:
        return (l[0][0]*l[1][1]-l[0][1]*l[1][0])

A=[[1,2,3],[4,5,6],[7,8,9]]
det=det(A)
print det

