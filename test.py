#! /usr/bin/python
import requests
import json


json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

pj = json.loads(json_string)

print(pj['first_name'])

print "hello world"

response = requests.get('https://api.github.com/user/repos', auth=('johnnywalsh201', 'Snooki15!'))

data= response.json()
#data = json.loads(response.text)

print data

r = requests.get('https://github.com/timeline.json')
c = r.content
j = json.loads(c)

for item in j:
    print item['repository']['name']
