# access data from url

import urllib.request as rq
import re
f= rq.urlopen("https://in.linkedin.com/in/email-list-database-mobile-number-database-97a7375b")
data= f.read()
print(data)
print(type(data))

data= str(data)
print(data)
print(type(data))