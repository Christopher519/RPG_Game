BEGIN Rpg:
    Begin Quest Menu
    END Quest Menu


        WHILE Health > 0:
        BEGIN movement
        IF Health < 0 :
         trigger died

    input: " Game Over you Died, Play Again?"
    IF input is "yes"
        BEGIN Menu
    if input is "no"
     END Rpg
   else input """please select "yes" or "no" """

Menu Code

BEGIN Menu:
    PRINT title
    INPUT "Select an option"
    options:
        1 : "start",  BEGIN movement
        2 : " Instructions" , BEGIN HelpMe
        3 :  "exit" , END Menu
        4: "map", BEGIN Map
   END options
END Menu

Movement Code:
BEGIN Movement :
    WHILE Health > 0:
        BEGIN Room situation

        INPUT "What will you do?"
        options:
        Go North : Move North  IF room is to the south
        Go South : Move south IF room is to the south
        Go East   : Move East  IF room is to the south
        Go West  : Move West IF room is to the south
        pickup        : BEGIN Get
        Talk         : BEGIN Talk
        Map         : BEGIN Map
        Use         : BEGIN Use
        Inventory    : BEGIN Inv
        END options
    IF Health < 0
    END WHILE
 END Movement

Map Code:
BEGIN MAP
    PRINT the visual representation of the map
END MAP

pickup Code:
BEGIN pickup
 INPUT the item you want to get
    IF item is in room:
        Add the item to your inventory
        Delete the item from room
    ELSE:
    PRINT "Item not in room"
END pickup


BEGIN Use:
    INPUT the item you want to use
    IF item is in inventory:
        use the item if it can be used

     ELSE:
        PRINT " Item is not in Inventory"

END Use

Inventory Code
BEGIN Inventory:
  INPUT "Would you like to use, view or throw away something or leave"
    IF access:
    INPUT the item you want to use
    IF item is in inventory:
        use the item if it can be used
     ELSE:
        PRINT " Item is not in Inventory"
    ELIF
    INPUT is view:
     PRINT the inventory
    ElIF throw away:
     INPUT What would you like to throw away
     IF item is in inventory:
      Throw away item
     ElIF
    INPUT is leave
      END Inventory
    ELSE
     PRINT "Choose either use, view, throw away, or leave"


Show Room situation:
BEGIN Room situation:
    PRINT Health
    PRINT the room you are in
    PRINT information about room

     IF enemy is in the room :
        BEGIN Battle

    ELSE:
    PRINT "You are under attack by a pack of wolves"
END Room situation

Battle code:
BEGIN Battle:
    PRINT "you are under attack by the wolves , what shall you do?"
    WHILE enemies Health > 0

    INPUT " Hit or Heal?"
    IF INPUT is hit:
        Make a random number (to find out if you hit or not)

            IF you get a number which allows you to hit
                 Make another random number which shall be your attack
                 IF number = 6
                  attack crits for 2x damage
                  Remove your attack from enemy's health
                PRINT " You did (attack) number of damage to every wolf"
            ELSE:
                PRINT "You Missed"

      ELIF INPUT is Heal:
        generate a number that can be multiplied by items which shall heal you
        Add Heal to your Health

      ELIF: Your Health < 0
        INPUT: " Game Over you Died, Play Again?"
            IF input is "yes"
        BEGIN Menu
        elif input is "no":
            END Battle

      ELSE:
         PRINT "Invalid input you must choose yes or no"

  Make a random number (to find out if the enemy hits or not
      IF you get a number which allows you to hit
        Make another random number which shall be the enemy's attack
          Remove the enemy's attack from your health
END Battle
