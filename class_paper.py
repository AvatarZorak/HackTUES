import pygame
from constants import screen_width, screen_height
from class_player import Player, player
from class_background import Background, floor

class Paper(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.update()
        self.image = pygame.transform.scale(pygame.image.load("assets/images/papers/paper.png"), (50, 50))
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and floor.sprite.rect.left < screen_width/2: 
            self.rect.x += 4
        if key[pygame.K_w] and floor.sprite.rect.top < screen_height/2:
            self.rect.y +=4
        if key[pygame.K_d] and floor.sprite.rect.right > screen_width - screen_width/2:
            self.rect.x -= 4
        if key[pygame.K_s] and floor.sprite.rect.bottom > screen_height - screen_height/2:
            self.rect.y -= 4

    def update(self):
        global col
        self.movement()
        
        if col:
            o.dontmove(self)

    def check_col(self):
        col = pygame.sprite.collide_rect(self, player.sprite)
        return col