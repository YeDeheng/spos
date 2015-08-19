"""Python script to transform tokenizer's output file (format:one tweet per line) to input format of the POS tagger (one token per line)""" 
"""Dani Yogatama (dyogatama@cs.cmu.edu)"""

import sys,os

def transforminput(istring,ostring):
  ifile=open(istring,'r')
  ofile=open(ostring,'w')
  for line in ifile:
    tokens=line.split()
    for t in tokens:
      ofile.write(t+'\tN\n')
    ofile.write('\n')
  ofile.close()
  ifile.close()

if __name__=='__main__':
  try:
    transforminput(*sys.argv[1:])
  except TypeError:
    print "Usage : python transforminput.py <input file> <output file>"
