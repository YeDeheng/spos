# -*- coding: utf-8 -*-

from get_data import readSQL
from tokenize import tokenize
from pretag import transforminput
from pretag import transformoutput


import shutil
import MySQLdb
import subprocess
import sys,os


def wrapper(istring, annotator, index):
	cur_dir = os.getcwd()
	batch_path = cur_dir + r'\pretag\pretag.bat'  # this is the batch file
	print batch_path

	os.chdir(".\data_final")

	q_id = istring
	q_raw_content = annotator + q_id + '-raw.txt'
	q_tokenize = annotator + q_id + '-tokenized.txt'
	q_transformin = annotator + q_id + '-input2tagger.txt'
	q_pretag = annotator + q_id + '-pretagged.txt'
	q_final = annotator + q_id + '-final.txt'


	readSQL.read_knowledge_unit(q_id, q_raw_content)
	tokenize.tokenize(q_raw_content, q_tokenize)
	transforminput.transforminput(q_tokenize, q_transformin)

	os.chdir("..\pretag")

	child = subprocess.Popen([batch_path, "..\\data_final\\" + q_transformin, "..\\data_final\\" + q_pretag])
	stdout, stderr = child.communicate()
	child.wait()	# wait() is important. 
	print("parent process")

	os.chdir("..\data_final")

	transformoutput.transformoutput(q_id, q_pretag, q_final)
	shutil.copy2(q_final, annotator+str(index)+'.automatic_tags')

	os.chdir("..")

	print("program finish")


def get_postid():
	db = MySQLdb.connect(host="localhost", 
	                     user="root", 
	                     passwd="ydh0114", 
	                     db="stackoverflow201503")
	cur = db.cursor() 
	cur.execute(" SELECT Id FROM posts where Tags like '%<java>%' and Tags like '%<javascript>%' LIMIT 120")
	id = cur.fetchall()
	print id

if __name__=='__main__':
	#wrapper('1158557', 'testliuyi', 1)

	annotators = ['liuyi']#['zhenchang', 'gaosa', 'chunyang', 'lijing', 'lingfeng', 'xuejiao']
	try:
		#wrapper(*sys.argv[1:])
		for anno in annotators:
			f = open(anno + '.txt', 'r')
			for index, line in enumerate(f):
				line = line.strip()
				wrapper(str(line), anno, index+1)
	except TypeError: 
		print "Usage : python tokenize.py <input file> <output file>"
