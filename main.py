#libraries
import pygame

#init pygame
pygame.init()

#constants
screen_width, screen_height = 1280, 720
scale = 2 

#ticks
FPS = 60
clock = pygame.time.Clock()

#screen_properties
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('test')

#classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.direction = 'L'
        self.image = pygame.image.load('Assets/Images/Player/Player_standing.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*scale, self.image.get_height()*scale))
        self.player_index = 0.0
        self.rect = self.image.get_rect(center = (screen_width/2, screen_height/2))
        self.width = self.image.get_width()*0.4
        self.height = self.image.get_height()*0.4

    def walk(self, player_walk):
        self.player_index += 0.15
        if self.player_index >= 2:
            self.player_index = 0
        self.image = player_walk[int(self.player_index)]

    def animation(self):
        dowalk = 0
        keys = pygame.key.get_pressed()
        
        if self.direction == 'L':
            player_stand = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/Player/Player_standing.png').convert_alpha(), (self.width * scale, self.height * scale)), True, False)
            player_walk1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/Player/Player_walk_1.png').convert_alpha(), (self.width * scale, self.height * scale)), True, False)
            player_walk2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/Player/Player_walk_2.png').convert_alpha(), (self.width * scale, self.height * scale)), True, False)
            player_walk = [player_walk1, player_walk2]
            self.image = player_stand
            
        else:
            player_stand = pygame.transform.scale(pygame.image.load('Assets/Images/Player/Player_standing.png').convert_alpha(), (self.width * scale, self.height * scale))
            player_walk1 = pygame.transform.scale(pygame.image.load('Assets/Images/Player/Player_walk_1.png').convert_alpha(), (self.width * scale, self.height * scale))
            player_walk2 = pygame.transform.scale(pygame.image.load('Assets/Images/Player/Player_walk_2.png').convert_alpha(), (self.width * scale, self.height * scale))
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
        self.image = pygame.image.load('Assets/Images/Floor.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_width*3,screen_height*3))
        self.rect = self.image.get_rect(center = (screen_width/2, screen_height/2))
        
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left < screen_width/2:
            self.rect.x += 4
        if keys[pygame.K_w] and self.rect.top < screen_height/2:
            self.rect.y += 4
        if keys[pygame.K_d] and self.rect.right > screen_width - screen_width/2:
            self.rect.x -= 4
        if keys[pygame.K_s] and self.rect.bottom > screen_height - screen_height/2:
            self.rect.y -= 4
            
    def update(self):
        self.movement()
        
        
class Object(pygame.sprite.Sprite):
    def __init__(self, design):
        super().__init__()
        self.image = pygame.image.load(design).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*scale, self.image.get_height()*scale))
        self.rect = self.image.get_rect(center = (800, 100))
        
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and floor.sprite.rect.left < screen_width/2:
            self.rect.x += 4
        if keys[pygame.K_w] and floor.sprite.rect.top < screen_height/2:
            self.rect.y += 4
        if keys[pygame.K_d] and floor.sprite.rect.right > screen_width - screen_width/2:
            self.rect.x -= 4
        if keys[pygame.K_s] and floor.sprite.rect.bottom > screen_height - screen_height/2:
            self.rect.y -= 4
            
    def update(self):
        self.movement()
        
#definition of objects
player = pygame.sprite.GroupSingle()
player.add(Player())

floor = pygame.sprite.GroupSingle()
floor.add(Background())

chair = pygame.sprite.GroupSingle()
chair.add(Object("Assets/Images/Object.png"))        


#functions
def main():
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        draw()
        pygame.display.update()

    pygame.quit()

#display
def draw():
    screen.fill((0, 0, 0))
    
    floor.draw(screen)
    floor.update()

    player.draw(screen)
    player.update()
    
    chair.draw(screen)
    chair.update()

#call main function
if __name__ == "__main__":
    main()