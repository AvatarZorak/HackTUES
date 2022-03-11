#libraries
import pygame

#
pygame.init()

#constants
screen_width, screen_height = 1000, 600

FPS = 60
clock = pygame.time.Clock()

#screen_properties
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('test')

#global variables
allowmove = 0

#classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.direction = 'L'
        self.image = pygame.image.load('Player\player_standingL.png').convert_alpha()
        self.player_index = 0
        self.rect = self.image.get_rect(center = (500, 300))

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
        self.rect = self.image.get_rect(center = (500, 300))
        
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left < 0:
            self.rect.x += 4
        if keys[pygame.K_w] and self.rect.top < 0:
            self.rect.y += 4
        if keys[pygame.K_d] and self.rect.right > screen_width:
            self.rect.x -= 4
        if keys[pygame.K_s] and self.rect.bottom > screen_height:
            self.rect.y -= 4

    def can_move(self):
        global allowmove
        if self.rect.left < 0 and self.rect.top < 0 and self.rect.right > screen_width and self.rect.bottom > screen_height:
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
        self.rect = self.image.get_rect(center = (600, 300))
        
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
        
#definition of objects
player = pygame.sprite.GroupSingle()
player.add(Player())

floor = pygame.sprite.GroupSingle()
floor.add(Background())

chair = pygame.sprite.GroupSingle()
chair.add(Object("object.png"))        


#functions
def main():

    run = True

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        draw()

        pygame.display.update()
        

    pygame.quit()

def draw():

    floor.draw(screen)
    floor.update()

    player.draw(screen)
    player.update()
    
    chair.draw(screen)
    chair.update()

#
if __name__ == "__main__":
    main()