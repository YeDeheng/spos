# -*- coding: utf-8 -*-

from get_data import readSQL
from tokenize import tokenize

import sys,os


def wrapper(istring, ostring):
	q_id = istring
	q_raw_content = q_id + '-raw.txt'
	q_tokenize = q_id + '-tokenized.txt'
	q_pretag = q_id + '-pretagged.txt'

	readSQL.read_knowledge_unit(q_id, q_raw_content)
	
	tokenize.tokenize(q_raw_content, q_tokenize)



if __name__=='__main__':
	try:
		#wrapper(*sys.argv[1:])
		wrapper('1447407', 'out.txt')
	except TypeError: 
		print "Usage : python tokenize.py <input file> <output file>"
