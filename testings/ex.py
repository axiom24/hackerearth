import fileinput as e
import sys
import math
a=[]
for l in e.input():
	a.append(l)
n=int(a[0][:-1])
def c(n,r):
    g=math.factorial
    return g(n)/g(r)/g(n-r)
for i in range(1,n+1):
	t=a[i].split(" ")
	t=map(int,t)
	sys.stdout.write(str(c(t[0],t[1]))+'\n')
		
			




	
		
