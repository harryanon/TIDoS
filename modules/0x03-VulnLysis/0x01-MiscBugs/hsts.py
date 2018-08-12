#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID
#This module requires TIDoS Framework
#https://github.com/theInfectedDrake/TIDoS-Framework 

import os
import time
import requests
import sys
from colors import *

def check0x00(headers):
	for head in headers:
		if 'Strict-Transport-Security'.lower() in head.lower():
			print O+' [!] Reflection in response headers found...'
			flag = True
	if flag == True:
		print G+' [+] Seems like the website uses strong HSTS...'
		time.sleep(0.6)
		print G+' [+] HSTS Presence Confirmed!'
	else:
		print R+' [-] Website does not seem to use HSTS...'

def getHeaders0x00(web):
	print O+' [*] Configuring headers...'
	time.sleep(0.5)
	gen_headers =    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
		   	  'Accept-Language':'en-US;',
		   	  'Accept-Encoding': 'gzip, deflate',
		   	  'Accept': 'text/html,application/xhtml+xml,application/xml;',
		   	  'Connection':'close'}
	input_cookie = raw_input(C+" [*] Got any cookies? [just enter if none] :> ")
	if(len(input_cookie) > 0):
		gen_headers['Cookie'] = input_cookie
	print GR+' [*] Making the request...'
	time.sleep(0.6)
	req = requests.get(web, headers=gen_headers, timeout=5, verify=True)
	h = req.headers
	return h

def hsts(web):
	print GR+' [*] Loading module...'
	time.sleep(0.5)
	print R+'\n    ================================'
	print R+'     HTTP STRICT TRANSPORT SECURITY'
	print R+'    ================================\n'
	if 'https' in web:
		m = getHeaders0x00(web)
		check0x00(m)
	else:
		print R+' [-] No SSL/TLS detected...'
		m = raw_input(O+' [#] Force SSL/TLS (y/N) :> ')
		if m == 'y' or m == 'Y':
			print GR+' [*] Using revamped SSL...'
			o = 'https://' + web.replace('http://','')
			m = getHeaders0x00(web)
			check0x00(m)
		elif m == 'n' or m == 'N':
			print GR+' [-] Skipping module...'
			pass		
