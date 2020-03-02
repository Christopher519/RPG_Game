title = ["shotty ", "lightning "]
inventory = []
inventory_part2 = []
inventory_items = ["sword", "shield", "amour"]
inventory.append(title[0] + inventory_items[0])
inventory.append(title[0] + inventory_items[1])
inventory.append(title[0] + inventory_items[2])
inventory.append('Spare tool parts')
inventory.append('super magic wand')
inventory_part2.append(title[1] + inventory_items[0])
inventory_part2.append(title[1] + inventory_items[1])
inventory_part2.append(title[1] + inventory_items[2])
inventory.sort
Number_of_Items = len(inventory)
print("there are " + str(Number_of_Items) + " items in your inventory,")
print(sorted(inventory))

inventory.insert(0, 'Magic Orb')
print("the " + str(inventory.pop()) + " transforms into a " + inventory[0])
print("You check your inventory")
print(inventory)
print("A surge of energy flows out of the orb and forms in the shape of a new"
      " inventory bag and takes the spare and forms them into new tools")
print("You then organize this new inventory")
inventory_part2.reverse
print("Apon closer inspection, you realize the orb has turned into a useless"
      " stone and you throw it away and check your inventory again")

del(inventory[0])

inventory.remove('Spare tool parts')
print(inventory)
print(inventory_part2)
