import urllib2
import json

data = urllib2.urlopen('http://api.stackoverflow.com/1.1/tags')
data.read()
j = json.load(data)
k = [i for i, j, k in j[1]]
l = json.dumps(k)

