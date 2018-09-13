import math


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




def imprimir(m):
	a=""
	orden=len(m[0])
	for i in range(orden):
		for j in range(orden):
			a+=str(m[i][j])+'\t'
		print (a)
		a=""

A=[[2,1,-1],[-1,-1,-1],[6,2,1]]
b=[2,-1,6]			

det_por_propiedad(A)
