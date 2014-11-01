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
			
f=open('/var/www/html/5443-Big-Data/Redis/nutrition_clean.json','r')
r=redis.StrictRedis(host='localhost',port=6379,db=0)
r.flushdb()

for line in f:
	
	if is_json(line):
		line = json.loads(filter(lambda x: x in string.printable, line))
		for Nutrients  in line['nutrients']:
			r.sadd("MyList13",Nutrients['_id'])
			r.hset("MyHash9",Nutrients['_id'],Nutrients)
			r.sadd("TagNameSet",Nutrients['tagname'])
			r.hset("TagNameHash",Nutrients['tagname'],Nutrients)
		
print r.scard("MyList13")

print r.hlen("MyHash9")

print r.scard("TagNameSet")

print r.hlen("TagNameHash")
