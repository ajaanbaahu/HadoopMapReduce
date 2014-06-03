#!/usr/bin/python

import sys
import csv

def mapper():
	# read the csv file using the csv module
    reader = csv.reader(sys.stdin, delimiter='\t')
   

    for line in reader:
		#check if the length of the data read is 19 and skip if header line
        if len(line)!=19 or line[0]=='id':
            continue
	# check if the entry is of answer and question
	if line[5]!='comment':
	
		# 	if the entry is question then it wont have an abs_parent_id, in that case assign the id as the abs_parent_id 
		if line[7]=='\N':
		    line[7]=line[0]
			# collect abs_parent_id, id, node_type, and length of the body
	            print "{0}\t{1}\t{2}\t{3}".format(line[7],line[0],line[5],len(line[4]))
		else:
		    print "{0}\t{1}\t{2}\t{3}".format(line[7],line[0],line[5],len(line[4])) 

	

proj=mapper()
