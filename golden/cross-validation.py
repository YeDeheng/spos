f = open('golden-all.txt', 'r')
f1 = open('golden-1.txt', 'w')
f2 = open('golden-2.txt', 'w')
f3 = open('golden-3.txt', 'w')
f4 = open('golden-4.txt', 'w')

for index, line in enumerate(f):
	i = index%4
	print i
	if i == 0:
		f1.write(line)
	if i == 1:
		f2.write(line)
	if i == 2:
		f3.write(line)
	if i == 3:
		f4.write(line)
f.close()
f1.close()
f2.close()
f3.close()
f4.close()
