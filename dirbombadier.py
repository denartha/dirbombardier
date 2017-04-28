#!/usr/bin/env python

import requests
import sys
import argparse


ap = argparse.ArgumentParser()
group = ap.add_mutually_exclusive_group(required=True)
group.add_argument('-u', nargs=2) # specify url to brute

opts = ap.parse_args()


url = opts.u[0]
word_list = opts.u[1]
#word_list = 'small.txt'

directories  = open(word_list, 'r')
dirs = directories.readlines()
directories.close()

for dir in dirs:
	uri = url + "/" + dir
	#print uri
	try:
		r = requests.get(uri)
		d = r.status_code
		code = '200'
		if d == int(code):
			print "URL: " + uri.strip()
		else:
			print "Not found: " + uri.strip()

	except requests.ConnectionError, e:
    		print e 

