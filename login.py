#!/usr/bin/env python

import os
import sys
import cgi

import cgitb
cgitb.enable()
import secret


method = os.environ['REQUEST_METHOD']

form = cgi.FieldStorage()

print "Content-Type: text/html"

if method == 'POST':
    username = form.getfirst('username') 
    password = form.getfirst('password') 
    
    if username == secret.username and password == secret.password:
        print "Set-Cookie: auth=mysecretvalue"
        print
        print "<h1> Welcome Back", secret.username
        print "</h1>"
    else:
        print
        print "<h1> Error! Invalid username or password!"
        print "</h1>"
    
else:
    raw_cookie = os.getenv('HTTP_COOKIE', '') or '='
    key, cookie = raw_cookie.split('=')
    
    if cookie == 'mysecretvalue':
        print
        print "<h1> Welcome Back", secret.username
        print "</h1>"        
    
#print "You did a", method, "request!"

print
print '<form method="POST">'
print 'Username: <input name="username">'
print '<br>'
print 'Password: <input type="password"'
print 'name="password">'
print '<br>'
print '<button type="submit">Login</button>'
print '</form>'