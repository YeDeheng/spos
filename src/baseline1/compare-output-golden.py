
mapped_tag_list = ['O', 'N', '^', 'V', 'A', 'R', '!', 'D', 'P', 'T', 'X', '&', '$', 'G']

def compare(istring1, istring2):
	test = open(istring1, 'r')
	gold = open(istring2, 'r')
	
	tags_test = []
	tags_gold = []
	for line in test:
		tag = line.split()[1]
		tags_test.append(tag)
	for line in gold:
		tag = line.split()[1]
		tags_gold.append(tag)

	if len(tags_test) == len(tags_gold):
		equals = 0
		total = 0
		for i, j in zip(tags_test, tags_gold):
			if j in mapped_tag_list:
				total += 1
				if i == j:
					equals += 1
	print (equals, total)
	return equals/float(total)






def transform_golden(istring, ostring):
	ifile = open(istring, 'r')
	ofile = open(ostring, 'w')

	for line in ifile:
		elem = line.split('\t')
		tokens = elem[0].split(' ')
		tags = elem[1].split(' ')
		for token, tag in zip(tokens, tags):
			ofile.write(token+'\t'+tag+'\n')
			


if __name__=='__main__':
	try:
		transform_golden('golden.txt', 'golden_tran.txt')
		print compare('output.txt', 'golden_tran.txt')
	except:
		print 'unknow error'
