import redis
import sys
import json
import string

def is_json(myjson):
	try:
		json_object=json.loads(myjson)
	except ValueError,e:
		return False
	return True
			
f=open('nutrition.json','r')
r=redis.StrictRedis(host='localhost',port=6379,db=0)
r.flushdb()
for line in f:
	if is_json(line):
		line = json.loads(filter(lambda x: x in string.printable, line))
		r.sadd("MyList1",line['_id'])
print r.scard("MyList1")