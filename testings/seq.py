
import fileinput
import sys
write=sys.stdout.write
a=[]
for l in fileinput.input():
		a.append(l)
n = int(a[0][:-1])
no=a[1]
no=no.split(" ")
c=0
for i in xrange(0,n):
	no[i]=int(no[i])
for x in xrange(0,n-1):
	
	no[x+1]=no[x+1]-no[x]
	no[x]=0
		
		
for j in xrange(0,n):
	if(no[j]!=0):
		c=1
		break
		
if(c==0):
	write("YES")
elif(c==1):
	write("NO")
		
	
				
	
	


		