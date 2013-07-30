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
		fix_children()

def current_ws():
	if whitespacing == 0 or not tab_spaced:
		return len(line) - len(line.lstrip())
	if tab_spaced:
		return len(line) - len(line.lstrip('\t\n\r'))

def last_parent_index(fudge):
	
	if fudge == 0:
		test_array = whitespace_array
	else:
		test_array = whitespace_array[:fudge]
	i = len(test_array) - 1
	for key, value in reversed(list(enumerate(test_array))):
		if value > (whitespace_array[key-1]):
			return key - 1
	return i
		# if '{' in value:
			# print '{0!s}: {1!s}'.format(key,value)
			# return key

def last_spinster(fudge):
	if fudge == 0:
		test_array = whitespace_array
	else:
		test_array = whitespace_array[:fudge]
	i = len(test_array) - 1
	for key, value in reversed(list(enumerate(test_array))):
		if value > (whitespace_array[key-1]):
			i = key
		if value < (whitespace_array[key-1]):
			return i + 1
	return i + 1

def lastfirst_with_value(keyofvalue):
	i = keyofvalue
	for key, value in reversed(list(enumerate(whitespace_array[:keyofvalue]))):
		if value == whitespace_array[keyofvalue]:
			i = key
		else:
			return i

def fix_children():
	#commas after each closed item
	json_to_write[-1] = json_to_write[-1] + ","
	
	#properties with only one childless child
	if (whitespace_array[-2] > whitespace_array[-3]) and (whitespace_array[-1] < whitespace_array[-2]):
		json_to_write[-1] = json_to_write[-1].replace(': {}}','')
		json_to_write[-2] = json_to_write[-2][:-2]
		return
		
	#properties that are local max for whitespace and have only childless children
	if (whitespace_array[-1] < whitespace_array[-2]) and (whitespace_array[-2] == whitespace_array[-3]):
		y = len(json_to_write) - 1
		first_in_series = lastfirst_with_value(last_spinster(y) % len(json_to_write))
		last_parent = last_parent_index(y+1)
		if (first_in_series - last_parent) == 1:
			json_to_write[last_parent-1] = json_to_write[last_parent-1][:-2] + "["
			json_to_write[-1] = json_to_write[-1][:-2] + "],"
			for x in xrange(last_parent,y+1):
				json_to_write[x] = json_to_write[x].replace(': {}','')

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
		
		close_tags()
		# fix_children()
		
		#deal with single line properties
		if ":" in stripped_line:
			propertysplit = stripped_line.strip().split(":")
			property = propertysplit[0].strip()
			propertyvalue = propertysplit[1].lstrip() + ':'.join(propertysplit[2:])
			json_to_write.append(quoted(property) + ": {")
			json_to_write.append(quoted(propertyvalue) + ": {")
			unclosed_tags.append(property)
			unclosed_tags.append(propertyvalue)
			whitespace_array.append(whitespace_array[-1]+1)
			continue
		
		#deal with property names (called tags here)
		json_to_write.append(quoted(stripped_line.strip())+": {")
		unclosed_tags.append(stripped_line)
		
		# For debugging purposes:
		a = ''.join(json_to_write)
		b = ','.join(unclosed_tags)
		c = ', '.join(str(x) for x in whitespace_array)
		d = '\n'.join('{0!s}~ {1}'.format(whitespace_array[x+1], json_to_write[x]) for x in xrange(len(json_to_write)))
		
		print '{0!s}\n{1!s}\n{2!s}'.format(a,b,c)
		# print d
		
	#close any unclosed tags at the end
	for key, tag in enumerate(reversed(unclosed_tags)):
		json_to_write[-1] = json_to_write[-1] + "}"
	
	whitespace_array.append(-1)
	
	json_to_write[-1] = json_to_write[-1] + "}"

# d = '\n'.join('{2!s}: {0!s}~ {1} {3},{4},{5}'.format(whitespace_array[x], json_to_write[x], x, last_spinster(x), last_parent_index(x+1), lastfirst_with_value(last_spinster(x) % len(json_to_write))) for x in xrange(len(json_to_write)))
# print d

primary = ''.join(json_to_write).replace("{}","\"\"")
print primary


intermediate = json.loads(primary)
secondary = json.dumps(intermediate,indent=4)

# print secondary

with codecs.open(jsfilename,'wU','utf-8') as jsonfile:
	jsonfile.write(secondary)