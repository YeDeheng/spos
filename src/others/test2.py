from HTMLParser import HTMLParser
from htmlentitydefs import entitydefs

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)

    def handle_starttag(self, tag, attrs):
        self.fed.append(' ')

    def handle_endtag(self, tag):
        self.fed.append(' ')

    def handle_entityref(self, name):
        if entitydefs.get(name) is None:
            # unknown entity refs are emitted as is
            self.fed.append('&{}'.format(name))
        else:
           # known entity refs are replaced with space
           self.fed.append(' ')

    def get_data(self):
        self.close()    # N.B. ensure all buffered data has been processed
        return ''.join(self.fed)
        
def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


html = '&abc= is my input text'
print strip_tags('html tags<p>will be&amp;replaced</p>with space. NOT this &abc')