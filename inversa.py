import math

def identidad(n):
	m=[[0]*n]*n
	i=0
	while i<n:
	    m[i][i]=1
	    i+=1
	return m

def zeros(n):
	m=[[0]*n]*n
	return m


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

def det(m): 
    orden=len(m[0])
    if orden==2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    else:
        j=0
        for i in range(orden):
            n=copia(m) 
 #            print n[0][i]
            for k in range(orden):
#                print i, k
                n[k].pop(i)
#                print n
            n.pop(0)
            j=j+m[0][i]*(-1)**(i+k)*det(n)
    return j

def cofactor(m,a,b):
	orden=len(m[0])
	i=0 
	j=0
	temp=zeros(orden)
	for row in range(orden):
		for col in range(orden):
			if(row!=a and col!=b):
				temp[i][j]=m[row][col]
				j+=1
				if(j==orden-1):
					j=0
					i+=1
	return temp

def m_cofactor(m):
	orden=len(m[0])
	cof=zeros(orden)
	for i in range(orden):
		for j in range(orden):
			cof[i][j]=((-1)**(i+j))*(det(cofactor(m,i,j)))
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

def inversa_cof(m):
	detx=det(m)
	if(detx==0):
		print("la matriz no tiene inversa")
		return
	else:
		Adj=traspuesta(m_cofactor(m))
		orden=len(Adj[0])
		for i in range(orden):
			for j in range(orden):
				Adj[i][i]/=abs(detx)

	imprimir(Adj)
	return Adj



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




def imprimir(m):
	a=""
	orden=len(m[0])
	for i in range(orden):
		for j in range(orden):
			a+=str(m[i][j])+'\t'
		print (a)
		a=""

A=[[1,2,3],[3,2,1],[1,1,0]]
b=[2,-1,6]			

inversa_cof(A)
