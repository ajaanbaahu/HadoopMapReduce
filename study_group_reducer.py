#!/usr/bin/python

import sys

oldKey=None
posters=[]

for line in sys.stdin:
	# read line from mapper, strip and split the contents
    line=line.strip().split()
	# defensive programming
    if len(line)!=3:
	continue
		
    thisKey,type,user=line[0],line[1],line[2]
	# check if the old key = current key
    if oldKey and oldKey!=thisKey:
	
		print oldKey,"\t",posters
		# assign old key as the current key
		oldKey=thisKey;
		# reset the posters list to empty
		posters=[]


    oldKey=thisKey
# collect the posters
    posters+=[user]

if oldKey!=None:

    print oldKey,"\t",posters

	
