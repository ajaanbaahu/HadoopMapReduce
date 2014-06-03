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
    # collect all the tags and split into individual words				
	tag=line[2].split()
	
	# for each word in tag print the word and append 1 
	for word in tag:
	    print "{0}\t{1}".format(word,1) 
	

proj=mapper()
