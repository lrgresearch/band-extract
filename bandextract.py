#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Author:     Dr. S. Bora Lisesivdin <bora@gazi.edu.tr>,
  Program:    bandextract.py
  Date:       Jan. 03, 2012

  Description:  Band structure parser for ATK for easy 
  importing with Excel or any scientific graphing software
"""
# PARAMETERS
# Filenames
file = "N09-dope01son.txt"
output = "output.txt"
# Do you want single-X-axis? (yes/no) (Default:No)
singlex = "yes"
# Number of bands including spin up and down
numberofdatagroup = 104
#Number of data in each band
data = 41

# DEFAULT SETTINGS
# Number of lines of header (default)
header = 12
# Number of lines before each data (default)
predata = 1
# Number of lines after each data (default)
postdata = 1

# - - - - - - - - - PROGRAM - - - - - - - - - - 
# create a  matrix of zeroes
arr = [[0 for col in range(2*numberofdatagroup)] for row in range(data)]
f = open(file, 'r')
lines = f.readlines()
f.close()
a = header 

for i in range(0, numberofdatagroup, 1):
   b = 0
   a = a + predata
   for a in range (a, a+data, 1):
      fields = lines[a].split()
      arr[b][2*i] = fields[0]
      arr[b][2*i+1] = fields[1]
      b = b + 1
   a = a + postdata+1

# writing to output file
f = open(output, 'w+')
stringline = ""

if singlex == "yes":
   for i in range(0, data, 1):
      stringline = stringline + arr[i][0] + " " + arr[i][1] + " "
      for j in range(1, numberofdatagroup, 1):
         stringline = stringline + arr[i][2*j+1] + " "
      f.write(stringline + "\n")
      stringline = ""
else:
   for i in range(0, data, 1):
      for j in range(0, numberofdatagroup, 1):
         stringline = stringline + arr[i][2*j] + " " + arr[i][2*j+1] + " "
      f.write(stringline + "\n")
      stringline = ""
f.close()
print "Output file is finished."

   


