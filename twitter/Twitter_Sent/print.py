import urllib
import json
import dictBuilder

response = urllib.urlopen("http://search.twitter.com/search.json?q=Boston")
print type(response)
p = json.load(response)
print type(p)
print p
#print p.keys()
#print "\n" * 2
#r = p["results"]

score = dictBuilder.dictBuilder()

#print r[0].keys()
#print r[0]['text']   
