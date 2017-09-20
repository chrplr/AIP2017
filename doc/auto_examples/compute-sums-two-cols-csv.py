#! /usr/bin/env python
# Time-stamp: <2017-09-20 13:16:25 cp983411>

""" 
    Computes the sums of two columns from an headerless csv file.

    Computes the sums of two columns from an headerless csv file.
"""

import csv

col1, col2 = 0.0, 0.0
for row in csv.reader(open('test.csv', 'r')):
    col1 += float(row[0])
    col2 += float(row[1])

print(col1, col2)
