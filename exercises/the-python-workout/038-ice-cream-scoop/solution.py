"""Exercise 38: Ice Cream Scoop"""

class Scoop():
    
    def __init__(self, name):
        self.name = name

def create_scoops():
    scoops = [Scoop("chocolate"),Scoop("vanilla"),Scoop("persimmon")]
    for scoop in scoops:
        print(scoop.name)

create_scoops()

