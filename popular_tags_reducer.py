#!/usr/bin/python

import sys

current_word=None
current_count=0
word=None
# declare a list for top counts
top=[1]*(10)
# declare a list for top tags
top_tag=[1]*(10)

for line in sys.stdin:
	
	# split the data
    data=line.split('\t')
	# defensive programming
    if len(data)!=2:
        continue

    word,count=data
    # check if the current word is = the previous word
    if current_word and current_word!=word:
		# iteratively traverse the list and check the value for the elements against the current count
        for index, item in enumerate(top):
		# replace existing value if the count is more than the value currently in the list
            if item<current_count:
			
                top[index]=current_count
				# insert the current word at the index 
                top_tag[index]=current_word
                break
		# assign current_word to the word received
        current_word=word
		# resent current count= 0
        current_count=0

    current_word=word
	# add to the count for every subsequent occurrence of the word
    current_count+=int(count)
print zip(top_tag,top)
