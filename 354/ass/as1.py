# 1(a)
# D={'a':100}
# D['b']=200
# print D

# 1(b)
# D={'b':200,'a':100}
# print D
# del D['b']
# print D

# 1(c)
# L=[100]
# print L
# L.append(200)
# print L

# 1(d)
# L=[100,200]
# print L
# del L[1]
# print L

# 1(e)
# T=(100,200,300)
# a,b,c=T
# print a
# print b
# print c
import random
import math
random.seed(123)
n=30
L=[None]*n
for i in L[:n]:
	r=random.random()
	A=math.pi*math.pow(r,2)
	t=(r,A)
	L.append(t)
print L





