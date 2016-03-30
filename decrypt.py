def dec(s,c1,c2,n1,n2):
	p = [0 for x in range(n1)]
	for x in range(n1):
		n=0
		for y in range(n2):
			p[x] = p[x] + (s[x][y]*c1[n])
		n=n+1

	for x in range(n1):
		p[x] = p[x] + c2[x]

	return p
