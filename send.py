#!/usr/bin/python

import json
import urllib2
from read import read


humidity, temp = read()

data = {
        'temperature': round(temp, 3),
	'humidity': round(humidity, 3)
}

req = urllib2.Request('http://hicks.steingard.lan:8080/log')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))
