# CS30
# date modified: 03/17/2020
# Characters + Inventory and locations for RPG game

# Dictionary that states the players and a nested dictonary of their items
players = {"Swordsman": {"Shortsword":
                         {"description": "A small iron blade",
                          "damage": 100, "protection": 5},
                         "Sheild":
                         {"description": "Protects from blows",
                          "damage": 10, "protection": 50},
                         "Chainmail Armour":
                         {"description":
                          "Armour for the swordsman",
                          "damage": 0, "protection": 100}},
                        "Marksman": {"Bow":
                         {"description": "A long range projectile",
                          "damage": 10, "protection": 0},
                        "Arrows":
                         {"description": "ammo for the bow",
                          "damage": 50, "protection": 0},
                        "Quiver":
                         {"description":
                         "Quiver of arrows",
                         "damage": 0, "protection": 0}},
                        "Tank": {"Godly armour":
                         {"description":
                          "protection against almost all attacks",
                          "damage": 0, "protection": 100}}
           }
# A dictionary of all the locations in the game
map_locations = ['Mountains', 'River', 'The Plains']

for player in players:
    for item in players[player]:
        description = players[player][item]["description"]
        damage = players[player][item]["damage"]
        protection = players[player][item]["protection"]
        print(f"{player}'s {item} - {description}")
        print(f"damage: {damage}")
        print(f"protection: {protection}")
        print("\n")
print("Options of where to go:")
for map in map_locations:
    print(map)
