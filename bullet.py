import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settigs, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settigs.bullet_width, ai_settigs.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settigs.bullet_color
        self.speed_factor = ai_settigs.bullet_speed_factor
