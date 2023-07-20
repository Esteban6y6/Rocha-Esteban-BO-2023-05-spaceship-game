import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40 
    SPACESHIP_HEIGHT = 60 
    SPACESHIP_POS_X = SCREEN_WIDTH / 2 
    SPACESHIP_POS_Y = 500
    #
    SHOOT_DELAY = 500
    #

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect(midbottom = (self.SPACESHIP_POS_X, self.SPACESHIP_POS_Y))
        self.type = 'player'
        #
        self.player_bullets = []
        self.can_shoot = True
        self.last_shot_time = 0 
        #self.space_pressed = False
        #
    def update(self, user_input):

        if user_input[pygame.K_LEFT]:
            self.rect.x -= 10
            if self.rect.left < 0:
                self.rect.right = SCREEN_WIDTH
        elif user_input[pygame.K_RIGHT]:
            self.rect.x += 10
            if self.rect.right > SCREEN_WIDTH:
                self.rect.left = 0
        elif user_input[pygame.K_UP] and self.rect.top > 300:
            self.rect.y -= 10
        elif user_input[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10
        
        #self.space_pressed = user_input[pygame.K_SPACE]
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    #
    def shoot(self):
        current_time = pygame.time.get_ticks()

        if self.can_shoot and current_time - self.last_shot_time >= self.SHOOT_DELAY:
            bullet = Bullet(self)
            self.player_bullets.append(bullet)
            self.last_shot_time = current_time
            self.can_shoot = False

    def reset_shooting(self):
        current_time = pygame.time.get_ticks()

        if not self.can_shoot and current_time - self.last_shot_time >= self.SHOOT_DELAY:
            self.can_shoot = True

    def draw_bullets(self, screen):
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
            bullet.draw(screen)
    #