#libraries
import pygame
from menu import Button, menu
from sys import exit

#init pygame
pygame.init()

#constants
screen_width, screen_height = 1280, 720
scale = 0.75
background_scale = 3.5
object_scale = 1.5

#global variables
col = False
try_move = []

#text properties
font_buttons = pygame.font.SysFont('Ariel', 35)
text = font_buttons.render("Play", True, (255, 255, 255))

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
        self.image = pygame.image.load('Assets/Images/player/sprite.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*scale, self.image.get_height()*scale))
        self.player_index = 0.0
        self.rect = self.image.get_rect(center = (screen_width/2, screen_height/2))
        self.width = self.image.get_width()*0.4
        self.height = self.image.get_height()*0.4

    def walk(self, player_walk):
        self.player_index += 0.3
        if self.player_index >= 8:
            self.player_index = 0
        self.image = player_walk[int(self.player_index)]

    def animation(self):
        dowalk = 0
        keys = pygame.key.get_pressed()
        
        if self.direction == 'L':
            player_stand = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite.png').convert_alpha(), (self.width * scale, self.height * scale)), True, False)
            player_walk1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_0.png').convert_alpha(), (self.width * scale, self.height * scale)), True, False)
            player_walk2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_1.png').convert_alpha(), (self.width * scale, self.height * scale)), True, False)
            player_walk3 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_2.png').convert_alpha(), (self.width * scale, self.height * scale)), True, False)
            player_walk4 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_3.png').convert_alpha(), (self.width * scale, self.height * scale)), True, False)
            player_walk5 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_4.png').convert_alpha(), (self.width * scale, self.height * scale)), True, False)
            player_walk6 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_5.png').convert_alpha(), (self.width * scale, self.height * scale)), True, False)
            player_walk7 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_6.png').convert_alpha(), (self.width * scale, self.height * scale)), True, False)
            player_walk8 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_7.png').convert_alpha(), (self.width * scale, self.height * scale)), True, False)
            player_walk = [player_walk1, player_walk2, player_walk3, player_walk4, player_walk5, player_walk6, player_walk7, player_walk8]
            self.image = player_stand
            
        else:
            player_stand = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite.png').convert_alpha(), (self.width * scale, self.height * scale))
            player_walk1 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_0.png').convert_alpha(), (self.width * scale, self.height * scale))
            player_walk2 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_1.png').convert_alpha(), (self.width * scale, self.height * scale))
            player_walk3 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_2.png').convert_alpha(), (self.width * scale, self.height * scale))
            player_walk4 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_3.png').convert_alpha(), (self.width * scale, self.height * scale))
            player_walk5 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_4.png').convert_alpha(), (self.width * scale, self.height * scale))
            player_walk6 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_5.png').convert_alpha(), (self.width * scale, self.height * scale))
            player_walk7 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_6.png').convert_alpha(), (self.width * scale, self.height * scale))
            player_walk8 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_7.png').convert_alpha(), (self.width * scale, self.height * scale))
            player_walk = [player_walk1, player_walk2, player_walk3, player_walk4, player_walk5, player_walk6, player_walk7, player_walk8]
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
        self.image = pygame.image.load('Assets/Images/backgrounds/Floor.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_width*background_scale, screen_height*background_scale))
        self.rect = self.image.get_rect(center = (screen_width/2, screen_height/2))
        
    def trymovement(self):
        global try_move
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left < screen_width/2:
            self.rect.x += 4
            try_move.append("+x")
        if keys[pygame.K_w] and self.rect.top < screen_height/2:
            self.rect.y += 4
            try_move.append("+y")
        if keys[pygame.K_d] and self.rect.right > screen_width - screen_width/2:
            self.rect.x -= 4
            try_move.append("-x")
        if keys[pygame.K_s] and self.rect.bottom > screen_height - screen_height/2:
            self.rect.y -= 4
            try_move.append("-y")
            
    def update(self):
        self.trymovement()
        
class Object(pygame.sprite.Sprite):
    def __init__(self, design, x, y, height, width): 
        super().__init__()
        self.x = x #x coordinate
        self.y = y
        self.height = height
        self.width = width
        self.image = pygame.image.load(design).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width*object_scale, self.height*object_scale))
        self.rect = self.image.get_rect(center = (self.x, self.y))
       
    def check_col(self):
        global col
        col = pygame.sprite.collide_rect(self, player.sprite)
       
    def trymovement(self):
        global try_move
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and floor.sprite.rect.left < screen_width/2:
            self.rect.x += 4
            try_move.append("+x")
        if keys[pygame.K_w] and floor.sprite.rect.top < screen_height/2:
            self.rect.y += 4
            try_move.append("+y")
        if keys[pygame.K_d] and floor.sprite.rect.right > screen_width - screen_width/2:
            self.rect.x -= 4
            try_move.append("-x")
        if keys[pygame.K_s] and floor.sprite.rect.bottom > screen_height - screen_height/2:
            self.rect.y -= 4
            try_move.append("-y")
        
    def update(self):
        global col
        global try_move
        try_move = []
        self.trymovement()
        self.check_col()
        if col:
            dontmove(self)
        col = False
        try_move = []

class Paper(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load("assets/images/papers/paper.png"), (40, 40))
        self.rect = self.image.get_rect(center = (screen_width/2 + 150, screen_height/2 - 200))
        


#definition of objects
player = pygame.sprite.GroupSingle()
player.add(Player())

floor = pygame.sprite.GroupSingle()
floor.add(Background())

paper = pygame.sprite.GroupSingle()
paper.add(Paper(450, -50))


desk = pygame.sprite.GroupSingle()
desk.add(Object("Assets/Images/objects/desk.png", 700, -240, 80, 110)) 

desk2 = pygame.sprite.GroupSingle()
desk2.add(Object("Assets/Images/objects/desk_variant2.png", 1000, -240, 80, 110))

desk3 = pygame.sprite.GroupSingle()
desk3.add(Object("Assets/Images/objects/desk.png", 1300, -240, 80, 110)) 

chair = pygame.sprite.GroupSingle()
chair.add(Object("Assets/Images/objects/Object.png", 690 ,-225, 60, 40))

chair2 = pygame.sprite.GroupSingle()
chair2.add(Object("Assets/Images/objects/Object.png", 990 ,-225, 60, 40))

chair3 = pygame.sprite.GroupSingle()
chair3.add(Object("Assets/Images/objects/Object.png", 1290 ,-225, 60, 40))

wall_down = pygame.sprite.GroupSingle()
wall_down.add(Object("Assets/Images/objects/wall_ud.png", 605, 1110, 60, 2100))

wall_down2 = pygame.sprite.GroupSingle()
wall_down2.add(Object("Assets/Images/objects/wall_ud.png", 880, 150, 60, 800))

wall_up = pygame.sprite.GroupSingle() 
wall_up.add(Object("Assets/Images/objects/wall_ud.png", 1350 ,-300, 60, 1150))

wall_up2 = pygame.sprite.GroupSingle()
wall_up2.add(Object("Assets/Images/objects/wall_ud.png", 650 , -610, 60, 2510))

wall_left = pygame.sprite.GroupSingle()
wall_left.add(Object("Assets/Images/objects/wall_lr.png", -205, 450, 1410, 60))

wall_left2 = pygame.sprite.GroupSingle()
wall_left2.add(Object("Assets/Images/objects/wall_lr.png", 305, 900, 310, 60))

wall_right = pygame.sprite.GroupSingle()
wall_right.add(Object("Assets/Images/objects/wall_lr.png", 1500, -500, 1200, 60))

wall_right2 = pygame.sprite.GroupSingle()
wall_right2.add(Object("Assets/Images/objects/wall_lr.png", 1500, -700, 600, 60))

wall_right3 = pygame.sprite.GroupSingle()
wall_right3.add(Object("Assets/Images/objects/wall_lr.png", 2200, 400, 1600, 60))

shelf = pygame.sprite.GroupSingle()
shelf.add(Object("Assets/Images/objects/shelf.png", 300 ,-300, 90, 300))   

#functions ###################################################################
def main():
    run = True
    main_menu = True

    while run:
        clock.tick(FPS)
        
        if main_menu:
            main_menu = menu()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())
            draw_game()
            pygame.display.update()

    pygame.quit()

def reversemove(sprite): #rollback if collide
    for i in try_move:
            if i == "+x": sprite.rect.x -= 4
            elif i == "+y": sprite.rect.y -= 4
            elif i == "-x": sprite.rect.x += 4
            elif i == "-y": sprite.rect.y += 4

def dontmove(self): #initiate rollback #####################################################
    reversemove(desk.sprite)
    reversemove(chair.sprite)
    reversemove(shelf.sprite)
    reversemove(desk2.sprite)
    reversemove(chair2.sprite)
    reversemove(floor.sprite)
    reversemove(wall_up.sprite)
    reversemove(wall_down.sprite)
    reversemove(wall_left.sprite)
    reversemove(wall_right.sprite)
    reversemove(wall_up2.sprite)
    reversemove(wall_right2.sprite)
    reversemove(wall_down2.sprite)
    reversemove(desk3.sprite)
    reversemove(chair3.sprite)
    reversemove(wall_left2.sprite)
    reversemove(wall_right3.sprite)

#display
def draw_game():
    screen.fill((0, 0, 0))
    
    floor.draw(screen)
    player.draw(screen)
    wall_left2.draw(screen)
    wall_right2.draw(screen)
    wall_up.draw(screen)
    wall_right.draw(screen)
    shelf.draw(screen)
    wall_down.draw(screen)
    wall_down2.draw(screen)
    wall_up2.draw(screen)
    wall_left.draw(screen)
    desk.draw(screen)
    chair.draw(screen)

    paper.draw(screen)

    desk2.draw(screen)
    chair2.draw(screen)
    desk3.draw(screen)
    chair3.draw(screen)
    wall_right3.draw(screen)
    
    ########################################################################
    paper.update()

    player.update()
    wall_right2.update()
    wall_up.update()
    wall_down.update()
    wall_left.update()
    wall_right.update()
    wall_up2.update()
    desk.update()
    chair.update()
    shelf.update()
    desk2.update()
    chair2.update()
    wall_down2.update()
    desk3.update()
    chair3.update()
    wall_left2.update()
    wall_right3.update()
    
    floor.update()

#call main function
if __name__ == "__main__":
    main()