from preprocessor import readMySQL, removeHTML
from tokenizer_so import tokenize

import sys,os

# read the body of the post
body_array = readMySQL.read()

f = open("input_raw.txt", "w")
# remove HTML tags
for row in body_array :
	input_POSTagger = removeHTML.strip_tags(row[0])
	f.write(input_POSTagger)
f.close()
#print input_POSTagger


if __name__=='__main__':
  try:
    tokenize.tokenize(*sys.argv[1:])
  except TypeError: 
    print "Usage : python tokenize.py <input file> <output file>"
    print "See README for input file format"
