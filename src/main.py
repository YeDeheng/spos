import readMySQL, removeHTML

# read the body of the post
body_array = readMySQL.read()

# remove HTML tags
for row in body_array :
	input_POSTagger = removeHTML.strip_tags(row[0])

print input_POSTagger