#libraries
from turtle import width
import pygame
from menu import Button, menu
from sys import exit
import datetime
import random

#init pygame
pygame.init()

#constants
screen_width, screen_height = 1280, 720
scale = 0.3
background_scale = 3.5
object_scale = 1.5

#global variables
col = False
try_move = []

#ticks
FPS = 60
clock = pygame.time.Clock()

#screen_properties
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Learn To Space')

#display icon
icon = pygame.image.load("assets/images/icon.png")
pygame.display.set_icon(icon)

#audio
pygame.mixer.music.load("assets/audio/soundtrack-v4.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)


#classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.direction = 'L'
        self.image = pygame.image.load('Assets/Images/player/sprite.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*scale, self.image.get_height()*scale))
        self.player_index = 0.0
        self.rect = self.image.get_rect(center = (screen_width/2, screen_height/2))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def walk(self, player_walk):
        self.player_index += 0.3
        if self.player_index >= 8:
            self.player_index = 0
        self.image = player_walk[int(self.player_index)]

    def animation(self):
        dowalk = 0
        keys = pygame.key.get_pressed()
        
        if self.direction == 'L':
            player_stand = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite.png').convert_alpha(), (self.width , self.height )), True, False)
            player_walk1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_0.png').convert_alpha(), (self.width , self.height )), True, False)
            player_walk2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_1.png').convert_alpha(), (self.width , self.height )), True, False)
            player_walk3 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_2.png').convert_alpha(), (self.width , self.height )), True, False)
            player_walk4 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_3.png').convert_alpha(), (self.width , self.height )), True, False)
            player_walk5 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_4.png').convert_alpha(), (self.width , self.height )), True, False)
            player_walk6 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_5.png').convert_alpha(), (self.width , self.height )), True, False)
            player_walk7 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_6.png').convert_alpha(), (self.width , self.height )), True, False)
            player_walk8 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_7.png').convert_alpha(), (self.width , self.height )), True, False)
            player_walk = [player_walk1, player_walk2, player_walk3, player_walk4, player_walk5, player_walk6, player_walk7, player_walk8]
            self.image = player_stand
            
        else:
            player_stand = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite.png').convert_alpha(), (self.width , self.height ))
            player_walk1 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_0.png').convert_alpha(), (self.width , self.height ))
            player_walk2 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_1.png').convert_alpha(), (self.width , self.height ))
            player_walk3 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_2.png').convert_alpha(), (self.width , self.height ))
            player_walk4 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_3.png').convert_alpha(), (self.width , self.height ))
            player_walk5 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_4.png').convert_alpha(), (self.width , self.height ))
            player_walk6 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_5.png').convert_alpha(), (self.width , self.height ))
            player_walk7 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_6.png').convert_alpha(), (self.width , self.height ))
            player_walk8 = pygame.transform.scale(pygame.image.load('Assets/Images/player/sprite_7.png').convert_alpha(), (self.width , self.height ))
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
            dontmove(self)

    def check_col(self):
        col = pygame.sprite.collide_rect(self, player.sprite)
        return col

paper_positions = [[0, 0], [100, 100], [200, 200], [500, 600], [372, 536], [1123, -888], [100, -500], [-100, 860], [1300, 860], [1700, 860]]

#definition of objects
player = pygame.sprite.GroupSingle()
player.add(Player())

floor = pygame.sprite.GroupSingle()
floor.add(Background())

paper1 = pygame.sprite.GroupSingle()
coordinates = random.randint(0, 9)
paper1.add(Paper(paper_positions[coordinates][0], paper_positions[coordinates][1]))
paper_positions.pop(coordinates)

paper2 = pygame.sprite.GroupSingle()
coordinates = random.randint(0, 8)
paper2.add(Paper(paper_positions[coordinates][0], paper_positions[coordinates][1]))
paper_positions.pop(coordinates)

paper3 = pygame.sprite.GroupSingle()
coordinates = random.randint(0, 7)
paper3.add(Paper(paper_positions[coordinates][0], paper_positions[coordinates][1]))
paper_positions.pop(coordinates)

desk = pygame.sprite.GroupSingle()
desk.add(Object("Assets/Images/objects/desk.png", 700, -240, 80, 110)) 

desk2 = pygame.sprite.GroupSingle()
desk2.add(Object("Assets/Images/objects/desk_variant2.png", 1000, -240, 80, 110))

desk3 = pygame.sprite.GroupSingle()
desk3.add(Object("Assets/Images/objects/desk_task2.png", 1300, -240, 80, 110))

desk4 = pygame.sprite.GroupSingle()
desk4.add(Object("Assets/Images/objects/desk_variant2.png", 1350 ,230, 80, 110))

desk5 = pygame.sprite.GroupSingle()
desk5.add(Object("Assets/Images/objects/desk.png", 850 ,770, 80, 110))

chair = pygame.sprite.GroupSingle()
chair.add(Object("Assets/Images/objects/chair.png", 690 ,-225, 60, 40))

chair2 = pygame.sprite.GroupSingle()
chair2.add(Object("Assets/Images/objects/chair.png", 990 ,-225, 60, 40))

chair3 = pygame.sprite.GroupSingle()
chair3.add(Object("Assets/Images/objects/chair.png", 1290 ,-225, 60, 40))

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

shelf2 = pygame.sprite.GroupSingle()
shelf2.add(Object("Assets/Images/objects/shelf_variant2.png", 500 ,200, 90, 300))

shelf3 = pygame.sprite.GroupSingle()
shelf3.add(Object("Assets/Images/objects/shelf_variant2.png", 1000 ,200, 90, 300))

shelf4 = pygame.sprite.GroupSingle()
shelf4.add(Object("Assets/Images/objects/shelf_task3.png", 550 ,750, 100, 250))

shelf5 = pygame.sprite.GroupSingle()
shelf5.add(Object("Assets/Images/objects/shelf.png", 1750 ,-220, 100, 250))

pot = pygame.sprite.GroupSingle()
pot.add(Object("Assets/Images/objects/emptypot.png", 2100 ,1030, 20, 40))

pot2 = pygame.sprite.GroupSingle()
pot2.add(Object("Assets/Images/objects/emptypot.png", 2100 ,-230, 20, 40))

table = pygame.sprite.GroupSingle()
table.add(Object("Assets/Images/objects/table.png", 2050 ,230, 80, 80))

table2 = pygame.sprite.GroupSingle()
table2.add(Object("Assets/Images/objects/table.png", 2050 ,430, 80, 80))

table3 = pygame.sprite.GroupSingle()
table3.add(Object("Assets/Images/objects/table_variant2.png", 2050 ,630, 80, 80))

box = pygame.sprite.GroupSingle()
box.add(Object("Assets/Images/objects/box.png", 1390 ,-430, 80, 80))

box2 = pygame.sprite.GroupSingle()
box2.add(Object("Assets/Images/objects/box.png", 1290 ,-470, 100, 100))

box3 = pygame.sprite.GroupSingle()
box3.add(Object("Assets/Images/objects/box.png", 1250 ,-400, 40, 40))

box4 = pygame.sprite.GroupSingle()
box4.add(Object("Assets/Images/objects/box.png", 0 ,1000, 80, 80))

telescope = pygame.sprite.GroupSingle()
telescope.add(Object("Assets/Images/objects/Telescope.png", 150, 990, 75, 45))

list = [paper1, paper2, paper3]
counter = 0
is_quest_1_screen = False
is_quest_2_screen = False
is_quest_2_screen_completed = False
starting_point = None

sentence = []
books = []

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
    reversemove(desk4.sprite)
    reversemove(chair3.sprite)
    reversemove(wall_left2.sprite)
    reversemove(wall_right3.sprite)
    reversemove(shelf2.sprite)
    reversemove(shelf3.sprite)
    reversemove(shelf4.sprite)
    reversemove(desk5.sprite)
    reversemove(shelf5.sprite)
    reversemove(pot.sprite)
    reversemove(pot2.sprite)
    reversemove(table.sprite)
    reversemove(table2.sprite)
    reversemove(table3.sprite)
    reversemove(box.sprite)
    reversemove(box2.sprite)
    reversemove(box3.sprite)
    reversemove(box4.sprite)
    reversemove(telescope.sprite)
    
    reversemove(paper1.sprite)
    reversemove(paper2.sprite)
    reversemove(paper3.sprite)

def is_open():
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_ESCAPE]:
        return False
    return True

#display
def draw_game():
    screen.fill((0, 0, 0))
    
    floor.draw(screen)

    key = pygame.key.get_pressed()

    global counter

    if paper1.sprite.check_col() and key[pygame.K_e] and paper1 in list:
        list.remove(paper1)
        counter += 1

    if paper2.sprite.check_col() and key[pygame.K_e] and paper2 in list:
        list.remove(paper2)
        counter += 1

    if paper3.sprite.check_col() and key[pygame.K_e] and paper3 in list:
        list.remove(paper3)
        counter += 1


    for i in list:
        i.draw(screen)    

    player.draw(screen)
    wall_left2.draw(screen)
    wall_right2.draw(screen)
    wall_up.draw(screen)
    wall_right.draw(screen)
    shelf.draw(screen)
    wall_down.draw(screen)
    wall_down2.draw(screen)
    shelf2.draw(screen)
    shelf3.draw(screen)
    shelf4.draw(screen)
    wall_up2.draw(screen)
    wall_left.draw(screen)
    desk.draw(screen)
    chair.draw(screen)
    desk2.draw(screen)
    chair2.draw(screen)
    desk3.draw(screen)
    chair3.draw(screen)
    desk4.draw(screen)
    desk5.draw(screen)
    wall_right3.draw(screen)
    shelf5.draw(screen)
    pot.draw(screen)
    pot2.draw(screen)
    table.draw(screen)
    table2.draw(screen)
    table3.draw(screen)
    box2.draw(screen)
    box.draw(screen)
    box3.draw(screen)
    box4.draw(screen)
    telescope.draw(screen)
    
    for i in range(counter):
        image = pygame.image.load("assets/images/papers/paper.png")
        screen.blit(pygame.transform.scale(image, (50, 50)), (i * 50, 0))

    global is_quest_1_screen
    global is_quest_2_screen

    key_pressed = pygame.key.get_pressed()
    if len(list) == 0 and key_pressed[pygame.K_q]:
        is_quest_1_screen = True

    if is_quest_1_screen:
        is_quest_1_screen = is_open()
        screen.blit(pygame.transform.scale(pygame.image.load("assets/images/papers/custom_text.png"), (screen_width, screen_height)), (0, 0))

    if desk_col() == True:
        is_quest_2_screen = True
        
    if is_quest_2_screen == True:
        is_quest_2_screen = is_open()
        screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/quest_2.png"), (screen_width, screen_height)), (0, 0))


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                sentence.append(event.unicode)

        for i in range(18):
            if i < len(sentence):
                image = pygame.image.load("assets/images/point_typed.png")
                screen.blit(pygame.transform.scale(image, (35, 35)), ((i * 30) + 375, 550)) 
            else:    
                image = pygame.image.load("assets/images/point.png")
                screen.blit(pygame.transform.scale(image, (35, 35)), ((i * 30) + 375, 550))

        if len(sentence) >= 18:
            sentence_string = ''.join(sentence)
            if sentence_string == "explore the cosmos":
                if is_open():
                    screen.blit(pygame.transform.scale(pygame.image.load("assets/images/papers/custom_text2.png"), (screen_width-200, screen_height-200)), (100, 100))
            else:
                global starting_point

                if starting_point == None:
                    starting_point = datetime.datetime.now()
                
                current_point = datetime.datetime.now()
                if (current_point - starting_point).seconds < 5:
                    screen.blit(pygame.image.load("assets/images/backgrounds/error.png"), (550, 350))
                else:
                    starting_point = None
                    sentence.clear()

    if shelf_col():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and len(books) <= 9:
                books.append(event.unicode)

        for i in range(9):
            if i < len(books):
                image = pygame.image.load("assets/images/rect_clicked.png")
                screen.blit(pygame.transform.scale(image, (20, 30)), ((i * 30) + 500, 500)) 
            else:    
                image = pygame.image.load("assets/images/rect.png")
                screen.blit(pygame.transform.scale(image, (20, 30)), ((i * 30) + 500, 500))

        if len(books) >= 9:
            books_string = ''.join(books)
            if books_string == "123412458":
                if is_open():
                    screen.blit(pygame.transform.scale(pygame.image.load("assets/images/papers/custom_text3.png"), (screen_width-200, screen_height-200)), (100, 100))
            else:

                if starting_point == None:
                    starting_point = datetime.datetime.now()
                
                current_point = datetime.datetime.now()
                if (current_point - starting_point).seconds < 5:
                    for i in range(9):
                        image = pygame.image.load("assets/images/rect_wrong.png")
                        screen.blit(pygame.transform.scale(image, (20, 30)), ((i * 30) + 400, 600))
                else:
                    starting_point = None
                    books.clear()


    ########################################################################
    paper1.update()
    paper2.update()
    paper3.update()

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
    shelf2.update()
    shelf3.update()
    desk4.update()
    shelf4.update()
    desk5.update()
    shelf5.update()
    pot.update()
    pot2.update()
    table.update()
    table2.update()
    table3.update()
    box.update()
    box2.update()
    box3.update()
    telescope.update()
    box4.update()
    
    floor.update()

    #print(floor.sprite.rect.x, floor.sprite.rect.y)
    
def desk_col():
    key_pressed = pygame.key.get_pressed()
    deskcol = floor.sprite.rect.x < -2150 and floor.sprite.rect.x > -2350 and floor.sprite.rect.y == -408 and key_pressed[pygame.K_p]
    return deskcol

def shelf_col():
    shelfcol = floor.sprite.rect.x < -1300 and floor.sprite.rect.x > -1730 and floor.sprite.rect.y == -1412
    return shelfcol 

#call main function
if __name__ == "__main__":
    main()