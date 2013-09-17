import fileinput
import sys
write=sys.stdout.write
a=[]
for l in fileinput.input():
		a.append(l)

no=a[1]
no=no.split(" ")
a[0]=a[0][:-1]
n=a[0]
n=n.split(" ")
n1=n[0]
n2=n[1]
for i in xrange(0,n1):
	no[i]=int(no[i])
m1=max(no)
m2=min(no)

	
	
	
		