import sys,os
import re

def transformoutput(id, istring, ostring):
  ifile=open(istring,'r')
  ofile=open(ostring,'w')
  token = ''
  tag = ''
  for line in ifile:
    if line.strip():
      tokens=line.split()
      token += tokens[0] + ' '
      tag += tokens[1] + ' '
    else:
      token = re.sub(' $', '', token)
      tag = re.sub(' $', '', tag)
      ofile.write(id + '\t' + token + '\t' + tag + '\n')
      token = ''
      tag = ''
    # for t in tokens:
    #   ofile.write(t+'\tN\n')
    # ofile.write('\n')
  ofile.close()
  ifile.close()

if __name__=='__main__':
  try:
    transformoutput('123','sample-output.txt','asdfasfas.txt')
    #transforminput(*sys.argv[1:])
  except TypeError:
    print "Usage : python transformoutput.py <id> <input file> <output file>"
