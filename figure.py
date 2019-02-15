import numpy as np
import matplotlib.pyplot as plt

def dir_vec(AB):
	return np.matmul(AB,dvec)

def norm_vec(AB):
	return np.matmul(omat, np.matmul(AB, dvec))

r=1
len=1000
t=np.linspace(0, 2*np.pi, len)
C=np.array([-3, 0])
x=C[0]+r*np.cos(t)
y=C[1]+r*np.sin(t)
plt.plot(x, y)

x2=np.linspace(-10, 10, 500)
y2=-x2**2/4
plt.plot(x2, y2, 'r')

A=np.array([0,1])
B=np.array([-5,-4])
len1 = 10

lam_1=np.linspace(0,1,len1)

x_AB=np.zeros((2,len1))
for i in range(len1):
	temp1=A + lam_1[i]*(B-A)
	x_AB[:,i]=temp1.T
	
plt.plot(x_AB[0,:],x_AB[1,:],label='$Tangent$')


P=np.array([-2,-1])
dvec=np.array([-1,1]).T
omat=np.array([[0,1],[-1,0]])
AB=np.vstack((A,B)).T
x_PX=np.zeros((2,len1))
for i in range(len1):
	temp1=P + lam_1[i]*norm_vec(AB)
	x_PX[:,i]=temp1.T
	
plt.plot(x_PX[0,:],x_PX[1,:],label='$Normal$')

plt.plot(P[0], P[1], 'o')
plt.text(P[0]*(1-0.1), P[1]*(1+0.1), 'P')
plt.plot(C[0], C[1], 'o')
plt.text(C[0]*(1-0.1), C[1]*(1-0.01), 'C')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
ax = plt.gca()
ax.set_xlim((-6,6))
ax.set_ylim((-4,4))
plt.grid()
plt.show()
