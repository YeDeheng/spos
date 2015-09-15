mapped_tag_list = ['G']#['O', 'N', '^', 'V', 'A', 'R', '!', 'D', 'P', 'T', 'X', '&', '$', 'G']
def compare(istring1, istring2):
	test = open(istring1, 'r')
	gold = open(istring2, 'r')
	
	tags_test = []
	tags_gold = []
	for line in test:
		if line != '\n':
			line = line.rstrip()
			tag = line.split('\t')[1]
			tags_test.append(tag)
	for line in gold:
		if line != '\n':
			line = line.rstrip()
			tag = line.split('\t')[1]
			tags_gold.append(tag)

	if len(tags_test) == len(tags_gold):
		equals = 0
		total = 0
		proper_noun_count = 0
		for i, j in zip(tags_test, tags_gold):
			if j == '^':
				proper_noun_count += 1
			if j in mapped_tag_list:
				total += 1
				if i == j:
					equals += 1
	print "#proper_noun_count is: ", proper_noun_count
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
	transform_golden('sample-golden.txt', 'golden_tran.txt')
	try:
		print compare('sample-output.txt', 'golden_tran.txt')	
	except Exception, e :
		print e	
		raise
	# #transform_golden('zhenchang5.automatic_tags', 'golden_tran.txt')
	# print compare('zhenchang5.automatic_tags.ST.mapped', 'golden_tran.txt')
