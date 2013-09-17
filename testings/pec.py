import fileinput as e
import sys
a=[]
for l in e.input():
	a.append(l)
n = int(a[0][:-1])
def z(n, r):
		if(n==r):
			return 1
		if(r==1):
			return n
		return z(n-1,r) + z(n-1,r-1)	
for i in range(1,n+1):
	t=a[i].split(" ")
	t=map(int,t)
	sys.stdout.write(str(z(t[0],t[1]))+'\n')
