# -*- coding: utf-8 -*-

import sys,os
import MySQLdb
import re
from HTMLParser import HTMLParser
from htmlentitydefs import entitydefs

import codecs
codecs.register_error('replace_against_space', lambda e: (u' ',e.start + 1))
#print unicode('ABC\x97ab\x99c上午', 'utf-8', errors='replace_against_space')

def my_encoder(my_string):
   for i in my_string:
      try :
         yield unicode(i, 'utf-8')
      except UnicodeDecodeError:
         yield ' ' #or another whietespaces 

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
            entity = m.group()
            # semicolon is consumed, other chars are not.
            if entity is not None:
            	print "entity is none"
            	if entity[-1] != ';':
                	entity = entity[:-1]
            	self.fed.append(entity)
            else: 
            	self.fed.append('')
        else:
            self.fed.append(' ')

    def get_data(self):
        self.close()
        return ''.join(self.fed) # I would rather want more spaces.  

    # def handle_data(self, d):
    #     self.fed.append(d)
    # def get_data(self):
    #     #return self.fed
    #     return ' '.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    html = re.sub(r'<pre>.*?</pre>', ' ', html)
    html = re.sub(r'(`(?=\S)|(?<=\S)`)', '', html)
    s.feed(html)
    return s.get_data()



def read_post(post_id):
	db = MySQLdb.connect(host="localhost", 
	                     user="root", 
	                     passwd="ydh0114", 
	                     db="stackoverflow201503")
	cur = db.cursor() 
	cur.execute("SELECT Title FROM posts where Id=%s" % (post_id))
	title = cur.fetchall()

	cur.execute("SELECT Body FROM posts where Id=%s" %(post_id))
	body = cur.fetchall()
	cur.execute("SELECT Text FROM comments where PostId=%s" % (post_id))
	comments = cur.fetchall()

	if title[0][0] is None:
		all = body + comments
	else: 
		all = title + body + comments 

	f = open('out.txt', 'w')
	for row in all: 
		f.write(strip_tags(row[0])+'\n')
	f.close()

	return all

def read_knowledge_unit(istring, ostring):
	question_id = istring
	db = MySQLdb.connect(host="localhost", 
	                     user="root", 
	                     passwd="ydh0114", 
	                     db="stackoverflow201503")
	cur = db.cursor() 
	cur.execute("SELECT Title FROM posts where Id=%s" % (question_id))
	title = cur.fetchall()

	cur.execute("SELECT Body FROM posts where Id=%s" %(question_id))
	body = cur.fetchall()
	cur.execute("SELECT Text FROM comments where PostId=%s" % (question_id))
	comments = cur.fetchall()

	if title[0][0] is None:
		all = body + comments
	else: 
		all = title + body + comments 

	cur.execute("SELECT Id FROM posts where ParentId=%s" %(question_id))
	answers = cur.fetchall()
	for row in answers:
		answer_id = row[0]
		cur.execute("SELECT Body FROM posts where Id=%s" %(answer_id))
		ans_body = cur.fetchall()
		all += ans_body
		
		cur.execute("SELECT Text FROM comments where PostId=%s" %(answer_id))
		ans_comments = cur.fetchall()
		all += ans_comments
	#print all
	f = open(ostring, 'w')
	for row in all: 
		print row[0]
		print strip_tags(row[0])
		#uni = unicode(strip_tags(row[0]), 'utf-8', errors='replace_against_space') # excellent answer from Stack Overflow
		uni = ''.join( my_encoder(strip_tags(row[0])) ) # excellent answer from Stack Overflow
		#print unicode(strip_tags(row[0]).decode('utf-8', 'ignore').encode('utf-8'), 'utf-8')
		#f.write(uni.encode('utf-8') + '\n') 
		f.write(uni + '\n')
	return all


if __name__ ==  '__main__':
	try:
		read_knowledge_unit(*sys.argv[1:])
	except TypeError:
		print "Usage : python readSQL.py <question_id> <output file>"


#for row in read_knowledge_unit(1447407):
#	print row[0]
