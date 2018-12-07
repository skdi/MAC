import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
puntos=100
aux = np.ones((puntos, puntos), dtype=int)

src = np.vstack([np.c_[aux, 2*aux], np.c_[3*aux, 4*aux]])
plt.imshow(src)
plt.show()


def graficar_matriz(src, a):
    M, N = src.shape
    points = np.mgrid[0:N, 0:M].reshape((2, M*N))
    new_points = np.linalg.inv(a).dot(points).round().astype(int)
    x, y = new_points.reshape((2, M, N), order='F')
    indices = x + N*y
    return np.take(src, indices, mode='wrap')

def trans_lineal(x,y,angulo,puntos):
	x1=np.array(range(puntos))
	x2=np.array(range(puntos))
	for i in range(puntos):
		x1[i]=x[i]*np.cos(angulo)-y[i]*np.sin(angulo)#x
		x2[i]=x[i]*np.sin(angulo)+y[i]*np.cos(angulo)#y
	result=np.array([x1,x2])
	return result

def trans_rotacional(vec,angulo):
	A=np.array([[np.cos(angulo),-np.sin(angulo)],[np.sin(angulo),np.cos(angulo)]])
	#print("Matriz rotacional: ",(A))
	return A*vec

def generar_puntos(puntos):
	x1=np.array(range(puntos))
	x2=np.array(range(puntos))
	for i in range(puntos):
		x1[i]=i#x
		x2[i]=i*np.sin(i)#y
	result=np.array([x1,x2])
	return result

a = np.array([[1.5, 0],
              [0, 1]])

x = np.array([-3,4])

#transformacion rotacional
pi=np.pi
trans_rotacional(x,pi)
dst = graficar_matriz(src, trans_rotacional(x,pi/6))
plt.imshow(dst)
plt.show()
##transformacion lineal
x1=np.array(range(puntos))
result=np.array([x1,x1])
original=np.array([x1,x1])

original=generar_puntos(100)
result=trans_lineal(original[0],original[1],pi/6,100)


fig, (ax0) = plt.subplots(nrows=1, figsize=(8, 9))
ax0.plot(original[0], original[1], 'cyan', linewidth=1.5, label='original')
ax0.plot(result[0], result[1], 'red', linewidth=1.5, label='transformada')
ax0.set_title('trans_lineal')
ax0.legend()
plt.show()
