#!/usr/bin/env python
from operator import itemgetter
import sys
from math import sqrt
import matplotlib as plt

def standard_deviation(lst):
    """Calculates the standard deviation for a list of numbers."""
    num_items = len(lst)
    mean = sum(lst) / num_items
    differences = [x - mean for x in lst]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
    variance = ssd / num_items
    sd = sqrt(variance)
    return sd

current_word = None
current_count = 0
word = None
dict = {}
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            # print '%s\t%s' % (current_word, current_count)
            dict[current_word]=current_count
        current_count = count
        current_word = word
# do not forget to output the last word if needed!
#if current_word == word:
    #print '%s\t%s' % (current_word, current_count)


#print (dict)
k = dict.values()
max1=max(k)
min1=min(k)
avg=sum(k)/len(k)
sd = standard_deviation(k)

print ("Maximum: ",max1)
print ("Minimum: ",min1)
print ("Average: ",avg)
print ("Standard Deviation: ", sd)

