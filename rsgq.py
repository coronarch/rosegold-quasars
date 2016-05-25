#/usr/bin/python

# 
# RoSeGold-Quasars
# 
# File system organization for music libraries
# author: Andrew Hayford <github.com/coronarch>
#

import os, zipfile, datetime

now = datetime.datetime.now()
dir_needed = False

# Try to open rsgq log file 
try:
	fp = open('log.txt', 'ab+')
except IOError:
	print 'Cannot open RoSeGold-Quasars log file', arg
else:
	# Find the last date we used program
	lines = fp.readlines()
	last = lines[-1] 
	
	if (now != datetime.datetime.strptime(last, "%Y-%m-%d") ):
		fp.write(str(now.year) + '-' + str(now.month) 
			+ '-' + str(now.day) + '\n') 
		fp.close() 


