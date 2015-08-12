# You have to install MySQLdb first
import MySQLdb
from HTMLParser import HTMLParser

def read(question_id):
	db = MySQLdb.connect(host="localhost", # your host, usually localhost
	                     user="root", # your username
	                     passwd="ydh0114", # your password
	                     db="stackoverflow201503") # name of the data base

	# you must create a Cursor object. It will let
	#  you execute all the queries you need
	cur = db.cursor() 

	# Use all the SQL you like
	cur.execute("SELECT Body FROM posts where Id=%s or ParentId=%s" %(question_id, question_id))
	#print cur.fetchall()
	return cur.fetchall()
	# print all the first cell of all the rows
	#for row in cur.fetchall() :
	#    print row[0]

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
    s.feed(html)
    return s.get_data()



f = open("lingfeng.txt", "w")
# remove HTML tags
for row in read(15406977) :
	input_POSTagger = strip_tags(row[0])
	print input_POSTagger
	f.write(input_POSTagger)
f.close()