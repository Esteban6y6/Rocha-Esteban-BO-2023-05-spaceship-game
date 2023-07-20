import pygame
import random
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullets.bullet import Bullet


class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60
    Y_POS = 0
    X_POS_RANGE = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    MOVES = {0: 'left', 1: 'right'}
    INITIAL_SHOOTING_TIME = 1000
    FINAL_SHOOTING_TIME = 3000

    def __init__(self):
        self.enemy_type = random.choice([ENEMY_1, ENEMY_2, ENEMY_3])
        self.image = pygame.transform.scale(self.enemy_type, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect(midtop=(random.choice(self.X_POS_RANGE), self.Y_POS))
        self.direction = self.MOVES[random.randint(0, 1)]
        self.movement_count = 0
        self.moves_before_change = random.randint(20, 50)
        self.type = 'enemy'
        current_time = pygame.time.get_ticks()
        self.shooting_time = random.randint(current_time + self.INITIAL_SHOOTING_TIME, current_time + self.INITIAL_SHOOTING_TIME)

        if self.enemy_type == ENEMY_1:
            self.SPEED_ON_Y = 1
            self.SPEED_ON_X = 10
        elif self.enemy_type == ENEMY_2:
            self.SPEED_ON_Y = 2
            self.SPEED_ON_X = 12
        elif self.enemy_type == ENEMY_3:
            self.SPEED_ON_Y = 3
            self.SPEED_ON_X = 14

    def update(self, enemies, game):
        self.rect.y += self.SPEED_ON_Y
        self.shoot(game.bullet_manager)

        if self.direction == self.MOVES[0]:
            self.rect.x -= self.SPEED_ON_X
        elif self.direction == self.MOVES[1]:
            self.rect.x += self.SPEED_ON_X

        self.handle_direction()

        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_direction(self):
        self.movement_count += 1

        if (self.movement_count >= self.moves_before_change and self.direction == self.MOVES[1]) or self.rect.right >= SCREEN_WIDTH:
            self.direction = self.MOVES[0]
        elif self.movement_count >= self.moves_before_change and self.direction == self.MOVES[0] or self.rect.left <= 0:
            self.direction = self.MOVES[1]

        if self.movement_count >= self.moves_before_change:
            self.movement_count = 0

    def reset(self):
        self.enemy_type = random.choice([ENEMY_1, ENEMY_2, ENEMY_3])
        self.image = pygame.transform.scale(self.enemy_type, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect(midtop=(random.choice(self.X_POS_RANGE), self.Y_POS))
        self.direction = self.MOVES[random.randint(0, 1)]
        self.movement_count = 0
        self.moves_before_change = random.randint(20, 50)
    
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()

        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(self.INITIAL_SHOOTING_TIME, self.FINAL_SHOOTING_TIME)