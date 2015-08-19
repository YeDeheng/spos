import re

text = 'http://asfas.com/asdfa/ '
text = re.sub(r'(?<=\w)/(?=\s+)', ' ', text)
print text