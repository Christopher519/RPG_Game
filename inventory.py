# 2020/03/02
# Inventory assignment for CS30

# Adding the items to the inventory for the invetory
title = ["shotty ", "lightning "]
broken_items = []
lightning_items = []
inventory_items = ["sword", "shield", "amour"]
# The broken items inventory
broken_items.append(title[0] + inventory_items[0])
broken_items.append(title[0] + inventory_items[1])
broken_items.append(title[0] + inventory_items[2])
broken_items.append('Spare tool parts')
broken_items.append('super magic wand')
# the lightning Items inventory
lightning_items.append(title[1] + inventory_items[0])
lightning_items.append(title[1] + inventory_items[1])
lightning_items.append(title[1] + inventory_items[2])
broken_items.sort
# Checking the the inventory for the first time and viewing the items in it
Number_of_Items = len(broken_items)
print("there are " + str(Number_of_Items) + " items in your inventory,")
print(sorted(broken_items))
# Adding the lightning items to the accessable inventory
broken_items.insert(0, 'Magic Orb')
print(f"the {broken_items.pop()} transforms into a {broken_items[0]}")
print("You check your inventory")
for broken_item in broken_items:
    print(broken_item)
print("A surge of energy flows out of the orb and forms in the shape of a new"
      " inventory bag and takes the spare and forms them into new tools")
print("You then organize this new inventory")
lightning_items.reverse
print("Apon closer inspection, you realize the orb has turned into a useless"
      " stone and you throw it away and check your inventory again")
# Printing the complete Inventory
del(broken_items[0])
broken_items.remove('Spare tool parts')
for broken_item in broken_items:
    print(broken_item)
for lightning_item in lightning_items:
    print(lightning_item)
