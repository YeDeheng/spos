import re

def replace_tagset(text, dic):
    for i, j in dic.iteritems():
        text = re.sub(i, j, text)
    return text
 
# our text the replacement will take place
my_text = '_abd_abd everybody.'
 
# dictionary with key:values.
# key is PTB tagset used by Stanford Tagger
# value is our own tagset 
REPS = {'_NN ' : '_N ',
		'_NNS ' : '_N ',

		'_PRP ' : '_O ', 
		'_WP ' : '_O ',

		'_NNP ' : '_^ ',
		'_NNPS ' : '_^ ', 

		'_VB[A-Z]? ' : '_V ',
		'_MD ' : '_V ', 

		'_JJ[A-Z]? ' : '_A ',

		'_R[BP][A-Z]? ' : '_R ',
		'_WRB ' : '_R ', 

		'_UH ' : '_! ',

		'_WDT ' : '_D ',
		'_DT ' : '_D ', 
		'_WP\$ ' : '_D ', 
		'_PRP\$ ' : '_D ', 

		'_IN ' : '_P ', 
		'_TO ' : '_P ', 

		'_CC ' : '_& ', 

		'_PDT ' : '_X ', 
		'_EX ' : '_X ', 

		'_CD ' : '_$ ', 

		'_. ' : '_, ', 
		'_: ' : '_, ',
 
		'_FW ' : '_G ', 
		'_POS ' : '_G ', 
		'_SYM ' : '_G ', 
		'_LS ' : '_G '
		}
 
infile = open('pretag.txt', 'r')
outfile = open('maptag.txt', 'w')
for line in infile: 
	outfile.write(replace_tagset(line, REPS))
infile.close()
outfile.close()

infile = open('lingfeng-out.txt', 'r')
outfile = open('lingfeng-map.txt', 'w')
for line in infile: 
	outfile.write(replace_tagset(line, REPS))
infile.close()
outfile.close()