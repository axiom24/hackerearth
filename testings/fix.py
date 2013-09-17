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
n1=int(n[0])
n2=int(n[1])
for i in xrange(0,n1):
	no[i]=int(no[i])
print n1/2
for i in xrange(0,n1):
	
