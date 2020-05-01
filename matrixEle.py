from sympy.physics.wigner import wigner_3j
from sympy.physics.wigner import clebsch_gordan
import math
import numpy as np

def TwoBodyElement(Q1,Q2,m1p,m2p,m1,m2,l):
	result = 0.0
	for lp in range(0,int(2*l+1)):
		for mp in range(-lp,lp+1):
			tmp = (-1)**(-m2p-m1p-mp)
			try:
				tmp *= wigner_3j(l,lp,l,-Q1,0,Q1)*wigner_3j(l,lp,l,m2p,-mp,-m2)*wigner_3j(l,lp,l,m1p,mp,-m1)*wigner_3j(l,lp,l,-Q2,0,Q2)
			except:
				tmp *= 0.0
			result += tmp
	return ((2*l+1)**2)*((-1)**(Q1+Q2))*result

def DoubletTwoBodyElement(Q,m1p,m2p,m1,m2,l):
	return 0.25*(TwoBodyElement(Q+2,Q+2,m1p,m2p,m1,m2,l)+TwoBodyElement(Q+2,Q,m1p,m2p,m1,m2,l)+TwoBodyElement(Q,Q+2,m1p,m2p,m1,m2,l)+TwoBodyElement(Q,Q,m1p,m2p,m1,m2,l))

def Kdelta(i,j):
	if i==j:
		return 1.0
	else:
		return 0.0
def PseudoPotential(n,l,m):
	sumrange = np.linspace(-l,l,int(2*l)+1,endpoint=True)
	result = 0.0
	for m1 in sumrange:
		for m2 in sumrange:
			for m3 in sumrange:
				for m4 in sumrange:
					tmp = Kdelta(m1+m2,m3+m4)*Kdelta(m1+m2,2*l-m)
					#try:
					tmp*=clebsch_gordan(l,l,2*l-m,m1,m2,m1+m2)*clebsch_gordan(l,l,2*l-m,m3,m4,m3+m4)*DoubletTwoBodyElement(l-n,m4,m3,m2,m1,l)
					#except:
					#	tmp*=0.0
					result += tmp
	return result/math.sqrt(float(l-n))


if __name__ == '__main__':
	Q = 2.5
	n = 3
	l = Q+n
	f = open("fluxEq{}in{}thLL.csv".format(Q,n),"a+")
	#tmp = PseudoPotential(2,3,1)
	#print(tmp)
	#f.write("{},{}\n".format(1,tmp))
	
	for m in range(int(2*(Q+n))):
		print("computation {} starts".format(m))
		tmp = PseudoPotential(n,n+Q,m)
		f.write("{},{}\n".format(m,tmp))
		print("computation {} is done".format(m))
	f.close()

	#tmp = PseudoPotential(2,2+3.5,11)
	#print(tmp)
