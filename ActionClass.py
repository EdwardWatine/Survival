class action:
     
    def __init__(self, name, time, rew, chain, args=(), kwargs={}):
         self.name = name
         self.time = time
         self.rew = rew
         self.chain = chain
         self.args = args
         self.kwargs = kwargs
     
    def checkReq(self, cls):
        if not self.chain:
             return True
        for x in self.chain:
               cls = getattr(cls, x)
        return cls(*self.args, **self.kwargs)  
        
    def __str__(self):
        return "\n".join([x+" - "+str(getattr(self, x)) for x in dir(self)])
           
#MDGF
actions4all = [
    ( "Collect resources", (10, 0, 0), ({"Branch":(2, 3)}, {}, {"Branch":(1,2), "Twine":(3, 4)}, {"Branch":(2,3), "Twine":(2,3)}) ,None),
    ( "Scavange", (20, 0, 0), ({"Berry":(1,2)}, {"Cactus":2}, {"Wheat":2}, {"Fruit":2}), None),
    ( "Hunt", (30, 0, 0), (("Encounter",)*4), None),
    (("Explore (1/4)", (0, 6, 0), ("Explore 1"), None),
    ("Explore (2/4)", (0, 6, 0), ("Explore 2"), ("currentSquare", "isDiscovered"), (1,)),
    ("Explore (3/4)", (0, 6, 0), ("Explore 3"), ("currentSquare", "isDiscovered"), (2,)),
    ("Explore (4/4)", (0, 6, 0), ("Explore 4"), ("currentSquare", "isDiscovered"), (3,)))
    
]

new = []

for x in actions4all:
    if type(x[0]) == tuple:
        for y in range(4):
            new.append((action(*z) for z in x))
    else:
        for y in x[2]:
            new.append(action(*(x[:2]+(y,)+x[3:])))        
        
m, d, g, f = [new[x::4] for x in range(4)]

while True:
    exec(raw_input())
        