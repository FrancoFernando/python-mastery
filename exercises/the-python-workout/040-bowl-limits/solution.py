"""Exercise 40: Bowl Limits"""

"""Exercise 39: Ice Cream Bowl"""

class Scoop():
    def __init__(self, name):
        self.name = name

class Bowl():
    max_scoops = 3
    def __init__(self):
        self.scoops = []

    def __str__(self):
        return ",".join(scoop.name for scoop in self.scoops)

    def add_scoops(self, *scoops):
        for scoop in scoops:
            if len(self.scoops) < Bowl.max_scoops:
                self.scoops.append(scoop)

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s1) # ignored
print(b)

