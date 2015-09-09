# -*- coding: utf-8 -*-
import sys,os

lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
from mytokenizer import mytokenizer

import MySQLdb
import re
from HTMLParser import HTMLParser
from htmlentitydefs import entitydefs
from bs4 import BeautifulSoup
import codecs

def my_encoder(my_string):
   for i in my_string:
      try :
         yield unicode(i)
      except UnicodeDecodeError:
         yield ' ' #or another whietespaces 

#codecs.register_error('replace_against_space', lambda e: (u' ',e.start + 1))
#print unicode('ABC\x97ab\x99c上午', 'utf-8', errors='replace_against_space')

def strip_backtick(istring):
    return re.sub(r'(`(?=\S)|(?<=\S)`)', '', istring)  # this is hacky. Deheng

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
        self.entityref = re.compile('&[a-zA-Z][-.a-zA-Z0-9]*[^a-zA-Z0-9]')

    def handle_data(self, d):
        self.fed.append(d)

    def handle_starttag(self, tag, attrs):
        self.fed.append(' ')

    def handle_endtag(self, tag):
        self.fed.append(' ')

    def handle_entityref(self, name):
        if entitydefs.get(name) is None:
            m = self.entityref.match(self.rawdata.splitlines()[self.lineno-1][self.offset:])
            
            # semicolon is consumed, other chars are not.
            if m is not None:
            	entity = m.group()
            	if entity[-1] != ';':
                	entity = entity[:-1]
            	self.fed.append(entity)
            else: 
            	print "entity is none"
            	self.fed.append('')
        else:
            self.fed.append(' ')

    def get_data(self):
        self.close()    # N.B. ensure all buffered data has been processed
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    html = re.sub(r'<pre>.*?</pre>', ' ', html)
    html = strip_backtick(html)
    s.feed(html)
    return s.get_data()


def dump(ostring):
	
	db = MySQLdb.connect(host="localhost", 
	                     user="root", 
	                     passwd="ydh0114", 
	                     db="stackoverflow201503")
	cur = db.cursor()

	#cur.execute("SELECT Id FROM posts where Tags like '%<java>%' or Tags like '%<javascript>%' ")
	cur.execute("SELECT Id FROM posts where (Tags like '%<java>%' or Tags like '%<javascript>%') and PostTypeId=1 ") #" and Id>=6155464 limit 10 ")
	IDs = cur.fetchall()
	
	f = open(ostring, 'w')
	for i, row in enumerate(IDs):
		if i >= 0:  # 201 is hachy here. We use the first 200 for annotation. 
			question_id = row[0]

			cur.execute("SELECT Title FROM posts where Id=%s" % (question_id))
			title = cur.fetchall()

			cur.execute("SELECT Body FROM posts where Id=%s" %(question_id))
			q_body = cur.fetchall()

			cur.execute("SELECT Text FROM comments where PostId=%s" % (question_id))
			q_comments = cur.fetchall()

			# if title[0][0] is None:
			# 	all = body + comments
			# else: 
			# 	all = title + body + comments
			body = q_body 
			comments = q_comments
			
			cur.execute("SELECT Id FROM posts where ParentId=%s" %(question_id))
			answers = cur.fetchall()
			for row in answers:
				answer_id = row[0]
				cur.execute("SELECT Body FROM posts where Id=%s" %(answer_id))
				ans_body = cur.fetchall()
				body += ans_body
				
				cur.execute("SELECT Text FROM comments where PostId=%s" %(answer_id))
				ans_comments = cur.fetchall()

				comments += ans_comments

			uni =  ''.join( my_encoder( title[0][0] ) )
			f.write(uni + '\n')
			for row in body: 
				#uni = unicode(strip_tags(row[0]), 'utf-8', errors='replace_against_space')
				uni =  ''.join( my_encoder(  strip_tags(''.join(my_encoder(row[0]) ) ) ) )
				f.write(uni + '\n')
			for row in comments:
				uni =  ''.join( my_encoder( strip_backtick(row[0]) ) )
				f.write(uni + '\n')
	f.close()

if __name__=='__main__':
	# html = '''asdfasdf'''
	# print strip_tags(''.join(my_encoder(html)))
	dump('raw.txt') # dump to input_brown.txt
	mytokenizer.tokenize('raw.txt', 'tokenized.txt')