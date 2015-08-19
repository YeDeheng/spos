# -*- coding: utf-8 -*-
import re
mycompile = lambda pat:  re.compile(pat,  re.UNICODE)


NotEdgePunct = r"""[a-zA-Z0-9]"""
EdgePunct      = r"""[  ' " “ ” ‘ ’ * « » { } ( \) [ \]  ]""".replace(' ','')

EdgePunctLeft  = r"""(\s|^)(%s+)(%s)""" % (EdgePunct, NotEdgePunct)
print EdgePunctLeft
api_suffix = r"""(?:\(\))"""
EdgePunctRight =   r"""(%s(?:\(\))?)(%s+)(\s|$)""" % (NotEdgePunct, EdgePunct)
print EdgePunctRight
EdgePunctLeft_RE = mycompile(EdgePunctLeft)
EdgePunctRight_RE= mycompile(EdgePunctRight)


def edge_punct_munge(s):
  s = EdgePunctLeft_RE.sub( r"\1\2 \3", s)
  s = EdgePunctRight_RE.sub(r"\1 \2\3", s)
  return s


s = 'printf()" I love china (but china do not love me hah) .'
print edge_punct_munge(s)
#print re.sub(r'(tf)', ' ', s)


s = r'[\'"]'
print s