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
                self.fed.append('')
        else:
            print "entity is none"
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



html = '''It was already in my comment on Balus C's reply but here is the import line: Line 53 is my javascript import: `<script src="http://view.light-speed.com/mumble.php?url=https%3A//api.mumble.com/mumble/‌​cvp.php%3Ftoken%3DLSG-6D-ECBDEB&c=000000&r=0&h=450&w=160&css=https%3A//view.light‌​-speed.com/styles/mumble-minimal.css"`'''
print strip_tags(html)