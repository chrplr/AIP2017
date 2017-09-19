#! /usr/bin/env python
# Time-stamp: <2017-09-19 15:35:28 cp983411>

""" computes the sums of two columns form na headerless csv file """

import csv

col1, col2 = 0.0, 0.0
for row in csv.reader(open('test.csv', 'r')):
    col1 += float(row[0])
    col2 += float(row[1])

print(col1, col2)
