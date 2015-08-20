# -*- coding: utf-8 -*-

from get_data import readSQL
from tokenize import tokenize
from pretag import transforminput

import subprocess
import sys,os


def wrapper(istring, ostring):
	cur_dir = os.getcwd()
	batch_path = cur_dir + r'\pretag\pretag.bat'  # this is the batch file
	print batch_path

	os.chdir(".\data_final")

	q_id = istring
	q_raw_content = q_id + '-raw.txt'
	q_tokenize = q_id + '-tokenized.txt'
	q_transformin = q_id + '-input2tagger.txt'
	q_pretag = q_id + '-pretagged.txt'

	readSQL.read_knowledge_unit(q_id, q_raw_content)
	tokenize.tokenize(q_raw_content, q_tokenize)
	transforminput.transforminput(q_tokenize, q_transformin)

	os.chdir("..\pretag")

	child = subprocess.Popen([batch_path, "..\\data_final\\" + q_transformin, "..\\data_final\\" + q_pretag])
	stdout, stderr = child.communicate()
	child.wait()	# wait() is important. 
	print("parent process")

	os.chdir("..")

if __name__=='__main__':
	try:
		#wrapper(*sys.argv[1:])
		wrapper('761459', 'out.txt')
	except TypeError: 
		print "Usage : python tokenize.py <input file> <output file>"
