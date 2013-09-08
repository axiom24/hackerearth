def is_palindrome( int_in_question) :
    
    x = list( str( int_in_question))
    reversed_list_of_chars = list(x)
    reversed_list_of_chars.reverse( )
    return x == reversed_list_of_chars

import math
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
    
    for j in range(max+1) :
        if  is_palindrome(j) :
            if is_palindrome( j * j) :
               c+=1

    fout.write("Case #"+str(i+1)+": "+str(c)+"\n")          