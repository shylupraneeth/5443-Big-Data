import redis
import string
import json
import sys

#Link up with redis 
r = redis.Redis(host='localhost', port=6379, db=0)
r.flushdb()
f = open('nutrition.json','r')
# Read one line from file

for line in f:
    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
    line = json.loads(filter(lambda x: x in string.printable, line))
    #Print the line nicely formatted
    #print json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))

    for nut in line['nutrients']:
        r.zincrby('taghash',nut['tagname'],1)
LenZList=r.zcard('taghash')
listVals=r.zrange('taghash',LenZList-5,LenZList)
for test in listVals:
	print test
	print r.zscore('taghash',test)