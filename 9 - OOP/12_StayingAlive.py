"""
Staying Alive
Improve your gaming program adding an 'isAlive' property if the lives count is greater than 0.
"""
class Player:
    def __init__(self, name):
        self.name = name
        self._lives = 5
        self._isAlive = self.lives > 0
    
    @property
    def lives(self):
        return self._lives
    
    @property
    def isAlive(self):
        return self._lives > 0

    def hit(self):
        #your code goes here
        self._lives -= 1
        if not self.isAlive:
            print("Game Over")
            
        

p = Player("Cyberpunk77")
print(p.lives)
p.hit()
print(p.lives)
p.hit()
print(p.lives)
p.hit()
print(p.lives)
p.hit()
print(p.lives)
p.hit()