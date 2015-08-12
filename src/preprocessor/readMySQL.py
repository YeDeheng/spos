# You have to install MySQLdb first
import MySQLdb

def read(question_id):
	db = MySQLdb.connect(host="localhost", # your host, usually localhost
	                     user="root", # your username
	                     passwd="ydh0114", # your password
	                     db="stackoverflow201503") # name of the data base

	# you must create a Cursor object. It will let
	#  you execute all the queries you need
	cur = db.cursor() 

	# Use all the SQL you like
	cur.execute("SELECT Body FROM posts where Id=18553292")
	return cur.fetchall()
	# print all the first cell of all the rows
	#for row in cur.fetchall() :
	#    print row[0]