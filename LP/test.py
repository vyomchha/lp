import random
import lp

a = [0 for x in range(1000)]

for x in range(1000):
	a[x] = chr(int(random.uniform(32,122)))

target = open('in.txt', 'w')
target.truncate()

for e in a:
	target.write(e)

target.close()

lp.main()


target = open('out.txt', 'r')
ms = target.read()
target.close()

g=0
b=0
x=0
for e in ms:
	if (e==a[x]): g=g+1
	else: b=b+1
	x=x+1

print float(g)/10
print float(b)/10
