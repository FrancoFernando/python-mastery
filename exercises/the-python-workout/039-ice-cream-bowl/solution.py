"""Exercise 39: Ice Cream Bowl"""

class Scoop():
    def __init__(self, name):
        self.name = name

class Bowl():
    def __init__(self):
        self.scoops = []

    def __str__(self):
        return ",".join(scoop.name for scoop in self.scoops)

    def add_scoops(self, *scoops):
        self.scoops.extend(scoops)
    


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b)
