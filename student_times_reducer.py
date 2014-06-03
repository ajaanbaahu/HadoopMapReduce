#!/usr/bin/python

import sys
from itertools import groupby

file =sys.stdin

#read the input from mapper strip and split the contents
lines = (line.split() for line in file if line.strip())

# for every lines, group by the author id and 
# lambda x: x[0]" tells groupby() to use the first item in each tuple as the grouping key

for id, same_id in groupby(lines, key=lambda x: x[0]): # group by author_id
	
	
    max_time=[]

    max_count = 0


    for time, same_time in groupby(same_id, key=lambda x: x[1]): #group by time_added
	
	#calculate the count if length of data matches the required length
	count=sum(int(x[2]) if len(x) >2 else 0 for x in same_time)
       
		# resolve ties
        if count == max_count:

            max_time += ''.join(' '+time)


            max_count=count

		# get the max count
        elif count > max_count:
            max_time, max_count = time, count
    print("{0}\t{1}".format(id, max_time))

