#!/usr/bin/python

import sys
import Adafruit_DHT
import time


def read():

	humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 2)

	temp_f = (temp_c * 1.8) + 32

	return [int(round(time.time())), humidity, temp_f]


read()

timestamp, humidity, temp = read()

print 'Time: {2:d}: Temp: {0:0.1f}F, Humidity: {1:0.1f}%'.format(temp, humidity, timestamp)
