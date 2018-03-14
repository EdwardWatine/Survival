from PrintDict import recursiveStr
from collections import OrderedDict as OD
def format1DDict(d, join=" x"):
    return "\n    "+"\n    ".join([("{}"+join+"{}").format(x, d[x]) for x in d]) if d else "None"


def weapon(name, struct, craft, ctime, tier, damage, elements={"Natural":100}, moves=None, funcArgs=None):
    props = OD([x for x in (("Damage", damage), ("Elements", elements), ("Moves", moves)) if x[1]])
    return item(name, "Weapon", "weapon", struct, craft, ctime, tier, props, funcArgs)
                
class item:
    
    def __init__(self, name, _type, slot, struct, craft, ctime, tier, props=None, funcArgs=None, referrable=None):
        self.name = name
        self._type = _type
        self.slot = slot
        self.struct = struct
        self.craft = craft
        self.ctime = ctime
        self.tier = tier
        self.props = props
        self.refer = referrable if referrable else name
        e = ""
        self.funcArgs = ((e, e, "\n"), 1, "    ",
(tuple, e, e, " - "), 
(dict, e, ("\n","    "), e),
(dict, "%", ("\n", "    "), e)) if not funcArgs else funcArgs
    
    def tree(self):
        if self.craft:
            return {self.name:[x.tree() for x in self.craft]}
        else:
            return self.name
    
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
            x.info = ("""{} ({})
Tier {}
Equippable Slot: {}

Crafting Structure: {}
Crafting"""+("" if not x.ctime else ' ({} mins {} hours {} days)'.format(*x.ctime)) +''': {}

Stats: {}
''').format(
    x.name, x._type, x.tier, x.slot, x.struct,
    format1DDict(x.craft),
    recursiveStr(x.props, *x.funcArgs)
    )
            self.contents.append(x)

    def __len__(self):
        return len(self.contents)

    def __getitem__(self, key):
        for x in self.contents:
            if x.refer==key or x.name==key:
                return x
        raise KeyError

    def __iter__(self):
        return iter(self.contents)
        
import ItemData
