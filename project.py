import numpy as np
import matplotlib.pyplot as plt
import sympy

V=sympy.Matrix([[1, 0], [0, 0]])
U=np.array([0, 2])
F=np.array([0])
C=np.array([-3, 0])
k=sympy.symbols('k', real=True)
K= sympy.Matrix([[k, 0], [0, k]])

X=(K.multiply(C)-U)
Y=(V.T+K).inv()
P1=Y.multiply(X)
P=P1.T
Z=P.multiply(V.multiply(P.T))+2*P.multiply(U.T)
k=sympy.solve(Z, k)
k=k[0]

x=int(k[0])
K=np.array([[x, 0],[0, x]])
C2=np.array([-3, 0])
K = K.T
X=np.matmul(K, C) - U
Y=(V.T+K).inv()
P1=Y.multiply(X)
P=P1.T
p=int(P[0])
p1=int(P[1])
P=np.array([p,p1])

normal = (V.T).multiply(P) + U 		#equation of normal
n=int(normal[0])
n1=int(normal[1])
normal=np.array([n,n1])
lambda1=np.matmul(-P, U.T) - F		#equation of lambda

print('The Equation of the tangent is :\n', normal, 'x =', lambda1 )
