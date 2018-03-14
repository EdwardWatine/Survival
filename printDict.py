from collections import OrderedDict as OD

def odc(*args):
    return OD(args)
    
def recursiveStr(d, esj, ilvl=1, linestart="", *args):
    for x in d:
        args = list(args)
        typs = [val[0] for val in args]
        places = {val:[] for val in typs}
        for ind, val in enumerate(typs):
            places[val].append(ind)   
            
        for y in args:
            if isinstance(d[x], y[0]):
                if len(places[y[0]]) > 1:
                    y = args[places[y[0]][1]]
                    del args[places[y[0]][1]]
                y = list(y)
                if isinstance(y[1], (tuple, list)):
                    y[1] = "{}{}".format(y[1][0], str(y[1][1])*ilvl)
                if isinstance(y[2], (tuple, list)):
                    y[2] = "{}{}".format(y[2][0], str(y[2][1])*ilvl)
                if isinstance(y[3], (tuple, list)):
                    y[3] = "{}{}".format(y[3][0], str(y[3][1])*ilvl)
                if y[0] == dict:
                    d[x] = recursiveStr(d[x], y[1:], ilvl+1, "", *args)
                    break
                else:
                    d[x] = y[3].join(["{}{}{}".format(y[2], z, y[1]) 
                    for z in d[x]])
                    break
         #else:
         #    d[x] = esj[2].join(["{}{}{}".format(esj[1], z, esj[0]) 
         #           	for z in d[x]])
    return (esj[2]+esj[2].join(["{}{}: {}{}".format(esj[1], z, d[z], esj[0]) for z in d])).replace("\n", "\n{}".format(linestart))

e = ""
mydict = odc(
("Attack",(2, 4)), 
("elements", odc(("Natural", 100))), 
("Moves", odc(("Die", odc(("Damage", 10))), ("Morn", "Shine")))
)
b = recursiveStr(mydict, (e, e, "\n"), 1, "    ",
(tuple, e, e, " - "), 
(dict, e, ("\n","    "), e),
(dict, "%", ("\n", "    "), e))
"""
while True:
    exec(raw_input())
"""
