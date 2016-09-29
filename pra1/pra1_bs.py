#learn about how to use urllib and beautifulSoup
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#element in bs
# html
# head
# title
# body
# p
# b
# p
# a
# a
# a
# p
import ssl
import urllib.request
import bs4
url = "https://www.cs.ucd.ie"
#When calling the SSLContext constructor directly,CERT_NONE is the default.
#Since it does not authenticate the other peer, it can be insecure,
#especially in client mode where most of time you would like to
#ensure the authenticity of the server you’re talking to.
#Therefore, when in client mode, it is highly recommended to use CERT_REQUIRED.


#This PEP proposes to enable verification of X509 certificate signatures,
#as well as hostname verification for Python's HTTP clients by default,
#subject to opt-out on a per-call basis.
#This change would be applied to Python 2.7, Python 3.4, and Python 3.5.
ssl._create_default_https_context = ssl._create_unverified_context
raw = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(raw,"lxml")
#print(soup.title) #this can print <title></title>
print(soup.title.get_text(strip=True))
print(soup.body.get_text(strip=True))
#a ,, find the links
#soup.findAll('a')
#foo = soup.findAll('a')
#for item in foo: print(item)

#soup.get_text()  # extracting all the text from a page


