"""Exercise 25: Xml Generator myxml('foo') <foo></foo>
 myxml('foo', 'bar') <foo>bar</foo>
 myxml('foo', 'bar', a=1, b=2, c=3) <foo a="1" b="2" c="3">bar</foo>"""

def myxml(name, content ="", **kwargs):
    attributes = [f"{key}=\"{value}\"" for key, value in kwargs.items()]
    attributes_str = " ".join(attributes)
    opening_tag = f"<{name} {attributes_str}>"
    closing_tag = f"</{name}>"
    return "".join([opening_tag, content, closing_tag])
    
print(myxml('foo', 'bar', a=1, b=2, c=3))


