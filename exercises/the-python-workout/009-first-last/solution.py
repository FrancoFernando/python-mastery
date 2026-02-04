"""Exercise 9: First Last"""

def firstlast(sequence):
    return sequence[0::len(sequence)-1]

def firstlast_v2(sequence):
    return sequence[:1] + sequence[-1:]

print(firstlast([1,2,3]))
print(firstlast((1,2,3)))
print(firstlast('abc'))

print(firstlast_v2([1,2,3]))
print(firstlast_v2((1,2,3)))
print(firstlast_v2('abc'))