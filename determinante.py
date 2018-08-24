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
  
A=[[1,2,3],[4,5,6],[7,8,9]]
det=determinante(A,len(A),len(A[0]))
print det

