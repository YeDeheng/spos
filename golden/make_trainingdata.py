f1 = open('golden-3.txt', 'r')
f2 = open('train-3.txt', 'w')
for line in f1:
  elem = line.split('\t')
  tokens = elem[0].split(' ')
  tags = elem[1].split(' ')
  for token, tag in zip(tokens,tags):
    f2.write(token + '\t' + tag + '\n')
