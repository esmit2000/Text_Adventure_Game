##############################################################
## Eric's Closet of DOOM                                    ##
##############################################################

from time import sleep
import random
from adven import *

game = Game("Closet of Doom")
#Opening Dialogue
print "Welcome to your doom!"
sleep(1)
print "..."
sleep(1)
print """I can see that you are blind to your eternal suffering, a pity. I will
do my best to describe your doom to you"""
sleep(1)
print """You are locked in a room with no visible doors or windows (though
nothing is visible to you anyway)."""
sleep(1)
print """If you choose to stay, you will starve to death. If you choose to
leave, However, I say good luck and good riddance."""
print """'You hear foot steps walking away and a door is shut and locked.
The footsteps continue walking until you can no longer hear them.'"""

#Locations
closet = game.new_location("Closet {n}","""You are in a dark closet with a
locked door in front of you. If you feel around you notice that there are some
random objects on the floor.""")
foyer = game.new_location("Foyer {n, e, w, s}","""You find yourself in a grand
foyer with doors leading in all directions.""")
nh = game.new_location("North Hallway {n,s}","""You are in a slim hallway with
exits to the north and south.""")
sh = game.new_location("South Hallway {s,n}","""You are in a slim hallway with
exits to the south and north.""")
eh = game.new_location("East Hallway {e,w}","""You are in a slim hallway with
exits to the east and west.""")
wh = game.new_location("West Hallway {w,e}","""You are in a slim hallway with
exits to the west and east.""")
d1 = game.new_location("Dead End {s}", """You are at the end of the North Hallway,
there appears to be something spooky about the single wooden chair that sits
against the wall.""")
exit = game.new_location("Strange Door {n, s}", """You are at the end of the South
Hallway and a locked door prevents you from moving onwards.""")
bd1 = game.new_location("Bedroom {east,down}", """You find yourself in an
elegant bedroom with a large bed and a desk.""")
kitchen = game.new_location("Kitchen {w}","""You go east from the East Hallway
to find yourself in a kitchen stocked with an assortment of ustensils and food""")
b1 = game.new_location("Basement {w}","""You go down the hidden staircase to
find yourself in a dark basement with a door to the north""" )
b2 = game.new_location("Basement West {w, e}","""Going west, you find youself in
a room almost identical to the first basement""")
dungeon = game.new_location("Dungeon {e}","""You find yourself in a evil
looking dungeon with shackels lining the walls.""")
#New Room for pudding monster

#Connections between rooms
game.new_connection("Doorway", closet, foyer, [NORTH], [SOUTH])
game.new_connection("Doorway", foyer, nh, [NORTH], [SOUTH])
game.new_connection("Doorway", foyer, sh, [SOUTH], [NORTH])
game.new_connection("Doorway", foyer, eh, [EAST], [WEST])
game.new_connection("Doorway", foyer, wh, [WEST], [EAST])
game.new_connection("Doorway", nh, d1, [NORTH], [SOUTH])
game.new_connection("Doorway", sh, exit, [SOUTH], [NORTH])
game.new_connection("Doorway", eh, kitchen, [EAST], [WEST])
game.new_connection("Doorway", wh, bd1, [WEST], [EAST])
game.new_connection("Staircase", bd1, b1, [DOWN], [UP])
game.new_connection("Doorway", bd1, closet, [NORTH])
game.new_connection("Doorway", b1, b2, [WEST, EAST])
game.new_connection("Doorway", b2, dungeon, [WEST, EAST])


#Objects
wrench = closet.new_object("wrench","A rusty and seemingly unstable wrench.")
stuffed_tortoise = closet.new_object("stuffed tortoise","""A Stuffed Toy
Tortoise that looks somehow sturdier than the wrench.""")
bone_saw = closet.new_object("bone saw", """An old and hefty bone saw that
looks as if it has been used in many surgeries.""" )

#NPC's
creepy_voice = Animal("Creepy Voice")
creepy_voice.set_location(closet)
creepy_voice.set_allowed_locations([closet])
game.add_actor(creepy_voice)
skeleton = Animal("Skeleton")
skeleton.set_location(dungeon)
skeleton.set_allowed_locations([dungeon])
game.add_actor(skeleton)
rice_pudding_monster = Animal("Rice Pudding Monster")
rice_pudding_monster.set_location(kitchen)
rice_pudding_monster.set_allowed_locations([kitchen])
game.add_actor(rice_pudding_monster)
mr_mayer = Animal("Mayer")
mr_mayer.set_location(bd1)
mr_mayer.set_allowed_locations([bd1])
game.add_actor(mr_mayer)

#Commands
def kill_creepy_voice(game, thing):
        if "battery tazer" in game.player.inventory:
            game.output("""The Creepy Voice can be heard snickering at you
but cannot be seen, do you ask it to come out of hiding or slash the air
randomly?""")
            player_choice = raw_input("Ask or Slash?")
            if player_choice == "ask":
                game.output("""Hearing your request the Voice came out of
hiding, only to bite your head off, darn.""")
                print "You have died"
                player.terminate()
                return
            if player_choice == "slash":
                game.output("""In a stroke of luck, you have knocked the
Creepy Voice out of the sky and killed it""")
                print "You have killed the Creepy Voice"
                magic_spoon = closet.new_object("magic spoon", """A golden spoon
that shines with a magial glow.""")
                print "The Creepy Voice has dropped a Magic Spoon."
                return

        if not "battery tazer" in game.player.inventory:
            game.output("""You fought valiantly but were ultimately defeated due to
your lacking of proper weapons.""")
            player.terminate()
            print "You have died"
            return

def kill_skeleton(game, thing):
        if "bone saw" in game.player.inventory:
            game.output("""The Skeleton has raised his shiled, do you raise
your shield in greeting or aim for its legs?""")
            player_choice = raw_input("Greet or Chop?")
            if player_choice == "greet":
                game.output("""The skeleton lowered its shield to wave to you,
do you take advantage of this opening or wave back?""")
                player_choice2 = raw_input("Wave or kill?")
                if player_choice2 == "wave":
                    game.output("""You have befriended the skeleton, as a token
of friendship he hands you the Battery Tazer and vanishes into thin air.""")
                    skeleton.terminate()
                    battery_tazer = dungeon.new_object("battery tazer","""An old D battery with a
button and paperclips attached to it, it looks very important""")
                    return
                if player_choice2 == "kill":
                    game.output("""The skeleton has dodge you attack and cleaved
in half.""")
                    print "You have died"
                    player.terminate()
                    return
            if player_choice == "chop":
                    game.output("""The skeleton has dodge you attack and cleaved
in half.""")
                    print "You have died"
                    player.terminate()
                    return

        if not "bone saw" in game.player.inventory:
            game.output("""You fought valiantly but were ultimately defeated due to
your lacking of proper weapons.""")
            player.terminate()
            print "You have died"
            return

def kill_rice_pudding_monster(game, thing):
        if "magic spoon" in game.player.inventory:
            game.output("""The Rice Pudding Monster is just sitting in the
middle of the kitchen, not fighting back. Do you take this opportunity to kill
the monster by thrusting the spoon into what you percieve to be the heart of
the beast, or do you eat the monster (you haven't eaten in a long time
after all).""")
            player_choice = raw_input("Eat or Stab")
            if player_choice == "eat":
                game.output("""Eating the Rice Pudding Monster has proved to be
to great a task for you, you made it halfway through when you died of food
poisoning, the pudding has been there a long time after all.""")
                print "You have died"
                player.terminate()
                return
            if player_choice == "stab":
                game.output("You have killed the Rice Pudding Moster!!")
                print "The Moster dropped a Mayer Slayer"
                mayer_slayer = kitchen.new_object("mayer slayer", """An
abnormally large sword with the words 'Slay the Mayer' engraved in the hilt.""")
                return

        if not "magic spoon" in game.player.inventory:
            game.output("""You fought valiantly but were ultimately defeated due to
your lacking of proper weapons.""")
            player.terminate()
            print "You have died"
            return

def kill_mr_mayer(game, thing):
        if "mayer slayer" in game.player.inventory:
            print "Mr. Mayer attacked, do you dodge or fight back?"
            player_choice = raw_input("Dodge or Attack?")
            if player_choice == "dodge":
                game.output ("""you have dodged ineffectively and were killed
by Mr.Mayer""")
                player.terminate()
                print "You have died"
                return
            if player_choice == "attack":
                game.output("""Your sudden attack has scared Mr. Mayer and
                caused him to cower in fear, dropping the salty key """)
                player_decision = raw_input("Take or Kill?")
                if player_decision == "take":
                    game.output("""Mr. Mayer took advantage of your genorosity
and stabbed you in the back (literally).""")
                    print "you have died"
                    player.terminate()
                    return
                if player_decision == "kill":
                    game.output("""You have slain Mr. Mayer, now take the keyand
                    gain your freedom!""")
                    salty_key = bd1.new_object("salty key", """A strangely
salty and slimy key taken out of the dead hands of Mayer""")
                    return

        if not "mayer slayer" in game.player.inventory:
            game.output("""You fought valiantly but were ultimately defeated due to
your lacking of proper weapons.""")
            player.terminate()
            print "You have died"
            return

def open_strange_door(game, thing):
        if "salty key" in game.player.inventory:
            game.output("""You have escaped the Closet of Doom!! You may now
go back to your boring life void of creepy voices and pudding
monsters. Thank you for playing""")
            player.terminate()
            return

        if not "salty key" in game.player.inventory:
            game.output("""You do not have the necessary key to unlock this
door""")
            return

#outside.add_phrase("victory", victory)
creepy_voice.add_phrase("fight creepy voice", kill_creepy_voice)
skeleton.add_phrase("fight skeleton", kill_skeleton)
rice_pudding_monster.add_phrase("fight rice pudding monster", kill_rice_pudding_monster)
mr_mayer.add_phrase("fight mayer", kill_mr_mayer)
exit.add_phrase("open strange door", open_strange_door)

player = game.new_player(closet)
foyer.make_requirement(stuffed_tortoise)

game.run()
