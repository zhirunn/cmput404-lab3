#!/usr/bin/env python

import os
import sys
import cgi

import cgitb
cgitb.enable()

method = os.environ['REQUEST_METHOD']

print "Content-Type: text/html"

print
print "You did a", method, "request!"
print "<pre>"

#raise ValueError

#length = int(os.environ['CONTENT_LENGTH'])
#params = sys.stdin.read(length)
#print params

form = cgi.FieldStorage()
print form.getfirst('username')