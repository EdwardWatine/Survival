import math, random
from itemClasses

class desert:

    def __init__(self):
        self.temp = 2
        self.actions = []
        
    def __str__(self):
        return "D"
        
class mountain:

    def __init__(self):
        self.temp = -2
        self.actions = []
        
    def __str__(self):
        return "M"
        
class forest:

    def __init__(self):
        self.temp = -1
        self.actions = []
        
    def __str__(self):
        return "F"   
        
class plain:

    def __init__(self):
        self.temp = 0
        self.actions = []
        
    def __str__(self):
        return "P"

class square: 
        
    def __init__(self, coord):
        
        places = [mountain(), forest(), plain()]
        self.coord = coord
        self.distance = math.sqrt(sum([x**2 for x in coord]))
        chanceOfDesert = self.distance/15
        if random.random() < chanceOfDesert:
            self._type = desert()
        else:
            self._type = random.choice(places)
            
    def __str__(self):
        return str(self._type)
            
class _map:
    
    def __init__(self):
        self.discmax = 2
        self.strarr = [["?","?","?"], ["?",square((0, 0)),"?"], ["?","?","?"]]
        
    def move(self, coord):
        if self.discmax-1 < max([abs(x) for x in coord])+1:
            self.discmax += 1
            for x in self.strarr:
                x.append("?")
                x.insert(0, "?")
            self.strarr.append(["?" for x in range(self.discmax*2 -1)])
            self.strarr.insert(0, ["?" for x in range(self.discmax*2 - 1)])
            
        if not self.isDisc(coord):
            self.strarr[-coord[1]+self.discmax-1][coord[0]+self.discmax-1] = square(coord)
        
    def isDisc(self, coord):
        return self.strarr[-coord[1]+self.discmax-1][coord[0]+self.discmax-1] != "?"
            
    def __str__(self):
        
        return ("\n"*len(str(-self.discmax))).join(["   ".join([str(self.discmax-1-z)+(" "*(len(str(-self.discmax+1))-len(str( self.discmax-1-z))+1))]+[str(y) for y in x]) for z, x in enumerate(self.strarr)]+
        	["\n"+(" "*(len(str(-self.discmax))+3))+" ".join([str(-self.discmax+z+1)+(" "*(3-len(str(-self.discmax+z+2)))) for z in range(len(self.strarr)) ])] )

    def __getitem__(self, coord):
        return self.strarr[-coord[1]+self.discmax-1][coord[0]+self.discmax-1]
