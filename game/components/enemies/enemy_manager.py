import pygame
from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.enemy_limit = 3  
    
    #
    def check_collisions(self, bullets):
        enemies_to_remove = []
        bullets_to_remove = []  

        for enemy in self.enemies:
            for bullet in bullets:
                if bullet.owner == 'player' and bullet.rect.colliderect(enemy.rect):
                    enemies_to_remove.append(enemy)
                    bullets_to_remove.append(bullet)  
                    break
    #
        for enemy in enemies_to_remove:
            self.enemies.remove(enemy)

        for bullet in bullets_to_remove:
            bullets.remove(bullet) 

    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)
        #    
        self.check_collisions(game.player.player_bullets)
        #

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    #
    def add_enemy(self):
        while len(self.enemies) < self.enemy_limit:
            enemy = Enemy()
            self.enemies.append(enemy)
    #