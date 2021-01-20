#!/usr/bin/python

import json
import urllib2
from read import read


timestamp, humidity, temp = read()

data = {
	'temperature': round(temp, 3),
	'humidity': round(humidity, 3),
	'timestamp': timestamp
}

req = urllib2.Request('http://192.168.1.15:8080/log')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))
