""" Wrapper for twitter tokenizer. See README for usage instruction"""
"""Kevin Gimpel (kgimpel@cs.cmu.edu)"""
import sys,os
import lib.twokenize

def tokenize(istring,ostring):
  print istring, ostring
  ifile=open(istring,'r')
  ofile=open(ostring,'w')
  for line in ifile:
    ofile.write(u" ".join(lib.twokenize.tokenize(line[:])).encode('utf-8')+'\n')
  ofile.close()
  ifile.close()

if __name__ == '__main__':
  try:
    tokenize(*sys.argv[1:])
  except TypeError: 
    print "Usage : python tokenize.py <input file> <output file>"
    print "See README for input file format"
