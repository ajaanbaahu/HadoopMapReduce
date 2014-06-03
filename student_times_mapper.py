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


		#collect the author id and time the comment was added at
        l=[line[3],line[8][11:13]]

		# print the author id, time comment added and append 1
        print ("{0}\t{1}\t{2}".format(line[3],line[8][11:13],1))

mapper()
