
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