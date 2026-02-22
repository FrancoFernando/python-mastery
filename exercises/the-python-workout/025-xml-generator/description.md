# Exercise 25: Xml Generator

## Description

Write a function, myxml, that allows you to create simple XML output. The output from the function will always be a string. The function can be invoked in a number of way. In all cases, the first argument is the name of the tag. In the latter two cases, the second argument is the content (text) placed between the opening and closing tags. And in the third case, the name–value pairs will be turned into attributes inside the opening tag.

myxml('foo') <foo></foo>
 myxml('foo', 'bar') <foo>bar</foo>
 myxml('foo', 'bar', a=1, b=2, c=3) <foo a="1" b="2" c="3">bar</foo>
 