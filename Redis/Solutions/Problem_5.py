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
			
f=open('/var/www/html/5443-Big-Data/Redis/nutrition.json','r')
r=redis.StrictRedis(host='localhost',port=6379,db=0)
r.flushdb()

for line in f:
	
	if is_json(line):
		line = json.loads(filter(lambda x: x in string.printable, line))
		for Nutrients  in line['nutrients']:
			r.sadd("LISTofID",Nutrients['_id'])
			r.hset("HashofNutrients",Nutrients['_id'],Nutrients)
			r.sadd("SetofTagName",Nutrients['tagname'])
			r.hset("HashofTagName",Nutrients['tagname'],Nutrients)
		
print r.scard("LISTofID")

print r.hlen("HashofNutrients")

print r.scard("SetofTagName")

print r.hlen("HashofTagName")
