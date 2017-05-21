#!/usr/bin/env python

import requests
import sys
import argparse


ap = argparse.ArgumentParser(description='dirbombardier brute force directories on a webserver or application. Simply supply a URL and a wordlist', usage='dirbombardier http://site.org/ wordlist.txt'   )
group = ap.add_mutually_exclusive_group(required=True)
group.add_argument('-u', nargs=2) # specify url to brute

opts = ap.parse_args()


url = opts.u[0]
word_list = opts.u[1]
#word_list = 'small.txt'



directories  = open(word_list, 'r')
dirs = directories.readlines()
lines = len(dirs)
directories.close()


print "Starting bruteforce of " + url + " with " + str(lines) + " directories"

for dir in dirs:
	uri = url + "/" + dir
	#print uri
	try:
		r = requests.get(uri)
		d = r.status_code
		code = '200'
		if d == int(code):
			print "URL Found: " + uri.strip()
		else:
			pass

	except requests.ConnectionError, e:
    		print e 

