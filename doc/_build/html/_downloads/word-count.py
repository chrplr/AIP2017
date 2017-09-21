"""
    Count the number of occurrences of words in a text file

   Count the number of occurrences of words in a text file

"""

import operator  # to sort the dictionary 'count'
import sys
import string

filename = sys.argv[1]  # reads the filename as a command line argument

f = open(filename, 'r')

text = f.read()

translator = str.maketrans('', '', string.punctuation)
text = text.translate(translator)  # suppress punctuation signs

words = text.split()

counts = {}

for w in words:
    if w.lower() in counts.keys():
         counts[w.lower()] += 1
    else:
         counts[w.lower()] = 1


# black magic follows:
sorted_counts = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
for w, n in sorted_counts:
    if n < 10:
        break
    print("%20s : %5d" % (w, n)) 
    
