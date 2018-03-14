from printDict import recursiveStr
from collections import OrderedDict as OD
def format1DDict(d, join=" x"):
    return "\n    "+"\n    ".join([("{}"+join+"{}").format(x, d[x]) for x in d]) if d else "None"


def weapon(name, struct, craft, tier, damage, elements, moves, funcArgs=False):
    props = OD([x for x in (("Damage", damage), ("Elements", elements), ("Moves", moves)) if x[1]])
    return item(name, "Weapon", "weapon", struct, craft, tier, props, funcArgs)
                
class item:
    
    def __init__(self, name, _type, slot, struct, craft, tier, props, funcArgs=None):
        self.name = name
        self._type = _type
        self.slot = slot
        self.struct = struct
        self.craft = craft
        self.tier = tier
        self.props = props
        e = ""
        
        self.funcArgs = ((e, e, "\n"), 1, "    ",
(tuple, e, e, " - "), 
(dict, e, ("\n","    "), e),
(dict, "%", ("\n", "    "), e)) if not funcArgs else funcArgs
        
        self.info = """{} ({})
Tier {}
Equippable Slot: {}

Crafting Structure: {}
Crafting: {}

Stats: {}
""".format(
    self.name, self._type, self.tier, self.slot, self.struct,
    format1DDict(self.craft),
    recursiveStr(self.props, *self.funcArgs)
    )

    def __str__(self):
        return self.name

class itemGroup:
    
    def __init__(self, *args):
        self.contents = []
        for x in args:
            if x.craft:
                x.craft = {self[y]:x.craft[y] for y in x.craft}
            if x.struct:
                x.struct = self[x.struct]
            self.contents.append(x)

    def __len__(self):
        return len(self.contents)

    def __getitem__(self, key):
        for x in self.contents:
            if x.name==key:
                return x
        raise KeyError

    def __iter__(self):
        return iter(self.contents)

    

    
items = itemGroup(weapon("Fist", None, None, 0, (1, 2), None, None),
         item("Stone", "Misc.", "weapon", None, None, 0, {"Damage":(2, 3)}),
         item("Sharp Stone", "Misc.", "weapon", None, {"Stone":2}, 0, {"Damage":3})


         )
