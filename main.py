#libraries
from re import S
import pygame
from sys import exit

#init pygame
pygame.init()

#constants
screen_width, screen_height = 1280, 720
scale = 2
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
        self.x = x
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

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image_name):
        super().__init__()
        self.x = x
        self.y = y
        self.image_name = image_name
        self.image = pygame.image.load(f"{self.image_name}.png")

    def change_button(self):
        mouse = pygame.mouse.get_pos()
        if self.x <= mouse[0] <= self.x + self.image.get_width() and self.y <= mouse[1] <= self.y  + self.image.get_height():
            self.image = pygame.image.load(f"{self.image_name}_pressed.png")
            screen.blit(self.image, (self.x, self.y))
        else:
            self.image = pygame.image.load(f"{self.image_name}.png")
            screen.blit(self.image, (self.x, self.y))
        
    def check_clicked(self):
        mouse = pygame.mouse.get_pos()
        if self.x <= mouse[0] <= self.x + self.image.get_width() and self.y <= mouse[1] <= self.y  + self.image.get_height():
            return True

#definition of objects
player = pygame.sprite.GroupSingle()
player.add(Player())

floor = pygame.sprite.GroupSingle()
floor.add(Background())

desk = pygame.sprite.GroupSingle()
desk.add(Object("Assets/Images/desk.png", 490, -50, 80, 110)) 

chair = pygame.sprite.GroupSingle()
chair.add(Object("Assets/Images/Object.png", 840 ,-55, 60, 40))   

wall_up = pygame.sprite.GroupSingle()
wall_up.add(Object("Assets/Images/wall_up.png", 500 ,-300, 60, 1000))

wall_down = pygame.sprite.GroupSingle()
wall_down.add(Object("Assets/Images/wall_down.png", 600 ,600, 60, 1000))

shkaf = pygame.sprite.GroupSingle()
shkaf.add(Object("Assets/Images/shkaf.png", 340 ,-245, 90, 300))   

             

play_button = Button(screen_width/2 - 50, screen_height/2, "assets/images/play_button")
quit_button = Button(screen_width/2 - 50, screen_height/2+100, "assets/images/quit_button")

#functions
def main():
    run = True
    main_menu = True

    while run:
        clock.tick(FPS)
        
        if main_menu == True:
            mouse = pygame.mouse.get_pos()

            screen.blit(pygame.transform.scale(pygame.image.load("assets/images/menu_background.png"), (screen_width, screen_height)), (0, 0))

            play_button.change_button()
            quit_button.change_button()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.check_clicked():
                        print("joe mama")
                        main_menu = False

                    if quit_button.check_clicked():
                        run = False
            pygame.display.update()
        elif main_menu == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())
            draw_game()
            pygame.display.update()



    pygame.quit()

def reversemove(sprite):
    for i in try_move:
            if i == "+x": sprite.rect.x -= 4
            elif i == "+y": sprite.rect.y -= 4
            elif i == "-x": sprite.rect.x += 4
            elif i == "-y": sprite.rect.y += 4

def dontmove(self):
    reversemove(desk.sprite)
    reversemove(chair.sprite)
    reversemove(shkaf.sprite)
    reversemove(floor.sprite)
    reversemove(wall_up.sprite)
    reversemove(wall_down.sprite)

#display
def draw_game():
    screen.fill((0, 0, 0))
    
    floor.draw(screen)
    player.draw(screen)
    wall_up.draw(screen)
    wall_down.draw(screen)
    desk.draw(screen)
    chair.draw(screen)
    shkaf.draw(screen)
    
    
    player.update()
    wall_up.update()
    wall_down.update()
    desk.update()
    chair.update()
    shkaf.update()
    
    
    
    floor.update()

#call main function
if __name__ == "__main__":
    main()