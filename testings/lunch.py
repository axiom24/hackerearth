import fileinput
import sys
import math
#writefile=sys.stdout.write
a=[]
printl = [""]*int(10)
indexdata = [""]*int(10)
for l in fileinput.input():
	a.append(l)
temp = a[0][:-1]
temp = temp.split(" ")
maxbox = int(temp[0])
maxwt = int(temp[1])
wtoffood = map(int,a[1].split(" "))
original = wtoffood[:]
temp = [""]*10
for i in range(0,4):
	wtoffood.sort()
	j = 0
	while(j<len(wtoffood)):
		tc = 0
		tc = 0+j
		wtoffood.sort()
		if sum(wtoffood[:j])>maxwt:
			j-=2
			tot = 0
			tot = 0+j
			while(j>=0):
				temp[original.index(wtoffood[j])] = wtoffood[j]
				wtoffood.pop(j)
				j-=1

			midstr = ""
			for k in range(0,len(temp)):
				if temp[k]!="":
					midstr +=" "+str(original.index(temp[k])) 
					 
			printl[i+1] = str(tot)+midstr+"\n"
			temp = [""]*10
			midstr = ''
			j=tc+1
		j+=1

print temp
print printl
print indexdata
print wtoffood
