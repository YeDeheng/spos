def transform_golden(istring, ostring):
	ifile = open(istring, 'r')
	ofile = open(ostring, 'w')

	for line in ifile:
		elem = line.split('\t')
		tokens = elem[0].split(' ')
		tags = elem[1].split(' ')
		for token, tag in zip(tokens, tags):
			ofile.write(token+'\t'+tag+'\n')


# f = open('ziqungaosa.txt', 'r')
# f1 = open('train_sep15.txt', 'w')
# f2 = open('eval_sep15.txt', 'w')
# for index, line in enumerate(f):
# 	i = index%2
# 	if i == 0:
# 		f1.write(line)
# 	if i == 1:
# 		f2.write(line)
# f1.close()
# f2.close()
# f.close()
transform_golden('golden-liuyi.txt', 'train_sep15_part2.conll')
transform_golden('golden-xuejiao.txt', 'eval_sep15_part2.conll')
