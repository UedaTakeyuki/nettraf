#-*- coding:utf-8 -*-
# Copy Right Takeyuki UEDA  © 2018 - All rights reserved.
import os
import re
import datetime

if not os.path.exists('/var/log/nettraf/'):
	os.makedirs('/var/log/nettraf/')

regex = r'\s*(\w*):(.*)'
pattern = re.compile(regex)

x=open('/proc/net/dev','r')
for line in x.readlines():
  line = line.strip()
  result = pattern.match(line)

  if result:
  	logfilename = '/var/log/nettraf/'+result.groups()[0]
  	logline = re.sub(r'\s+', ',', result.groups()[1])
#  	logline = result.groups()[1]

  	with open(logfilename,'a') as f:
  		f.write(str(datetime.datetime.now())
  			      +','+logline+"\n")



