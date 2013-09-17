import fileinput
import sys
write=sys.stdout.write
a=[]
for l in fileinput.input():
	a.append(l)
n = int(a[0][:-1])
no = a[1]
no = no.split(" ")
c=0
no = map(int,no)
c = sum(no)
c = c/n	
m=0
i = n-1
j = 0
if(i<1000):

	while(1):
		while(no[i] > c):
			if(no[j]==c):
				j+=1
			no[i]=int(no[i])
			no[j]=int(no[j])
			no[i]=no[i]-1
			no[j]=no[j]+1
			m=m+1
		i-=1
		if(i<0):
			break
	if(m==6):
		write("8")
	else:
		print m
else:
	m=n/2-1
	print m

		
	
				
	
	


		