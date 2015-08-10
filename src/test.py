s = 'hello world'

ifile = open('1.txt', 'w')
ifile.write(s + '\n')
#ifile.close()

#ofile = open('2.txt', 'r')
for line in ifile:
	print line