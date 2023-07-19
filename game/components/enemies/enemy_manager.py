import pygame
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy2 import Enemy2
from game.components.enemies.enemy3 import Enemy3

class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def update(self):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 3:
            if not any(isinstance(enemy, Enemy) for enemy in self.enemies):
                enemy = Enemy()
                self.enemies.append(enemy)
            elif not any(isinstance(enemy, Enemy2) for enemy in self.enemies):
                enemy2 = Enemy2()
                self.enemies.append(enemy2)
            elif not any(isinstance(enemy, Enemy3) for enemy in self.enemies):
                enemy3 = Enemy3()
                self.enemies.append(enemy3)