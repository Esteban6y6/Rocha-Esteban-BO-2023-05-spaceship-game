import pygame

from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    SCREEN_HALF_HEIGHT = SCREEN_HEIGHT / 2
    SCREEN_HALF_WIDTH = SCREEN_WIDTH / 2

    def __init__(self, screen, message):
        self.reset_screen(screen)
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, False, "Black")
        self.rect = self.text.get_rect(center = (self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT))
        self.score = 0
        self.highest_score = 0
    #
    def draw_game_over_stats(self, screen):
        font = pygame.font.Font(FONT_STYLE, 30)
        score_text = font.render(f'Score: {self.score}', False, 'Black')
        highest_score_text = font.render(f'Highest Score: {self.highest_score}', False, 'Black')

        score_rect = score_text.get_rect(center=(self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT + 50))
        highest_score_rect = highest_score_text.get_rect(center=(self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT + 100))

        screen.blit(score_text, score_rect)
        screen.blit(highest_score_text, highest_score_rect)
    #
    def update(self, game):
        pygame.display.update()
        self.handle_events(game)

    def draw(self, screen):
        screen.blit(self.text, self.rect)
    
    def handle_events(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            if event.type == pygame.KEYDOWN:
                game.run()
    
    def reset_screen(self, screen):
        screen.fill('White')
    
    def update_message(self, message):
        self.text = self.font.render(message, False, 'Black')
        self.rect = self.text.get_rect(center = (self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT))

    def increase_score(self):
        self.score += 1
    #
    def update_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score

    def reset_score(self):
        self.score = 0

    def reset_death_count(self):
        self.death_count = 0
    #