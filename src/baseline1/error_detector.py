
def detect(istring1, istring2):
	f1 = open(istring1, 'r')
	f2 = open(istring2, 'r')
	for la, lb in zip(f1, f2):
		print la


if __name__=='__main__':
	detect('sample-output.txt', 'golden_tran.txt')	
	# #transform_golden('zhenchang5.automatic_tags', 'golden_tran.txt')
	# print compare('zhenchang5.automatic_tags.ST.mapped', 'golden_tran.txt')
