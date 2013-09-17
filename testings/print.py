def main():
	
	
	fin=open("small.in","r")
	fout=open("output.txt","w")
	line=fin.readlines()
	line[0]=line[0][:-1]
	totalcases = int(line[0])
	line.pop(0)
	for i in range(0,totalcases*2+1):
		line[i] = line[i][:-1]
	print(totalcases)	
	print(line)
	
	no=[line[i+1:i+3] for i in range(0,len(line),3)]
	for i in range(0,totalcases):
		x=line[i*3]
		v1=no[i][0].split(" ")
		v2=no[i][1].split(" ")
		v1=map(int,v1)
		v2=map(int,v2)
		v1=sorted(v1)
		v2=sorted(v2)
		v2.reverse()
		min = 0
		for j in range(0,int(x)):
			min = min + v1[j]*v2[j]
		fout.write("Case #"+str(i+1)+": "+str(min)+"\n")
		print(min)
		print(v1)
		print(v2)
				
	
	

if __name__=="__main__":
		main()
		