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
#opening for reading a file			
f=open('/var/www/html/5443-Big-Data/Redis/nutrition.json','r')

r=redis.StrictRedis(host='localhost',port=6379,db=0)
#iterating a file
for line in f:
	if is_json(line):
		line = json.loads(filter(lambda x: x in string.printable, line))
		nutrients = line['nutrients']
		for nutrient in nutrients:
			
			r.zincrby('',nutrient['tagname'],1)
print r.zrange("nutrient", 1, 5)