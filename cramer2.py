import math


def copia(m):
    result=[]
    for f in m:
        result.append(f[:])
    return result
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
 


A=[[2,1,-1],[-1,-1,-1],[6,2,1]]
b=[2,-1,6]
cramer(A,b)

