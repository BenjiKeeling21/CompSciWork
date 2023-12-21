import random

class Enemy:

    def __init__(self):
        self.type = random.choice(["goblin", "orc", "troll"])
        if self.type == "goblin":
            self.health = random.randint(7, 15)
        if self.type == "orc":
            self.health = random.randint(13, 20)
        if self.type == "troll":
            self.health = random.randint(25, 50)

    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()
    
    def die(self):
        currentEnemies.remove(self)

currentEnemies = []

def newEnemies(num):
    global currentEnemies
    for i in range(num):
        currentEnemies.append(Enemy())

