from IntoTheVirbox.worldgen import WorldGenerator
from IntoTheVirbox.models.player import Player
import os

rooms = WorldGenerator(seed="virbox").genRooms()
player =  Player(rooms[0])

while True:
    troll = input("\nVim, or Emacs? (Determines Keybindings)> ")
    if troll.lower() == "vim":
        os.system("clear")
        break
    if troll.lower() == "emacs":
        os.system("clear")
        print("\nWrong answer, You die instantly")
        print("\nGame Over\n")
        exit()
    else:
        os.system("clear")
print(f"\nVim Bindings are used for movement")
print(f"\nYou wake up inside a box, your coordinates are {player.room.coordinates}\n")
while True:
    movement = input("\nWhat direction do you go?> ")
    if movement == "h":
        os.system("clear")
        player.moveLeft()

    if movement == "j":
        os.system("clear")
        print(player.moveDown())

    if movement == "k":
        os.system("clear")
        print(player.moveUp())

    if movement == "l":
        os.system("clear")
        print(player.moveRight())

    print(f"Your coordinates: {player.room.coordinates}")


