# -*- coding: utf-8 -*-
import os

if __name__=='__main__':
	#wrapper('12750691', 'testliuyi', 1)

	annotators = ['wentao', 'ziqun', 'liuyi', 'zhenchang', 'gaosa', 'chunyang', 'lijing', 'lingfeng', 'xuejiao']
	
	try:
		#wrapper(*sys.argv[1:])
		for anno in annotators:
			f = open(anno + '.txt', 'r')
			os.chdir("./baseline1/tagged_by_ST")
			for index, line in enumerate(f):
				line = line.strip()
				filename_id = anno + line + '-tokenized.txt.ST.mapped'
				filename_index = anno + str(index+1) + '-tokenized.txt.ST.mapped'
				print filename_id, filename_index
				os.rename(filename_id, filename_index)
				#wrapper(str(line), anno, index+1)
			os.chdir("../../")
	except TypeError: 
		print "Usage : python tokenize.py <input file> <output file>"
