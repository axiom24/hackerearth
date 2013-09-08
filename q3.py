import math
def is_square(n):
	return math.sqrt(n).is_integer()

fin=open("input.in","r")
fout=open("output.txt","w")
line=fin.readlines()
line[0]=line[0][:-1]
totalcases = int(line[0])
line.pop(0)
for i in xrange(0,totalcases-1):
	line[i] = line[i][:-1]


for i in xrange(0,totalcases):
	r=line[i].split(" ")
	low=int(r[0])
	high=int(r[1])
	min=int(math.ceil(math.sqrt(low)))
	max=int(math.floor(math.sqrt(high)))
	c=0
	fil=[]
	
	for j in xrange(min,max+1):
		if str(j)==str(j)[::-1]:
			if str(j*j) == str(j*j)[::-1]:
				c +=1 						
	fout.write("Case #"+str(i+1)+": "+str(c)+"\n")
			
	
	


		