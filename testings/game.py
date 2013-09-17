import fileinput
import sys
write=sys.stdout.write
a=[]
for l in fileinput.input():
	a.append(l)
n = int(a[8])
p = []
for j in range(0,8):
	a[j] = a[j][:-1]
	p.append(map(int,a[j].split(" ")))

if(n==1):
	i=7
	j=7
	while(j>0):
		if(p[j][i]==0):
			x=str(i)
			y=str(j)
			write(x+" "+y)
			break
			
		else:
			if(p[j-1][i]!=2):
				j=j-1
			else:
				i=i-1
	
	
if(n==2):
	coord=10
	if p[7][0]==0 and p[7][7]==0:
		for i in range(0,8):
			for j in range(0,8):
				if p[i][j]==0:
					continue
				else:
					coord = j
					break
	
	i=7
	j=7
	if coord!=10:
		if coord<=3:
			i = 0
			j = 7
			while(i<8):
				if(p[j][i]==0):
					x=str(i)
					y=str(j)
					write(x+" "+y)
					break
				else:
					if(p[j][i+1]!=1):
						i=i+1
					else:
						j=j-1
						
		
		
		else:
			
			while(i>0):
				if(p[j][i]==0):
					x=str(i)
					y=str(j)
					write(x+" "+y)
					break
				else:
					if(p[j][i-1]!=1):
						i=i-1
					else:
						j=j-1
						i=i-1
			
			
	else:
		
		if p[7][7]!=0:
			while(i>0):
					if(p[j][i]==0):
						x=str(i)
						y=str(j)
						write(x+" "+y)
						break
					else:
						if(p[j][i-1]!=1):
							i=i-1
						else:
							j=j-1
							i=i-1
		else:
			i = 0
			j = 7
			while(i<8):
				if(p[j][i]==0):
					x=str(i)
					y=str(j)
					write(x+" "+y)
					break
				else:
					if(p[j][i+1]!=1):
						i=i+1
					else:
						j=j-1
						
		