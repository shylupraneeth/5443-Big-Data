import redis
import string
import json
import sys

def is_json(myjson):
   try:
      json_object = json.loads(myjson)
   except ValueError, e:
      return False
   return True

   
#Link up with redis 
r = redis.Redis(host='localhost', port=6379, db=0)
 
f=open('/var/www/html/5443-Big-Data/Redis/nutrition.json','r')
g = open("nutrition_clean.json", "w")
h = open("writeup.md", "w")
    # str() converts to string

# Read one line from file
i = 0
j = 0
k = 0.0

for line in f:
    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
	j = j+1
	if is_json(line):
			i = i + 1
			line = json.loads(filter(lambda x: x in string.printable, line))
			g.write( str(line) )  
		
k = float(((j-i)/i)*100)		
h.write('### Json File Processing')
h.write('\n### Written By Shylendra P Vanga')
h.write('\n Total Good Lines Processed: '+str(i))	
h.write('\n Total Bad lines Removed: '+str(j-i))
h.write('\n Ratio of Good vs Bad : ' +str(k))
h.write('')		
g.close()
h.close()
