#!/usr/bin/python

import sys
oldKey=None
qLength=0
avgLength=0
counter=0

for line in sys.stdin:
	# read line from mapper, strip and split the contents
    line=line.strip().split()
	# defensive programming
    if len(line)!=4:
        continue
	# map the data
    thisKey,type,length= line[0],line[2],line[3]
	
	# if current key is not = previous key, then print the final result for the previous key
    if oldKey and oldKey!=thisKey:
		
		# if the question has answers then counter will not be = 0
        if counter!=0:
            print oldKey,"\t",qLength,"\t",(avgLength/counter)
        else:
		# if the question does not have answers then counter will be = 0, in that case average length of answer =0
            print oldKey,"\t",qLength,"\t",0
			
		# assign new key as the current key	
        oldKey=thisKey
		# reset average length of answer =0
        avgLength=0
		# reset counter =0
        counter=0
	# check if type is question
    if type=="question":
        qLength=int(length)

        length=0
        counter=0
	
    oldKey=thisKey
    # update the average length of answer with each new answer length received
	avgLength+=float(length)
    if type=='answer':
		# count the number of answers
        counter+=1


if oldKey!=None:
    if counter!=0:
            print oldKey,"\t",qLength,"\t",(avgLength/counter)
    else:
	print oldKey,"\t",qLength,"\t",0

