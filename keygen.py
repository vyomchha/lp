import random
import numpy as np

def gena(n,c):
	a = [[0 for x in range(n)] for x in range(n)]
	for x in range(n):
		for y in range(n):
			a[x][y] = int(random.random()*c)

	return a

def gend(n,l,mu,sigma,size):
	d = np.random.normal(mu, sigma, size)
	return d

def gens(n,l,d,size):
	s = [[0 for x in range(n)] for x in range(l)]
	for x in range(l):
		for y in range(n):
			s[x][y] = d[int(random.random()*size)]
	return s

def genp(n,l,a,s,e):
	p = [[0 for x in range(n)] for x in range(l)]
	for x in range(l):
		for y in range(n):
			for z in range(n):
				p[x][y] = p[x][y] - (s[x][z]*a[z][y])

	for x in range(l):
		for y in range(n):
			p[x][y] = p[x][y] + e[x][y]

	return p
