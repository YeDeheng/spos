tag_list = ['O', 'N', '^', 'V', 'A', 
			'R', '!', 'D', 'P', 'T', 
			'X', 'Y', '&', '$', ',', 
			'G', 'Z', 'S', 'L', 'M', 
			'=', 'C', '@', 'U', 'E']


def count(istring1):
	counter_list = [0, 0, 0, 0, 0,
				0, 0, 0, 0, 0,
				0, 0, 0, 0, 0,
				0, 0, 0, 0, 0,
				0, 0, 0, 0, 0]
	gold = open(istring1, 'r')
	
	tags_gold = []

	for line in gold:
		if line != '\n':
			line = line.rstrip()
			tag = line.split('\t')[1]
			tags_gold.append(tag)

	total = 0
	for i in tags_gold:
		total += 1
		if i in tag_list:
			index = tag_list.index(i)
			counter_list[index] += 1

	print total 
	return counter_list

print tag_list
print count('train_sep24.conll')
print count('devel_sep24.conll')
print count('test_sep24.conll')
print count('golden_tran.txt')