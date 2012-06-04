import urllib2
from urllib import urlencode
import re
import cookielib

try:
    from loginInfo import *
    #Create loginInfo.py with USERNAME and PASSWORD variables in it to use that.
except:
    USERNAME = raw_input("Username>")
    PASSWORD = raw_input("Password>")


def save(filename, data):
    print "saving."
    with open(filename,"w") as f:
        f.write(data)


USER_AGENT = ("Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.5 (KHTML, "
                  "like Gecko) Chrome/19.0.1084.52 Safari/536.5")
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [
    ("User-Agent", USER_AGENT),
    ("Referer","http://www.okcuipd.com/")
]    


resp = opener.open("http://www.okcupid.com/")
save("homepage.html",resp.read())


data = urlencode({
    "username": USERNAME
   ,"password": PASSWORD
   ,"dest":"/?"
   })
url = "http://www.okcupid.com/login"
resp = opener.open(url)
save("loggedin.html",resp.read())

