#!/usr/bin/env python3
import cgi, cgitb
import os, json
from templates import login_page, secret_page, after_login_incorrect, _wrapper
from secret import username, password
from http.cookies import SimpleCookie

# Python 3.7 versus Python 3.8
try:
    from cgi import escape #v3.7
except:
    from html import escape #v3.8

cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get Data fom Cookie
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = cookie.get("Username").value if cookie.get("Username") else None
cookie_password = cookie.get("Pwd").value if cookie.get("Pwd") else None


if(cookie_username == username and cookie_password == password):
    print(secret_page(username, password))

    for param in os.environ.keys():
        if param == "HTTP_COOKIE":
            print("<b>%20s<b>: %s<br>" % (param, os.environ[param]))

else:
     # Get data from fields
    usernameEntered = form.getvalue('username')
    passwordEntered = form.getvalue('password')

    if(not(usernameEntered == username and passwordEntered == password)):
        print(login_page())

    if(usernameEntered != None):
        print("<p><b>Username</b> %s <b>password</b> %s</p>" % (usernameEntered, passwordEntered))

    # Login Success
    if(usernameEntered == username and password == passwordEntered):
        # Set the cookie
        print(f"Set-Cookie:Username = {username}")
        print(f"Set-Cookie:Pwd = {password}")


        print(secret_page(username, password))

    # Login fail
    elif ((usernameEntered != None)):
        print(after_login_incorrect())



