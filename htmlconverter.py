#! python
# -*- coding: utf-8 -*-

def stripped(str):
	if tab_spaced:
		return str.lstrip('\t').rstrip('\n\r')
	else:
		return str.lstrip().rstrip('\n\r')

def indented (str,i):
	return ("\t"*(len(unclosed_tags)-i) + str + "\n")

def write_indented (str,i,writearray):
	return writearray.append(indented(str,i))

def close_tags():
	if currentws <= previousws:
		for x in xrange(1+int(round((previousws-currentws)/float(whitespacing)))):
			write_indented("</"+unclosed_tags[-1]+">",1,html_to_write)
			unclosed_tags.pop()

def last_tag_index():
	tagindex = 0
	for key,value in enumerate(reversed(html_to_write)):
		if stripped(value).startswith('<'+unclosed_tags[-1]):
			tagindex = -1 - key
			return tagindex
	return tagindex

def current_ws():
	if whitespacing == 0 or not tab_spaced:
		return len(line) - len(line.lstrip())
	if tab_spaced:
		return len(line) - len(line.lstrip('\t\n\r'))

import codecs
import sys

#initialise variables
html_to_write = []
unclosed_tags = []
debug = []
vividfilename = sys.argv[1]
htmlfilename = sys.argv[2]
currentws = 0
previousws = -1
whitespacing = 0
tab_spaced = False
last_type_tag = False
multi_line_text = False

#open the file
with codecs.open(vividfilename,'rU', "utf-8-sig") as vividfile:
	
	for line in vividfile:
		#work out how many whitespaces at start
		currentws = current_ws()
		
		#For first line with whitespace, work out the whitespacing (eg tab vs 4-space)
		if whitespacing == 0 and currentws > 0:
			whitespacing = currentws
			if line[0] == '\t':
				tab_spaced = True
		
		#strip out whitespace at start and end
		stripped_line = stripped(line)
		
		#deal with unclosed multiline text
		if multi_line_text:
			#work out if it's been closed on this line, close if it has, append appropriately
			if stripped_line.endswith('##'):
				if len(stripped(line)) > 2:
					write_indented(stripped_line[:-2],0,html_to_write)
				#if it's just a closing '##', get rid of the <br /> on the previous line
				else:
					html_to_write.append(html_to_write[-1][:-7] + "\n")
					html_to_write.pop(-2)
				multi_line_text = False
			else:
				write_indented(stripped_line + "<br />",0,html_to_write)
			continue
		
		#deal with text ie things starting with '#'
		if stripped_line.startswith('#'):
			#if the current tag has less whitespace than the last, close all tags up to this one
			close_tags()
			#deal with start of multiline text (first '##')
			if stripped_line.startswith('##'):
				#deal with when it starts and ends on the same line
				if stripped_line.endswith('##') and len(stripped(line)) > 2:
					write_indented(stripped_line[2:-2],0,html_to_write)
					continue
				#if it just starts with '##', append as necessary
				if len(stripped(line)) > 2:
					write_indented(stripped_line[2:] + "<br />",0,html_to_write)
				multi_line_text = True
			#deal with single line text
			else:
				write_indented(stripped_line[1:],0,html_to_write)
			#skip the rest of the cycle.
			continue
		
		#deal with everything else
		
		#deal with properties eg class:20
		if ":" in stripped_line:
			#if the current tag has less whitespace than the last, close all tags up to this one
			close_tags()
			#break the property up and insert it into the last tag
			tagstart = html_to_write[last_tag_index()].strip()[:-1]
			propertysplit = stripped_line.strip().split(":")
			property = propertysplit[0].strip()
			propertyvalue = propertysplit[1].lstrip() + ':'.join(propertysplit[2:])
			html_to_write[last_tag_index()] = indented(tagstart + " " + property + "=\"" + propertyvalue + "\">",1)
			# write_indented(tagstart + " " + property + "=\"" + propertyvalue + "\">",1,html_to_write)
			#set the last type to not be a tag
			last_type_tag = False
			#reduce whitespace by one as it's a property
			currentws -= whitespacing
			
		
		#deal with tags eg div
		else:
			#if the current tag has less whitespace than the last, close all tags up to this one
			close_tags()
			#append the current tag
			write_indented("<"+stripped_line.strip()+">",0,html_to_write)
			unclosed_tags.append(stripped_line.strip())
			#set the last type to be a tag
			last_type_tag = True
			
		# For debugging purposes:
		a = ''.join(html_to_write)
		b = ','.join(unclosed_tags)
		print str(last_type_tag) + "," + str(currentws) + "," + stripped_line + "," + str(previousws) + "\n" + a + "\n" + b + "\n\n"
		
		previousws = currentws
	
	#close any unclosed tags at the end
	for key, tag in enumerate(reversed(unclosed_tags)):
		write_indented("</"+tag+">",key+1,html_to_write)

s = ''.join(html_to_write)

with codecs.open(htmlfilename,'wU','utf-8') as htmlfile:
	htmlfile.write(s)