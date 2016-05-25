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

temp_dir = ''
musi_dir = ''
down_dir = ''


# Try to open rsgq log and config file 
try:
	with open('log.txt', 'ab+') as fp_1, open('config.txt', 'r') as fp_2:
		# Check if file is empty
		if os.stat('log.txt').st_size != 0:
			# Find the last date we used program
			lines = fp_1.readlines()
			last = lines[-1] 
		
			# If we haven't used rsgq today, create new log entry
			if (now_str != last):
				fp_1.write(now_str) 
				fp_1.close() 
				dir_needed = True
		else:
			# First time using rsgq
			fp_1.write(now_str) 
			fp_1.close() 
			dir_needed = True

		

except IOError as e:
	print 'Cannot open RoSeGold-Quasars log file: %s' % e.strerror


