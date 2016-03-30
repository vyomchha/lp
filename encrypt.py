import random

def encl(n,d,size):
	s = [0 for x in range(n)]
	for x in range(n):
		s[x] = d[int(random.random()*size)]
	return s

def enc(e1,e2,a,n1,n2):
	p = [0 for x in range(n1)]
	for x in range(n1):
		n=0
		for y in range(n2):
			p[x] = p[x] + (a[x][y]*e1[n])
		n=n+1

	for x in range(n1):
		p[x] = p[x] + e2[x]

	return p

