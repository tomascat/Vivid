#! python
# -*- coding: utf-8 -*-

#Import relevant libraries
import codecs
import sys
import json

#Functions
def stripped(s):
	if tab_spaced:
		return s.lstrip('\t').rstrip('\n\r')
	else:
		return s.lstrip().rstrip('\n\r')

def quoted(s):
	return '"'+s+'"'

def close_tags():
	if (whitespace_array[-1] <= whitespace_array[-2]) and (whitespacing>0):
		for x in xrange(1+int(round((whitespace_array[-2]-whitespace_array[-1])/float(whitespacing)))):
			json_to_write[-1] = json_to_write[-1] + "}"
			unclosed_tags.pop()

def current_ws():
	if whitespacing == 0 or not tab_spaced:
		return len(line) - len(line.lstrip())
	if tab_spaced:
		return len(line) - len(line.lstrip('\t\n\r'))

def last_parent_index():
	i = -1
	for key, value in reversed(list(enumerate(json_to_write))):
		if '{' in value:
			# print '{0!s}: {1!s}'.format(key,value)
			return key

def fix_children():
	if (whitespace_array[-2] > whitespace_array[-3]) and (whitespace_array[-1] < whitespace_array[-2]):
		json_to_write[-1] = json_to_write[-1].replace(': {}}','') + ','
		json_to_write[-2] = json_to_write[-2][:-2]
		return
	if whitespace_array[-1] <= whitespace_array[-2]:
		json_to_write[-1] = json_to_write[-1] + ","
		json_to_write[-1] = json_to_write[-1].replace(': {}','')
	if (whitespace_array[-1] < whitespace_array[-2]):
		if (whitespace_array[-2] == whitespace_array[-3]):
			json_to_write[last_parent_index()] = json_to_write[last_parent_index()][:-1] + "["
			json_to_write[-1] = json_to_write[-1].replace('"}','"]')

#initialise variables
json_to_write = []
unclosed_tags = []
debug = []

# vividfilename = 'simple.vivid'
vividfilename = sys.argv[1]
if len(sys.argv)>2:
	jsfilename = sys.argv[2]
else:
	jsfilename = vividfilename.split('.')[0] + '.json'

whitespacing = 0
whitespace_array = [-2,-1]
tab_spaced = False

#open the file
with codecs.open(vividfilename,'rU', "utf-8-sig") as vividfile:
	
	json_to_write.append("{")
	
	for line in vividfile:
		#work out how many whitespaces at start
		whitespace_array.append(current_ws())
		
		#For first line with whitespace, work out the whitespacing (eg tab vs 4-space)
		if whitespacing == 0 and whitespace_array[-1] > 0:
			whitespacing = whitespace_array[-1]
			if line[0] == '\t':
				tab_spaced = True
		
		#strip out whitespace at start and end
		stripped_line = stripped(line)
		
		#deal with property names (called tags here)
		close_tags()
		
		fix_children()
		
		json_to_write.append(quoted(stripped_line.strip())+": {")
		unclosed_tags.append(stripped_line)
		
		# For debugging purposes:
		# a = ''.join(json_to_write)
		# b = ','.join(unclosed_tags)
		
	#close any unclosed tags at the end
	for key, tag in enumerate(reversed(unclosed_tags)):
		json_to_write[-1] = json_to_write[-1] + "}"
	
	whitespace_array.append(-1)
	fix_children()
	
	print str(whitespace_array[-4:])
	
	json_to_write[-1] = json_to_write[-1][:-1] + "}"

primary = ''.join(json_to_write)
print primary
intermediate = json.loads(primary)
secondary = json.dumps(intermediate,indent=4)

print secondary

with codecs.open(jsfilename,'wU','utf-8') as jsonfile:
	jsonfile.write(secondary)