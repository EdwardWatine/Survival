<<<<<<< HEAD
import random, math
import MapClasses as mc
#from ItemData import items

=======
import random
>>>>>>> fd6c303d1061107a6e156311eea9ab53b4d28ccf
class DayStats:

    def __init__(self):
        self.seasons = ["Spring", "Summer", "Autumn", "Winter"]
        self.choices = [[12, 20], [18, 30], [5, 15], [-5, 10]]
        self.temp = random.randint(*self.choices[0])
        self.season = "Spring"

    def newDay(self, days):
        self.temp = random.randint(*self.choices[((days-1)%360)//90])
        self.season = self.seasons[((days-1)%360)//90]

class Time:

    def __init__(self, DayStats):
        self.days = 1
        self.hours = 9
        self.mins = 0
        self.DayStats = DayStats
        
    def __str__(self):
        return ("""{}
Day {:d}
{}\xb0C
"""+
        	("0"*(self.hours<10))+
        		"{:d}:"+
        			("0"*(self.mins<10))+
        				"{:d}").format(self.DayStats.season, self.days, self.DayStats.temp, self.hours, self.mins)
        
<<<<<<< HEAD
    def add(self, mins, hours, days=0):
=======
    def add(self, hours, mins=0, days=0):
>>>>>>> fd6c303d1061107a6e156311eea9ab53b4d28ccf
        self.mins += mins
        self.hours += hours + self.mins//60
        self.days += days + self.hours//24
        if days + self.hours//24 > 0:
            self.DayStats.newDay(self.days)
        self.mins %= 60
        self.hours %= 24

class Inventory:

<<<<<<< HEAD
    def __init__(self, d={}):
=======
    def __init__(self, d):
>>>>>>> fd6c303d1061107a6e156311eea9ab53b4d28ccf
        self.contents = d
        
    def __str__(self):
        return "\n".join(
        	["- '{}' x{}".format(x, self.contents[x]) for x in self.contents]
        	) if self.contents else "This inventory is empty!"
        	
    def add(self, request):
        for x in request:
            if x in self.contents:
                self.contents[x] += request[x]
            else:
                self.contents[x] = request[x]
            
    def remove(self, request):
        for x in request:
            if x in self.contents:
                self.contents[x] -= request[x]
                if self.contents[x] < 1:
                    del self.contents[x]   
        
    def check(self, request):
        for x in request:
            if x not in self.contents:
                return False
            if request[x] > self.contents[x]:
                return False
        return True
            
    def PopIfPresent(self, request):
        if self.check(request):
            self.remove(request)
            return True
        return False

class Person:
<<<<<<< HEAD

=======
>>>>>>> fd6c303d1061107a6e156311eea9ab53b4d28ccf
    def __init__(self):
        self.health = 100
        self.effects = []
        self.hunger = 100
<<<<<<< HEAD
        self.temp = 35
        self.thirst = 100
        self.sleep = 100
        self.position = (0, 0)
        self.inventory = Inventory()
        self._map = mc._map()
        
while True:
    exec(raw_input())
=======
        self.thirst = 100
        self.sleep = 100
        self.inventory = Inventory()
        """self.equipment = {
        	"weapon":weapon("Fist"),
        	"shield":armour("Shield"),
        "head":armour("None"), 
        "chest":armour("Woolen Jumper"),
        "legs":armour("Cloth Trousers"),
        "arms":armour("None"),
        "hands":armour("None"),
        "feet":armour("Trainers")
        }"""
>>>>>>> fd6c303d1061107a6e156311eea9ab53b4d28ccf
