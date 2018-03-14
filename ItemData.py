from ItemClasses import itemGroup, item, weapon

items = itemGroup(
	        weapon("Fist", None, None, None, 0, (1, 2), None),
         item("Stone", "Misc.", "weapon", None, None, None, 0, {"Damage":(2, 3)}),              
         item("Sharp Stone", "Misc.", "weapon", None, {"Stone":2}, (10, 0, 0), 0, {"Damage":3}),           
         item("Branch", "Crafting item", None, None, None, None, 0),
         item("Plants", "Crafting item", None, None, None, None, 0),
         item("Twine", "Crafting item", None, None, {"Plants":20}, (30, 0, 0), 0),
         item("Table", "Crafting item", None, None, {"Branch":7, "Twine":6}, (20, 0, 0), 0),                      
         item("Crude stone knife", "Misc.", "weapon", None, {"Branch":1, "Twine":2, "Sharp Stone":1}, (10, 0, 0), 1, {"Damage":(4,5)}, None, "crd stn kfe"),       
         item("Crafting Bench (I)", "Crafting structure", None, None, {"crd stn kfe":1, "Table":1}, (0, 0, 0), 1,  None, None, "cbI")
         
         
         )

while True:
    exec(raw_input())