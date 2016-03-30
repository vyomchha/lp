import keygen
import encrypt
import decrypt

ms = raw_input('Enter the message: ')
msg = ''
q=8

for ch in ms:
	i = ord(ch)
	i = int(i)
	m = str(bin(i%q))
	l = len(m)
	mo = "00000000"
	mo = mo[l-2:] + m[2:]
	msg = msg + mo
	
l=len(msg)
n=40
c=10
mu=1
sigma=2
size=1000

a=keygen.gena(n,c)
d=keygen.gend(n,l,mu,sigma,size)
s=keygen.gens(n,l,d,size)
e=keygen.gens(n,l,d,size)
p=keygen.genp(n,l,a,s,e)

e1=encrypt.encl(n,d,size)
e2=encrypt.encl(n,d,size)
e3=encrypt.encl(l,d,size)
c1=encrypt.enc(e1,e2,a,n,n)
c2=encrypt.enc(e1,e3,p,l,n)
for x in range(l):
	c2[x] = c2[x] + int(msg[x]*(q/2))

d1=decrypt.dec(s,c1,c2,l,n)
for x in range(l):
	d2 = d1[x]%q
	if (d2<((3*q)/4) and d2>(q/4)):d1[x]=1
	else:d1[x]=0

out = ''
for x in range(len(ms)):
	o1 = 0
	z = 7
	for y in range(8):
		o1 = o1 + (int(d1[(8*x)+y])*(2**z))
		z = z - 1
	print o1
	out = out + chr(o1)

print "input:\n",ms
print "a:\n",a
print "d:\n",d
print "s:\n",s
print "p:\n",p
print "c1:\n",c1
print "c2:\n",c2
print "d1:\n",d1
print "output:\n",out
