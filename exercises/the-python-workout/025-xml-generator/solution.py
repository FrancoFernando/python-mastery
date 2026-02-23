"""Exercise 25: Xml Generator myxml('foo') <foo></foo>
 myxml('foo', 'bar') <foo>bar</foo>
 myxml('foo', 'bar', a=1, b=2, c=3) <foo a="1" b="2" c="3">bar</foo>"""

def myxml(tagname, content ="", **kwargs):
    attributes = " ".join([f'{key}="{value}"' for key, value in kwargs.items()])
    return f"<{tagname} {attributes}>{content}</{tagname}>" 
    
print(myxml('foo', 'bar', a=1, b=2, c=3))
