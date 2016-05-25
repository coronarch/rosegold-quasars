#/usr/bin/python

# 
# RoSeGold-Quasars
# 
# File system organization for music libraries
# author: Andrew Hayford <github.com/coronarch>
#

import os, zipfile, datetime

# Get current date for log and organization
now = datetime.datetime.now()
now_str = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '\n'

dir_needed = False

# Try to open rsgq config file
try:
	fp = open('config.txt', 'r') 
except IOError:
	print 'Cannot open RoSeGold-Quasars configurations', arg
else:
	#TO-DO: read in directory information to variables

# Try to open rsgq log file 
try:
	fp = open('log.txt', 'ab+')
except IOError:
	print 'Cannot open RoSeGold-Quasars log file', arg
else:
	if os.stat('log.txt').st_size != 0:
		# Find the last date we used program
		lines = fp.readlines()
		last = lines[-1] 
		
		# If we haven't used rsgq today, create new log entry
		if (now_str != last):
			fp.write(now_str) 
			fp.close() 
			dir_needed = True
	else:
		# First time using rsgq
		fp.write(now_str) 
		fp.close() 
		dir_needed = True


