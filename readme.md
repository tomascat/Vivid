##Vivid

A simple and elegant markup language that compiles to HTML (and soon to XML and JSON). Vivid is clear markup that looks like an outline, just like something written with a permanent marker ;)

###How to use it

- Vivid files can be created in any text editor of your choice.
- At the moment you need Python 2+ installed to make use of the script.
- Simply download 'htmlconverter.py' to the directory you want to use it in.
- Open a command-line and enter 'python htmlconverter.py [filename of your vivid file] [filename of the html file you want to output]'
- That's it!

###Syntax - HTML

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

####Properties (eg id, class, type)

Assigning properties (such as id or class) is easy; on a new line after a tag, just add an extra indent with the syntax property:value as follows:

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

####New tags

If you're particularly adventurous you can of course make up random tags:

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

Even though I'm not sure why you'd want to! This does mean that new tags in the HTML arsenal will be supported.

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