"""
Game Over
Complete the code for a video game to take the name and level from user input.
"""

class Game:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    def show_player_info(self):
        print("Name:" + self.name)
        print("Level:" + self.level)

player = Game(input("Insert username player: "), input("Insert level player: "))
player.show_player_info()