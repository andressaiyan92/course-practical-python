"""
Preservation
Complete the game program so that it outputs 'Game Over' in case the lives equal to 0.
Data Hiding
We are working on a game. Our Player class has name and private _lives attributes.
The hit() method should decrease the lives of the player by 1. In case the lives equal to 0, it should output "Game Over".
Complete the hit() method to make the program work as expected.

"""
class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        #your code goes here
        self._lives -= 1
        if self._lives == 0:
            print("Game Over")
        

p = Player("Cyberpunk77", 4)
p.hit()
p.hit()
p.hit()
p.hit()
