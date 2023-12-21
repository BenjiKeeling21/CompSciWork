import player as p
import enemy as e
import rooms as r

print(len(e.currentEnemies))
e.newEnemies(7)
print(len(e.currentEnemies))
e.currentEnemies[1].die()
print(len(e.currentEnemies))
