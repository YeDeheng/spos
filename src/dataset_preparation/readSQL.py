# -*- coding: utf-8 -*-

import MySQLdb
import re
from HTMLParser import HTMLParser

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

def read_knowledge_unit(question_id):
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

	f = open('out.txt', 'w')
	for row in all: 
		f.write(strip_tags(row[0])+'\n')
	return all


for row in read_knowledge_unit(1447407):
	print row[0]
