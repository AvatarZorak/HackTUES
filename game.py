import pygame
from sys import exit


allowmove = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.direction = 'L'
        self.image = pygame.image.load('Player\player_standingL.png').convert_alpha()
        self.player_index = 0
        self.rect = self.image.get_rect(center = (640, 360))

    def walk(self, player_walk):
        self.player_index += 0.15
        if self.player_index >= 2:
            self.player_index = 0
        self.image = player_walk[int(self.player_index)]

    def animation(self):
        dowalk = 0
        keys = pygame.key.get_pressed()
        
        if self.direction == 'L':
            player_stand = pygame.image.load('Player\player_standingL.png').convert_alpha()
            player_walk1 = pygame.image.load('Player\player_walk_1L.png').convert_alpha()
            player_walk2 = pygame.image.load('Player\player_walk_2L.png').convert_alpha()
            player_walk = [player_walk1, player_walk2]
            self.image = player_stand
        else:
            player_stand = pygame.image.load('Player\player_standingR.png').convert_alpha()
            player_walk1 = pygame.image.load('Player\player_walk_1R.png').convert_alpha()
            player_walk2 = pygame.image.load('Player\player_walk_2R.png').convert_alpha()
            player_walk = [player_walk1, player_walk2]
            self.image = player_stand
            
        if keys[pygame.K_a]:
            self.direction = 'L'
            dowalk = 1
        if keys[pygame.K_d]:
            self.direction = 'R'
            dowalk = 1
        if keys[pygame.K_w] or keys[pygame.K_s]:
            dowalk = 1
        
        if dowalk: self.walk(player_walk)
        
        
    def update(self):
        self.animation()
        
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('floor.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (640, 360))
        self.rect = self.image.get_rect(center = (640, 360))
        
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left < 0:
            self.rect.x += 4
        if keys[pygame.K_w] and self.rect.top < 0:
            self.rect.y += 4
        if keys[pygame.K_d] and self.rect.right > 1280:
            self.rect.x -= 4
        if keys[pygame.K_s] and self.rect.bottom > 720:
            self.rect.y -= 4

    def can_move(self):
        global allowmove
        if self.rect.left < 0 and self.rect.top < 0 and self.rect.right > 1280 and self.rect.bottom > 640:
            allowmove = 1
        else:
            allowmove = 0
            
    def update(self):
        self.movement()
        self.can_move()
        
class Object(pygame.sprite.Sprite):
    def __init__(self, design):
        super().__init__()
        self.image = pygame.image.load(design).convert_alpha()
        self.rect = self.image.get_rect(center = (640, 360))
        
    def movement(self):
        keys = pygame.key.get_pressed()
        if allowmove:
            if keys[pygame.K_a]:
                self.rect.x += 4
            if keys[pygame.K_w]:
                self.rect.y += 4
            if keys[pygame.K_d]:
                self.rect.x -= 4
            if keys[pygame.K_s]:
                self.rect.y -= 4
            
    def update(self):
        self.movement()
        
        
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Mission: Develop')
clock = pygame.time.Clock()

player = pygame.sprite.GroupSingle()
player.add(Player())

floor = pygame.sprite.GroupSingle()
floor.add(Background())

chair = pygame.sprite.GroupSingle()
chair.add(Object("object.png"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    floor.draw(screen)
    floor.update()

    player.draw(screen)
    player.update()
    
    chair.draw(screen)
    chair.update()

    pygame.display.update()
    clock.tick(60)