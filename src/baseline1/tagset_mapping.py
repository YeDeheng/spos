import re
import sys, os

def replace_tagset(text, dic):
    for i, j in dic.iteritems():
        text = re.sub(i, j, text)
    return text
 
# our text the replacement will take place
my_text = '_abd_abd everybody.'
 
# dictionary with key:values.
# key is PTB tagset used by Stanford Tagger
# value is our own tagset 
REPS = {'_NN(?=[ \n])' : '_N',
		'_NNS(?=[ \n])' : '_N',

		'_PRP(?=[ \n])' : '_O', 
		'_WP(?=[ \n])' : '_O',

		'_NNP(?=[ \n])' : '_^',
		'_NNPS(?=[ \n])' : '_^', 

		'_VB[A-Z]?(?=[ \n])' : '_V',
		'_MD(?=[ \n])' : '_V', 

		'_JJ[A-Z]?(?=[ \n])' : '_A',

		'_R[BP][A-Z]?(?=[ \n])' : '_R',
		'_WRB(?=[ \n])' : '_R', 

		'_UH(?=[ \n])' : '_!',

		'_WDT(?=[ \n])' : '_D',
		'_DT(?=[ \n])' : '_D', 
		'_WP\$(?=[ \n])' : '_D', 
		'_PRP\$(?=[ \n])' : '_D', 

		'_IN(?=[ \n])' : '_P', 
		'_TO(?=[ \n])' : '_P', 

		'_RP(?=[ \n])' : '_T',
		
		'_PDT(?=[ \n])' : '_X', 
		'_EX(?=[ \n])' : '_X', 

		'_CC(?=[ \n])' : '_&', 

		'_CD(?=[ \n])' : '_$', 

		# '_.(?=[ \n])' : '_, ', 
		# '_:(?=[ \n])' : '_, ',
 
		'_FW(?=[ \n])' : '_G', 
		'_POS(?=[ \n])' : '_G', 
		'_SYM(?=[ \n])' : '_G', 
		'_LS(?=[ \n])' : '_G'
		}
if __name__=='__main__': 
	infile = open(sys.argv[1], 'r')
	outfile = open(sys.argv[2], 'w')
	for line in infile: 
		outfile.write(replace_tagset(line, REPS))
	infile.close()
	outfile.close()
