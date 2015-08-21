# -*- coding: utf-8 -*-

import sys,os
import MySQLdb
import re
from HTMLParser import HTMLParser

import codecs
codecs.register_error('replace_against_space', lambda e: (u' ',e.start + 1))
#print unicode('ABC\x97ab\x99c上午', 'utf-8', errors='replace_against_space')

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        #return self.fed
        return ' '.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    html = re.sub(r'<pre><code>.*?</code></pre>', '', html)
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
		#print strip_tags(row[0])
		uni = unicode(strip_tags(row[0]), 'utf-8', errors='replace_against_space') # excellent answer from Stack Overflow
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