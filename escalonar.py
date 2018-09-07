import math

def escalona(m):
	a=1
	orden=len(m[0])
	for i in range(a,orden):
		for ii in range(2,orden):
			if(m[i][i]<m[ii][i]):
				for j in range(0,orden):
					x=m[i][j]
					m[i][j]=m[ii][j]
					m[ii][j]=x

	for ii in range(1,orden):
		x=m[ii+a][a]
		y=m[a][a]
		for j in range(1,orden):
			m[ii+a][j]=m[ii+a][j]-(x/y)*m[a][j]
		a+=1

def escalona2(m):
	diagonaliza(m)
	orden=len(m[0])
	for k in range(0,orden):
		for i in range(k,orden):
			if(m[k][k]!=0):
				z=m[i][k]/m[k][k]
				m[i][k]=0
				for j in range(k,orden):
					m[i][j]=m[i][j]-z*m[k][j]
	imprimir(m)

def diagonaliza(m):
	orden=len(m[0])
	for i in range(0,orden):
		for k in range(i+1,orden):
			if(abs(m[i][i])<abs(m[k][i])):
				for j in range(0,orden):
					temp=m[i][j]
					m[i][j]=m[k][j]
					m[k][j]=temp
	

def escalonar(m):
	diagonaliza(m)
	orden=len(m[0])
	for j in range(1,orden-1):
		for i in range(j,orden):
			if(i>j):
				z=m[i][j]/m[j][j]
				m[i][j]=0
				for k in range(0,orden):
					if(A[i][i]==0):
						for i in range(0,orden):
							may=abs(m[i][i])
							fmay=i
							for j in range(i,orden):
								if(abs(m[j][i])>may):
									may=abs(m[j][i])
									fmay=j
							for k in range(0,orden):
								paso=m[i][k]
								m[i][k]=m[fmay][k]
								m[fmay][k]=paso
					else:
						m[i][k]=round(m[i][k]-z*A[j][k])
	imprimir(A)


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
imprimir(A)
print ("")
escalona(A)
