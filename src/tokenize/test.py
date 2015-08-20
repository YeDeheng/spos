# -*- coding: utf-8 -*-
s = '\x97'
print unicode(s, errors='replace')


s = '上午'
print unicode(s, 'utf-8')
# s = unicode('上午')
# uni = unicode(s)
# f = open('output.txt', 'w')
# f.write(uni.encode('utf-8')+'\n') 

# uni = unicode(s)
# print uni
InputString='ABC\x97abc上午' 
print InputString
print InputString.decode('utf-8', 'replace').replace(InputString.decode('utf-8', 'replace')[3],' ')

import codecs
codecs.register_error('replace_against_space', lambda e: (u' ',e.start + 1))
print unicode('ABC\x97ab\x99c上午', 'utf-8', errors='replace_against_space')

