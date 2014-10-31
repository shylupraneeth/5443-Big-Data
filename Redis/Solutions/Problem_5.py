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
def DispMemInfo():
	print "**************************************************************"
	InfoData=str(r.info())
	InfoData=InfoData.replace('\'','"')
	if is_json(str(InfoData)):
		InfoDataVal=json.loads(filter(lambda x: x in string.printable, InfoData))
		print "Used memeory is: "
		print InfoDataVal['used_memory']
	print "**************************************************************"
for line in f:
	if is_json(line):
		line = json.loads(filter(lambda x: x in string.printable, line))
		count=0;
		StrVal=""
		for Nutrients  in line['nutrients']:
			r.sadd("MyList13",Nutrients['_id'])
			r.hset("MyHash9",Nutrients['_id'],Nutrients)
			r.sadd("TagNameSet",Nutrients['tagname'])
			r.hset("TagNameHash",Nutrients['tagname'],Nutrients)
			r.hset("SubColl",Nutrients['_id'],Nutrients)
			StrVal=(StrVal)+(Nutrients['_id'])+","
			count=count+1
		StrVal=StrVal[:-1]
		print StrVal
		r.hset("MainColl",line['_id'],StrVal)
# Storing the key of all the keys in the main hash
# Storing the nutrients and keys in Sub hash
intVal="01001"
strVal=r.hget("MainColl",intVal)
#print "*******************************************"
#print strVal
#print "*******************************************"
ArrstrVal=strVal.split(',')
# Accessing each element from the list
for EachVal in ArrstrVal:
	print EachVal
print r.scard("MyList13")
print r.hlen("MyHash9")
print r.scard("TagNameSet")
print r.hlen("TagNameHash")
DispMemInfo()