# from HTMLParser import HTMLParser
# from bs4 import BeautifulSoup
# class MLStripper(HTMLParser):
#     def __init__(self):
#         self.reset()
#         self.fed = []
#     def handle_data(self, d):
#             self.fed.append(d)
#     def get_data(self):
#         return ' '.join(self.fed)
        
# def strip_tags(html):
#     s = MLStripper()
#     s.feed(html)
#     return s.get_data()


# html = '&abc= is my input text'
# soup = BeautifulSoup(html)
# print soup.text
# print strip_tags('&abc= is my input text')

from bs4 import BeautifulSoup

html = '&abc= is my input text<h2>asdf</h2>'
soup = BeautifulSoup(html, 'html.parser')
all_text = ' '.join(soup.findAll(text=True))
print all_text