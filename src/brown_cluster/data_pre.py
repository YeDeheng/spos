# -*- coding: utf-8 -*-
import sys,os

lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
from mytokenizer import mytokenizer

import MySQLdb
import re
from HTMLParser import HTMLParser
from htmlentitydefs import entitydefs

import codecs
codecs.register_error('replace_against_space', lambda e: (u' ',e.start + 1))
#print unicode('ABC\x97ab\x99c上午', 'utf-8', errors='replace_against_space')



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
            if entity[-1] != ';':
                entity = entity[:-1]
            self.fed.append(entity)
        else:
            self.fed.append(' ')

    def get_data(self):
        self.close()
        return ' '.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    html = re.sub(r'<pre>.*?</pre>', ' ', html)
    s.feed(html)
    return s.get_data()


def dump(ostring):
	
	db = MySQLdb.connect(host="localhost", 
	                     user="root", 
	                     passwd="ydh0114", 
	                     db="stackoverflow201503")
	cur = db.cursor()

	cur.execute("SELECT Id FROM posts where Tags like '%<java>%' and Tags like '%<javascript>%' limit 2")
	IDs = cur.fetchall()
	
	f = open(ostring, 'w')
	for i, row in enumerate(IDs):
		if i >= 0:  # 201 is hachy here. We use the first 200 for annotation. 
			question_id = row[0]

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

			for row in all: 
				uni = unicode(strip_tags(row[0]), 'utf-8', errors='replace_against_space')
				f.write(uni + '\n')
	f.close()

if __name__=='__main__':
	dump('raw.txt') # dump to input_brown.txt
	mytokenizer.tokenize('raw.txt', 'tokenized.txt')