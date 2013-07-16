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
<div>
	<div>
		<p>
		</p>
	</div>
	<div>
		<p>
		</p>
	</div>
</div>
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
<p>
	Based on ideal line length 50-75 characters.
</p>
<p>
	As you can see... blah blah blah<br />
	this is a multi-line block
</p>
<p>
	This is another multi line block<br />
	that I have created
</p>
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
<div id="kafka" class="blocktext" data-category="3">
</div>
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
<hello>
	<these>
		<are>
		</are>
		<some>
		</some>
	</these>
	<tags>
	</tags>
</hello>
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
<html lang="en">
	<head>
		<meta charset="utf-8">
		</meta>
		<title>
			Ideal line lengths by font
		</title>
		<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js">
		</script>
		<script src="linelength.js">
		</script>
		<link rel="stylesheet" href="linelength.css">
		</link>
	</head>
	<body>
		<div id="heading">
			<h1>
				Ideal Line Lengths by Font
			</h1>
		</div>
		<div id="intro">
			<p>
				Based on ideal line length 50-75 characters.
			</p>
			<p>
				As you can see... blah blah blah<br />
				this is a multi-line block
			</p>
			<p>
				This is another multi line block<br />
				that I have created
			</p>
		</div>
		<div id="tester" class="kafka">
			<h2>
				Test it out here:
			</h2>
			<input type="range" id="charsperline" max="75" min="50" step="1" value="62">
			</input>
			<ul class="fiddle">
				<li>
					An item
				</li>
				<li>
					Another item
				</li>
			</ul>
		</div>
	</body>
</html>
</pre>

Have fun!