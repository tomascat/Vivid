##Vivid

A simple and elegant markup language that compiles to HTML & XML (and soon JSON). Vivid is clear markup that looks like an outline, just like something written with a permanent marker ;)

###How to use the converter

- Vivid files can be created in any text editor of your choice, but at this stage should be encoded in Unicode, preferably UTF-8.
- At the moment you need Python 2+ installed to make use of the script.
- Simply download 'xconverter.py' and the 'markdown' directory to the directory you want to use it in.
- Open a command-line and enter 'python xconverter.py [filename of your vivid file] [filename of the html file you want to output]'
- That's it!

###Syntax - XML & HTML

####Starting out, tags, whitespace and nesting tags

Vivid uses indentation (tab or spaces) much like an outlining tool to organise the DOM rather than start and end tags. Here is a simple example:

<pre>
div
	div
		p
	div
		p
</pre>

will automatically nest the tags and convert to:

<pre>
&lt;div&gt;
	&lt;div&gt;
		&lt;p&gt;
		&lt;/p&gt;
	&lt;/div&gt;
	&lt;div&gt;
		&lt;p&gt;
		&lt;/p&gt;
	&lt;/div&gt;
&lt;/div&gt;
</pre>

much as you'd expect it to.

Whichever indentation regime you prefer will be supported as long as you are consistent; tab-spaces, 2-space and 4-space and other schemes that use multiples of a space are all supported and automatically detected.

The output is currently tab-spaced only.

####Text

Text is designated with a leading # or between two ##s:

<pre>
p
	#Based on ideal line length 50-75 characters.
p
	##As you can see... blah blah blah
	this is a multi-line block##
p
	##
	This is another multi line block
	that I have created
	##
</pre>

converts to:

<pre>
&lt;p&gt;
	Based on ideal line length 50-75 characters.
&lt;/p&gt;
&lt;p&gt;
	As you can see... blah blah blah&lt;br /&gt;
	this is a multi-line block
&lt;/p&gt;
&lt;p&gt;
	This is another multi line block&lt;br /&gt;
	that I have created
&lt;/p&gt;
</pre>

If you have a single line of text and want to put it on the same line as the tag it belong to you can:

<pre>
table
	tr
		th#First Name
		th#Surname
		th#Age
	tr
		td#Adam
		td#Adamsen
		td#40
	tr
		td#Mavis
		td#Withers
		td#92
</pre>

will turn into:

<pre>
&lt;table&gt;
	&lt;tr&gt;
		&lt;th&gt;
			First Name
		&lt;/th&gt;
		&lt;th&gt;
			Surname
		&lt;/th&gt;
		&lt;th&gt;
			Age
		&lt;/th&gt;
	&lt;/tr&gt;
	&lt;tr&gt;
		&lt;td&gt;
			Adam
		&lt;/td&gt;
		&lt;td&gt;
			Adamsen
		&lt;/td&gt;
		&lt;td&gt;
			40
		&lt;/td&gt;
	&lt;/tr&gt;
	&lt;tr&gt;
		&lt;td&gt;
			Mavis
		&lt;/td&gt;
		&lt;td&gt;
			Withers
		&lt;/td&gt;
		&lt;td&gt;
			92
		&lt;/td&gt;
	&lt;/tr&gt;
&lt;/table&gt;
</pre>

####Attributes (eg id, class, type)

Assigning attributes (such as id or class) is easy; on a new line after a tag, just add an extra indent with the syntax attribute:value as follows:

<pre>
div
	id:kafka
	class:blocktext
	data-category:3
</pre>

which will turn into:

<pre>
&lt;div id="kafka" class="blocktext" data-category="3"&gt;
&lt;/div&gt;
</pre>

You can also use attributes on multiple lines by using 'attribute:', indenting the values you want to use and putting a semicolon at the end, like so:

<pre>
div
	id:
		kafka
		blocktext
		menu;
</pre>

which turns into:

<pre>
&lt;div id="kafka blocktext menu"&gt;
&lt;/div&gt;
</pre>

####Tags you can use

You can use whichever tags you like as long as they don't start with '#' or contain ':'

<pre>
hello
	these
		are
		some
	tags
</pre>

ie

<pre>
&lt;hello&gt;
	&lt;these&gt;
		&lt;are&gt;
		&lt;/are&gt;
		&lt;some&gt;
		&lt;/some&gt;
	&lt;/these&gt;
	&lt;tags&gt;
	&lt;/tags&gt;
&lt;/hello&gt;
</pre>

####Markdown

<a href="http://daringfireball.net/projects/markdown/">Markdown</a> is supported (courtesy of The Python Markdown Project, see copyright/licence details below), starting and ending with '#markdown#':

<pre>
div
	#markdown#
	Here is some **Markdown** for your viewing pleasure:
	* A list perhaps?
	* I think that sounds grand!
	*Spectacular*, if I do say so myself!
	#markdown#
</pre>

converts to:

<pre>
&lt;div&gt;
	&lt;p&gt;Here is some &lt;strong&gt;Markdown&lt;/strong&gt; for your viewing pleasure:&lt;/p&gt;
	&lt;ul&gt;
	&lt;li&gt;
	&lt;p&gt;A list perhaps?&lt;/p&gt;
	&lt;/li&gt;
	&lt;li&gt;
	&lt;p&gt;I think that sounds grand!&lt;/p&gt;
	&lt;/li&gt;
	&lt;/ul&gt;
	&lt;p&gt;&lt;em&gt;Spectacular&lt;/em&gt;, if I do say so myself!&lt;/p&gt;
&lt;/div&gt;
</pre>

Indentation not as nice but I'm working on it!

Markdown project and syntax available at <a href="http://daringfireball.net/projects/markdown/">Daring Fireball</a>

####Putting it all together: a complex example

Here is a particularly involved example (example.vivid and example.html):

<pre>
html
	lang:en
	head
		meta
			charset:utf-8
		title
			#Ideal line lengths by font
		script
			src://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js
		script
			src:linelength.js
		link
			rel:stylesheet
			href:linelength.css
	body
		div
			id:heading
			h1
				#Ideal Line Lengths by Font
		div
			id:intro
			p
				#Based on ideal line length 50-75 characters.
			p
				##As you can see... blah blah blah
				this is a multi-line block##
			p
				##
				This is another multi line block
				that I have created
				##
		div
			id:tester
			h2
				#Test it out here:
			input
				type:range
				id:charsperline
				max:75
				min:50
				step:1
				value:62
			class:kafka
			ul
				class:fiddle
				li
					#An item
				li
					#Another item
</pre>

converts to:

<pre>
&lt;html lang="en"&gt;
	&lt;head&gt;
		&lt;meta charset="utf-8"&gt;
		&lt;/meta&gt;
		&lt;title&gt;
			Ideal line lengths by font
		&lt;/title&gt;
		&lt;script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js"&gt;
		&lt;/script&gt;
		&lt;script src="linelength.js"&gt;
		&lt;/script&gt;
		&lt;link rel="stylesheet" href="linelength.css"&gt;
		&lt;/link&gt;
	&lt;/head&gt;
	&lt;body&gt;
		&lt;div id="heading"&gt;
			&lt;h1&gt;
				Ideal Line Lengths by Font
			&lt;/h1&gt;
		&lt;/div&gt;
		&lt;div id="intro"&gt;
			&lt;p&gt;
				Based on ideal line length 50-75 characters.
			&lt;/p&gt;
			&lt;p&gt;
				As you can see... blah blah blah&lt;br /&gt;
				this is a multi-line block
			&lt;/p&gt;
			&lt;p&gt;
				This is another multi line block&lt;br /&gt;
				that I have created
			&lt;/p&gt;
		&lt;/div&gt;
		&lt;div id="tester" class="kafka"&gt;
			&lt;h2&gt;
				Test it out here:
			&lt;/h2&gt;
			&lt;input type="range" id="charsperline" max="75" min="50" step="1" value="62"&gt;
			&lt;/input&gt;
			&lt;ul class="fiddle"&gt;
				&lt;li&gt;
					An item
				&lt;/li&gt;
				&lt;li&gt;
					Another item
				&lt;/li&gt;
			&lt;/ul&gt;
		&lt;/div&gt;
	&lt;/body&gt;
&lt;/html&gt;
</pre>

Have fun!

###Credits & Licence information

####Vivid

Vivid is licenced under **The MIT License (MIT)**

**Copyright &copy; 2013 Vivid Project**

Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.

####Markdown module courtesy of The Python Markdown Project:

Copyright 2007, 2008 The Python Markdown Project (v. 1.7 and later)  
Copyright 2004, 2005, 2006 Yuri Takhteyev (v. 0.2-1.6b)  
Copyright 2004 Manfred Stienstra (the original version)  

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    
*   Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
*   Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
*   Neither the name of the <organization> nor the
    names of its contributors may be used to endorse or promote products
    derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE PYTHON MARKDOWN PROJECT ''AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL ANY CONTRIBUTORS TO THE PYTHON MARKDOWN PROJECT
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
