#libraries
import pygame
from menu import Button, menu
from sys import exit
import datetime
import random
import object_coordinates as oc

#init pygame
pygame.init()

#constants
screen_width, screen_height = 1280, 720
scale = 0.3
background_scale = 3.5
object_scale = 1.5

#global variables
level = 1
col = False
try_move = []
paper_complete, book_complete, computer_complete = False, False, False
R, Y, G = False, False, False
device_complete = False
volume_strength = 0.2
controls = True

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
pygame.mixer.music.set_volume(volume_strength)

key = None

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
        global try_move, controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left < screen_width/2:
            self.rect.x += 4
            try_move.append("+x")
            controls = False
        if keys[pygame.K_w] and self.rect.top < screen_height/2:
            self.rect.y += 4
            try_move.append("+y")
            controls = False
        if keys[pygame.K_d] and self.rect.right > screen_width - screen_width/2:
            self.rect.x -= 4
            try_move.append("-x")
            controls = False
        if keys[pygame.K_s] and self.rect.bottom > screen_height - screen_height/2:
            self.rect.y -= 4
            try_move.append("-y")
            controls = False

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
        self.rect = self.image.get_rect(center = (self.x - 10, self.y - 10))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        #self.outer_rect = pygame.Rect((self.x - 1, self.y - 1), (self.width + 2, self.height + 2))
        
       
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

paper_positions = [[0, 0], [100, 100], [200, 200], [500, 600], [372, 536], [1123, -488], [100, -500], [-100, 860], [1300, 860], [1700, 860]]

#definition of objects
#level 1
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
desk.add(Object("Assets/Images/objects/desk.png", oc.desk_x, oc.desk_y, 80, 110)) 

desk2 = pygame.sprite.GroupSingle()
desk2.add(Object("Assets/Images/objects/desk_variant2.png", oc.desk2_x, oc.desk2_y, 80, 110))

desk3 = pygame.sprite.GroupSingle()
desk3.add(Object("Assets/Images/objects/desk_task2.png", oc.desk3_x, oc.desk3_y, 80, 110))

desk4 = pygame.sprite.GroupSingle()
desk4.add(Object("Assets/Images/objects/desk_variant2.png", oc.desk4_x ,oc.desk4_y, 80, 110))

desk5 = pygame.sprite.GroupSingle()
desk5.add(Object("Assets/Images/objects/desk.png", oc.desk5_x ,oc.desk5_y, 80, 110))

chair = pygame.sprite.GroupSingle()
chair.add(Object("Assets/Images/objects/chair.png", oc.chair_x ,oc.chair_y, 60, 40))

chair2 = pygame.sprite.GroupSingle()
chair2.add(Object("Assets/Images/objects/chair.png", oc.chair2_x ,oc.chair2_y, 60, 40))

chair3 = pygame.sprite.GroupSingle()
chair3.add(Object("Assets/Images/objects/chair.png", oc.chair3_x ,oc.chair3_y, 60, 40))

wall_down = pygame.sprite.GroupSingle()
wall_down.add(Object("Assets/Images/objects/wall_ud.png", oc.wall_down_x, oc.wall_down_y, 60, 2100))

wall_down2 = pygame.sprite.GroupSingle()
wall_down2.add(Object("Assets/Images/objects/wall_ud.png", oc.wall_down2_x, oc.wall_down2_y, 60, 800))

wall_up = pygame.sprite.GroupSingle() 
wall_up.add(Object("Assets/Images/objects/wall_ud.png", oc.wall_up_x ,oc.wall_up_y, 60, 1150))

wall_up2 = pygame.sprite.GroupSingle()
wall_up2.add(Object("Assets/Images/objects/wall_ud.png", oc.wall_up2_x , oc.wall_up2_y, 60, 2510))

wall_left = pygame.sprite.GroupSingle()
wall_left.add(Object("Assets/Images/objects/wall_lr.png", oc.wall_left_x, oc.wall_left_y, 1410, 60))

wall_left2 = pygame.sprite.GroupSingle()
wall_left2.add(Object("Assets/Images/objects/wall_lr.png", oc.wall_left2_x, oc.wall_left2_y, 310, 60))

wall_right = pygame.sprite.GroupSingle()
wall_right.add(Object("Assets/Images/objects/wall_lr.png", oc.wall_right_x, oc.wall_right_y, 1200, 60))

wall_right2 = pygame.sprite.GroupSingle()
wall_right2.add(Object("Assets/Images/objects/wall_lr.png", oc.wall_right2_x, oc.wall_right2_y, 600, 60))

wall_right3 = pygame.sprite.GroupSingle()
wall_right3.add(Object("Assets/Images/objects/wall_lr.png", oc.wall_right3_x, oc.wall_right3_y, 1600, 60))

shelf = pygame.sprite.GroupSingle()
shelf.add(Object("Assets/Images/objects/shelf.png", oc.shelf_x ,oc.shelf_y, 90, 300))

shelf2 = pygame.sprite.GroupSingle()
shelf2.add(Object("Assets/Images/objects/shelf_variant2.png", oc.shelf2_x ,oc.shelf2_y, 90, 300))

shelf3 = pygame.sprite.GroupSingle()
shelf3.add(Object("Assets/Images/objects/shelf_variant2.png", oc.shelf3_x ,oc.shelf3_y, 90, 300))

shelf4 = pygame.sprite.GroupSingle()
shelf4.add(Object("Assets/Images/objects/shelf_task3.png", oc.shelf4_x ,oc.shelf4_y, 100, 250))

shelf5 = pygame.sprite.GroupSingle()
shelf5.add(Object("Assets/Images/objects/shelf.png", oc.shelf5_x ,oc.shelf5_y, 100, 250))

pot = pygame.sprite.GroupSingle()
pot.add(Object("Assets/Images/objects/emptypot.png", oc.pot_x ,oc.pot_y, 20, 40))

pot2 = pygame.sprite.GroupSingle()
pot2.add(Object("Assets/Images/objects/emptypot.png", oc.pot2_x ,oc.pot2_y, 20, 40))

table = pygame.sprite.GroupSingle()
table.add(Object("Assets/Images/objects/table.png", oc.table_x ,oc.table_y, 80, 80))

table2 = pygame.sprite.GroupSingle()
table2.add(Object("Assets/Images/objects/table.png", oc.table2_x ,oc.table2_y, 80, 80))

table3 = pygame.sprite.GroupSingle()
table3.add(Object("Assets/Images/objects/table_variant2.png", oc.table3_x ,oc.table3_y, 80, 80))

box = pygame.sprite.GroupSingle()
box.add(Object("Assets/Images/objects/box.png", oc.box_x ,oc.box_y, 80, 80))

box2 = pygame.sprite.GroupSingle()
box2.add(Object("Assets/Images/objects/box.png", oc.box2_x ,oc.box2_y, 100, 100))

box3 = pygame.sprite.GroupSingle()
box3.add(Object("Assets/Images/objects/box.png", oc.box3_x ,oc.box3_y, 40, 40))

box4 = pygame.sprite.GroupSingle()
box4.add(Object("Assets/Images/objects/box.png", oc.box4_x ,oc.box4_y, 80, 80))

telescope = pygame.sprite.GroupSingle()
telescope.add(Object("Assets/Images/objects/Telescope.png", oc.telescope_x, oc.telescope_y, 75, 45))

hologram = pygame.sprite.GroupSingle()
hologram.add(Object("Assets/Images/objects/hologram.png", oc.hologram_x, oc.hologram_y, 125, 75))

#level2  ###################################################################
desklvl2 = pygame.sprite.GroupSingle()
desklvl2.add(Object("Assets/Images/objects/desk.png", oc.desklvl2_x, oc.desklvl2_y, 80, 110)) 

wall_ud = pygame.sprite.GroupSingle()
wall_ud.add(Object("Assets/Images/objects/1wall_ud.png", oc.wall_ud_x, oc.wall_ud_y, 60, 845))

wall_ud2 = pygame.sprite.GroupSingle()
wall_ud2.add(Object("Assets/Images/objects/1wall_ud.png", oc.wall_ud2_x, oc.wall_ud2_y, 60, 860))

wall_ud3 = pygame.sprite.GroupSingle()
wall_ud3.add(Object("Assets/Images/objects/1wall_ud.png", oc.wall_ud3_x, oc.wall_ud3_y, 60, 820))

wall_ud4 = pygame.sprite.GroupSingle()
wall_ud4.add(Object("Assets/Images/objects/1wall_ud.png", oc.wall_ud4_x, oc.wall_ud4_y, 60, 820))

wall_lr = pygame.sprite.GroupSingle()
wall_lr.add(Object("Assets/Images/objects/1wall_lr.png", oc.wall_lr_x, oc.wall_lr_y, 1410, 60))

wall_lr2 = pygame.sprite.GroupSingle()
wall_lr2.add(Object("Assets/Images/objects/1wall_lr.png", oc.wall_lr2_x, oc.wall_lr2_y, 910, 60))

wall_lr3 = pygame.sprite.GroupSingle()
wall_lr3.add(Object("Assets/Images/objects/1wall_lr.png", oc.wall_lr3_x, oc.wall_lr3_y, 525, 60))

wall_lr4 = pygame.sprite.GroupSingle()
wall_lr4.add(Object("Assets/Images/objects/1wall_lr.png", oc.wall_lr4_x, oc.wall_lr4_y, 140, 60))

shelflvl2 = pygame.sprite.GroupSingle()
shelflvl2.add(Object("Assets/Images/objects/shelf_variant2.png", oc.shelflvl2_x ,oc.shelflvl2_y, 90, 300))

device = pygame.sprite.GroupSingle()
device.add(Object("Assets/Images/objects/device.png", oc.device_x ,oc.device_y, 80, 250))

tablelvl2 = pygame.sprite.GroupSingle()
tablelvl2.add(Object("Assets/Images/objects/table_variant2.png", oc.tablelvl2_x ,oc.tablelvl2_y, 80, 80))

tree = pygame.sprite.GroupSingle()
tree.add(Object("Assets/Images/objects/1tree.png", oc.tree_x, oc.tree_y, 70, 70))

chairlvl2 = pygame.sprite.GroupSingle()
chairlvl2.add(Object("Assets/Images/objects/1chair.png", oc.chairlvl2_x, oc.chairlvl2_y, 90, 60))

chairlvl23 = pygame.sprite.GroupSingle()
chairlvl23.add(Object("Assets/Images/objects/1chair.png", oc.chairlvl23_x, oc.chairlvl23_y, 90, 60))

tree = pygame.sprite.GroupSingle()
tree.add(Object("Assets/Images/objects/1tree.png", oc.tree_x, oc.tree_y, 100, 70))

tree2 = pygame.sprite.GroupSingle()
tree2.add(Object("Assets/Images/objects/1tree2.png", oc.tree2_x, oc.tree2_y, 100, 70))

tree3 = pygame.sprite.GroupSingle()
tree3.add(Object("Assets/Images/objects/1tree2.png", oc.tree3_x, oc.tree3_y, 100, 70))

tree4 = pygame.sprite.GroupSingle()
tree4.add(Object("Assets/Images/objects/1tree3.png", oc.tree4_x, oc.tree4_y, 100, 70))

tree5 = pygame.sprite.GroupSingle()
tree5.add(Object("Assets/Images/objects/1tree3.png", oc.tree5_x, oc.tree5_y, 100, 70))

hologramlvl2 = pygame.sprite.GroupSingle()
hologramlvl2.add(Object("Assets/Images/objects/hologram.png", oc.hologramlvl2_x, 880, 125, 75))
hologramlvl2.sprite.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/objects/hologram.png').convert_alpha(), (125, 205 )), True, False)

options = False
controls_options = False

list = [paper1, paper2, paper3]
counter = 0
is_quest_1_screen = False
is_quest_2_screen = False
is_quest_2_screen_completed = False
starting_point = None

sentence = []
books = []

is_quest_4_screen = False
levers = []

end = False

#functions
def main():
    global level
    global key

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
                if event.type == pygame.KEYDOWN:
                    key = event.key
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
    global level
    if level == 1:
        reversemove(desk.sprite)
        reversemove(chair.sprite)
        reversemove(shelf.sprite)
        reversemove(desk2.sprite)
        reversemove(chair2.sprite)
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
        reversemove(hologram.sprite)
    elif level == 2:
        reversemove(wall_ud.sprite)
        reversemove(wall_lr.sprite)
        reversemove(wall_ud2.sprite)
        reversemove(wall_ud3.sprite)
        reversemove(wall_lr3.sprite)
        reversemove(wall_lr2.sprite)
        reversemove(wall_ud4.sprite)
        reversemove(wall_lr4.sprite)
        reversemove(device.sprite)
        reversemove(desklvl2.sprite)
        reversemove(shelflvl2.sprite)
        reversemove(tablelvl2.sprite)
        reversemove(chairlvl2.sprite)
        reversemove(chairlvl23.sprite)
        reversemove(tree.sprite)
        reversemove(tree2.sprite)
        reversemove(tree3.sprite)
        reversemove(hologramlvl2.sprite)
        reversemove(tree4.sprite)
        reversemove(tree5.sprite)
        
    reversemove(floor.sprite)
    
    reversemove(paper1.sprite)
    reversemove(paper2.sprite)
    reversemove(paper3.sprite)

def is_open():
    global key

    if key == pygame.K_ESCAPE and level != 3:
        return False
    return True

#display
def draw_game():
    global paper_complete, book_complete, computer_complete, level
    global R, Y, G
    global key
    
    screen.fill((0, 0, 0))
    
    floor.draw(screen)

    global counter

    if paper1.sprite.check_col() and key == pygame.K_e and paper1 in list:
        list.remove(paper1)
        counter += 1

    if paper2.sprite.check_col() and key == pygame.K_e and paper2 in list:
        list.remove(paper2)
        counter += 1

    if paper3.sprite.check_col() and key == pygame.K_e and paper3 in list:
        list.remove(paper3)
        counter += 1


    for i in list:
        i.draw(screen)    

    player.draw(screen)

    if level == 1: ########################################################################
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
        hologram.draw(screen)
    elif level == 2:
        wall_ud.draw(screen)
        wall_lr.draw(screen)
        wall_ud2.draw(screen)
        wall_lr3.draw(screen)
        wall_ud3.draw(screen)
        wall_lr2.draw(screen)
        wall_ud4.draw(screen)
        wall_lr4.draw(screen)
        device.draw(screen)
        desklvl2.draw(screen)
        shelflvl2.draw(screen)
        chairlvl2.draw(screen)
        tablelvl2.draw(screen)
        chairlvl23.draw(screen)
        tree.draw(screen)
        tree2.draw(screen)
        tree3.draw(screen)
        tree4.draw(screen)
        hologramlvl2.draw(screen)
        tree5.draw(screen)
    
    paper_col()

    for i in range(counter):
        image = pygame.image.load("assets/images/papers/paper.png")
        screen.blit(pygame.transform.scale(image, (50, 50)), (i * 50, 0))

    if counter == 3:
        screen.blit(pygame.transform.scale(pygame.image.load("assets/images/controls/q.png"), (40, 40)), (160, 5))

    global is_quest_1_screen
    global is_quest_2_screen

    if len(list) == 0 and key == pygame.K_q:
        is_quest_1_screen = True
        paper_complete = True

    if is_quest_1_screen:
        is_quest_1_screen = is_open()
        screen.blit(pygame.transform.scale(pygame.image.load("assets/images/papers/custom_text.png"), (screen_width, screen_height)), (0, 0))

    if desk_col() == True:
        is_quest_2_screen = True
        computer_complete = True
        
    if is_quest_2_screen == True:
        is_quest_2_screen = is_open()
        screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/quest_2.png"), (screen_width, screen_height)), (0, 0))


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                sentence.append(event.unicode)

        for i in range(18):
            if i < len(sentence):
                image = pygame.image.load("assets/images/points/point_typed.png")
                screen.blit(pygame.transform.scale(image, (35, 35)), ((i * 30) + 375, 550)) 
            else:    
                image = pygame.image.load("assets/images/points/point.png")
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
                image = pygame.image.load("assets/images/rects/rect_clicked.png")
                screen.blit(pygame.transform.scale(image, (20, 30)), ((i * 30) + 500, 500)) 
            else:    
                image = pygame.image.load("assets/images/rects/rect.png")
                screen.blit(pygame.transform.scale(image, (20, 30)), ((i * 30) + 500, 500))

        if len(books) >= 9:
            books_string = ''.join(books)
            if books_string == "123412458":
                if is_open():
                    screen.blit(pygame.transform.scale(pygame.image.load("assets/images/papers/custom_text3.png"), (screen_width-200, screen_height-200)), (100, 100))
                    book_complete = True
            else:

                if starting_point == None:
                    starting_point = datetime.datetime.now()
                
                current_point = datetime.datetime.now()
                if (current_point - starting_point).seconds < 5:
                    for i in range(9):
                        image = pygame.image.load("assets/images/rects/rect_wrong.png")
                        screen.blit(pygame.transform.scale(image, (20, 30)), ((i * 30) + 500, 500))
                else:
                    starting_point = None
                    books.clear()
    
    if hologram1_col():
            level = 2
            floor.sprite.rect.x = -900
            floor.sprite.rect.y = -600
            floor.sprite.image = pygame.image.load('Assets/Images/backgrounds/Floor1.png').convert_alpha()
            floor.sprite.image = pygame.transform.scale(floor.sprite.image, (screen_width*4, screen_height*4))


    global is_quest_4_screen

    if board_col():
        is_quest_4_screen = True

    if is_quest_4_screen:
        is_quest_4_screen = is_open()
        if R:
            if G: screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/levers_boardRG.png"), (screen_width, screen_height)), (0, 0))
            elif Y: screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/levers_boardRY.png"), (screen_width, screen_height)), (0, 0))
            else: screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/levers_boardR.png"), (screen_width, screen_height)), (0, 0))
        elif G:
            if Y: screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/levers_boardYG.png"), (screen_width, screen_height)), (0, 0))
            else: screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/levers_boardG.png"), (screen_width, screen_height)), (0, 0))
        elif Y: screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/levers_boardY.png"), (screen_width, screen_height)), (0, 0))
        else: screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/levers_board.png"), (screen_width, screen_height)), (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and len(levers) < 3:
                mouse = pygame.mouse.get_pos()
                if 477 < mouse[0] < 534 and 359 < mouse[1] < 535:
                    levers.append('1')
                    R = True
                
                if 617 < mouse[0] < 702 and 361 < mouse[1] < 537:
                    levers.append('2')
                    Y = True

                if 785 < mouse[0] < 868 and 361 < mouse[1] < 532:
                    levers.append('3')
                    G = True

        global device_complete

        if len(levers) == 3:
            R, Y, G = False, False, False
            levers_string = ''.join(levers)
            if levers_string == "213":
                device_complete = True
                screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/levers_board_pressed.png"), (screen_width, screen_height)), (0, 0))
                screen.blit(pygame.transform.scale(pygame.image.load("assets/images/papers/custom_text4.png"), (800, 225)), (275, 60))
            else:

                if starting_point == None:
                    starting_point = datetime.datetime.now()
                
                current_point = datetime.datetime.now()
                if (current_point - starting_point).seconds < 5:
                    for i in range(9):
                        screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/levers_board_pressed.png"), (screen_width, screen_height)), (0, 0))
                        screen.blit(pygame.transform.scale(pygame.image.load("assets/images/texts/error_text.png"), (1000, 200)), (170, 88))  
                else:
                    starting_point = None
                    levers.clear()

    #print(floor.sprite.rect.x, floor.sprite.rect.y)

    #pygame.draw.rect(screen, (255, 0, 0), hologramlvl2.sprite, 2)
    
    global end

    if hologram2_col():
        level = 3
        end = True
    
    if end:
        end = is_open()

        screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/mars_last.png"), (screen_width, screen_height)), (0, 0))


    if controls:
        blit_controls()

    global options
    global controls_options

    if key == pygame.K_m and is_quest_2_screen == False:
        options = True

    if options:
        options = is_open()
        screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/transparency.png"), (1280, 720)), (0, 0))
        screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/options.png"), (400, 600)), (430, 50))

        quit_button = Button(screen_width/2 - 65, screen_height/2 + 200, "assets/images/buttons/quit_button", 1)
        controls_button = Button(screen_width/2 - 150, screen_height/2 + 100, "assets/images/buttons/controls_button", 1)
        # restart_button = Button(screen_width/2 - 135, screen_height/2 + 40, "assets/images/buttons/restart_button", 1)
        volume_up_button = Button(screen_width/2 + 120, screen_height/2 + 25, "assets/images/buttons/volume_up_button", 0.5)
        volume_down_button = Button(screen_width/2 - 170, screen_height/2 + 25, "assets/images/buttons/volume_down_button", 0.5)

        blit_volume()
        screen.blit(pygame.image.load("assets/images/buttons/volume_button.png"), (screen_width/2 - 115, screen_height/2 - 50))
        screen.blit(pygame.image.load("assets/images/buttons/options_button.png"), (screen_width/2 - 135, screen_height/2 - 230))

        quit_button.change_button()
        controls_button.change_button()
        # restart_button.change_button()
        volume_up_button.change_button()
        volume_down_button.change_button()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.check_clicked():
                    exit(0)

                # if restart_button.check_clicked():
                #     restart()

                if volume_up_button.check_clicked():
                    global volume_strength
                    
                    print(volume_strength)

                    if volume_strength < 0.2:
                        volume_strength += 0.02
                        pygame.mixer.music.set_volume(volume_strength + 0.02)

                if volume_down_button.check_clicked():

                    print(volume_strength)

                    if volume_strength > 0:
                        pygame.mixer.music.set_volume(volume_strength - 0.02)
                        volume_strength -= 0.02

                if controls_button.check_clicked():
                    key = pygame.K_ESCAPE
                    controls_options = True

    if controls_options:
        if starting_point == None:
            starting_point = datetime.datetime.now()
        
        current_point = datetime.datetime.now()
        if (current_point - starting_point).seconds < 5:
            blit_controls()
        else:
            starting_point = None
            controls_options = False


    ########################################################################
    paper1.update()
    paper2.update()
    paper3.update()

    player.update()
    
    if level == 1:
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
        hologram.update()
    elif level == 2:
        wall_ud.update()
        wall_lr.update()
        wall_ud2.update()
        wall_lr3.update()
        wall_ud3.update()
        wall_lr2.update()
        wall_ud4.update()
        wall_lr4.update()
        device.update()
        desklvl2.update()
        shelflvl2.update()
        tablelvl2.update()
        chairlvl2.update()
        chairlvl23.update()
        tree.update()
        tree2.update()
        tree3.update()
        hologramlvl2.update()
        tree4.update()
        tree5.update()
    
    floor.update()

    #print(floor.sprite.rect.x, floor.sprite.rect.y)    

def blit_controls():
    screen.blit(pygame.transform.scale(pygame.image.load("assets/images/controls/w.png"), (40, 40)), (player.sprite.rect.x, player.sprite.rect.y - 80))
    screen.blit(pygame.transform.scale(pygame.image.load("assets/images/controls/a.png"), (40, 40)), (player.sprite.rect.x - 80, player.sprite.rect.y))
    screen.blit(pygame.transform.scale(pygame.image.load("assets/images/controls/s.png"), (40, 40)), (player.sprite.rect.x, player.sprite.rect.y + 80))
    screen.blit(pygame.transform.scale(pygame.image.load("assets/images/controls/d.png"), (40, 40)), (player.sprite.rect.x + 80, player.sprite.rect.y))
    screen.blit(pygame.transform.scale(pygame.image.load("assets/images/controls/m.png"), (250, 40)), (800, 500))
    screen.blit(pygame.transform.scale(pygame.image.load("assets/images/controls/esc.png"), (350, 40)), (800, 550))

def blit_volume():
    global volume_strength

    if volume_strength >= 0.2:
        index = 10
    elif 0.2 > volume_strength >= 0.18:
        index = 9
    elif 0.18 > volume_strength >= 0.16:
        index = 8
    elif 0.16 > volume_strength >= 0.14:
        index = 7
    elif 0.14 > volume_strength >= 0.12:
        index = 6
    elif 0.12 > volume_strength >= 0.1:
        index = 5
    elif 0.1 > volume_strength >= 0.08:
        index = 4
    elif 0.08 > volume_strength >= 0.06:
        index = 3
    elif 0.06 > volume_strength >= 0.04:
        index = 2
    elif 0.04 > volume_strength >= 0.02:
        index = 1
    elif 0.2 > volume_strength:
        index = 0

    image = pygame.image.load(f"assets/images/volume_bars/volume{index}.png")
    screen.blit(pygame.transform.scale(image, (image.get_width() * 0.75, image.get_height() * 0.75)), (screen_width/2 - 120, screen_height/2 + 30))

def paper_col():
    papercol = (player.sprite.rect.colliderect(paper1.sprite.rect) and paper1 in list) or (player.sprite.rect.colliderect(paper2.sprite.rect) and paper2 in list) or (player.sprite.rect.colliderect(paper3.sprite.rect) and paper3 in list)

    if papercol:
        screen.blit(pygame.transform.scale(pygame.image.load("assets/images/controls/e.png"), (40, 40)), (player.sprite.rect.x, player.sprite.rect.y-40))

def desk_col():
    global key

    deskcol = floor.sprite.rect.x < -2150 and floor.sprite.rect.x > -2350 and floor.sprite.rect.y == -408

    if deskcol:
        screen.blit(pygame.transform.scale(pygame.image.load("assets/images/controls/p.png"), (40, 40)), (player.sprite.rect.x, player.sprite.rect.y-40))

    return deskcol and key == pygame.K_p

def shelf_col():
    shelfcol = floor.sprite.rect.x < -1300 and floor.sprite.rect.x > -1730 and floor.sprite.rect.y == -1412
    return shelfcol 

def hologram1_col():
    global paper_complete, book_complete, computer_complete
    global key

    if paper_complete == book_complete == computer_complete == True:

        holocol = floor.sprite.rect.x < -800 and floor.sprite.rect.x > -1000 and (floor.sprite.rect.y == -100 or floor.sprite.rect.y == -20)

        if holocol:
            screen.blit(pygame.transform.scale(pygame.image.load("assets/images/controls/e.png"), (40, 40)), (player.sprite.rect.x, player.sprite.rect.y-40))


        return holocol and key == pygame.K_e and level == 1

def board_col():
    global key

    boardcol = floor.sprite.rect.x < -1508 and floor.sprite.rect.x > -1848 and floor.sprite.rect.y == -796

    if boardcol:
        screen.blit(pygame.transform.scale(pygame.image.load("assets/images/controls/p.png"), (40, 40)), (player.sprite.rect.x, player.sprite.rect.y-40))

    return boardcol and key == pygame.K_p and level == 2

def hologram2_col():
    global device_complete
    global key

    if device_complete:
        key_pressed = pygame.key.get_pressed()

        holocol = floor.sprite.rect.y < -1128 and floor.sprite.rect.y > -1224 and floor.sprite.rect.x == -2676        

        if holocol:
            screen.blit(pygame.transform.scale(pygame.image.load("assets/images/controls/e.png"), (40, 40)), (player.sprite.rect.x, player.sprite.rect.y-40))

        return holocol and key == pygame.K_e and level == 2

# def restart():
#     global level, col, paper_complete, book_complete, computer_complete, R, Y, G, device_complete, list, counter, is_quest_1_screen, is_quest_2_screen, is_quest_2_screen_completed, starting_point, sentence, books, is_quest_4_screen, levers, end

#     level = 1
#     col = False
#     try_move = []
#     paper_complete, book_complete, computer_complete = True, True, True
#     R, Y, G = False, False, False
#     device_complete = True
#     options = False

#     list = [paper1, paper2, paper3]
#     counter = 0
#     is_quest_1_screen = False
#     is_quest_2_screen = False
#     is_quest_2_screen_completed = False
#     starting_point = None

#     sentence = []
#     books = []

#     is_quest_4_screen = False
#     levers = []

#     end = False

#     floor.sprite.rect.x = -100
#     floor.sprite.rect.y = -100

#     wall_right2.sprite.rect.x = oc.wall_right2_x
#     wall_up.sprite.rect.x = oc.wall_up_x
#     wall_down.sprite.rect.x = oc.wall_down_x
#     wall_left.sprite.rect.x = oc.wall_left_x
#     wall_right.sprite.rect.x = oc.wall_right_x
#     wall_up2.sprite.rect.x = oc.wall_up2_x
#     desk.sprite.rect.x = oc.desk_x
#     chair.sprite.rect.x = oc.chair_x
#     shelf.sprite.rect.x = oc.shelf_x
#     desk2.sprite.rect.x = oc.desk2_x
#     chair2.sprite.rect.x = oc.chair2_x
#     wall_down2.sprite.rect.x = oc.wall_down2_x
#     desk3.sprite.rect.x = oc.desk3_x
#     chair3.sprite.rect.x = oc.chair3_x
#     wall_left2.sprite.rect.x = oc.wall_left2_x
#     wall_right3.sprite.rect.x = oc.wall_right3_x
#     shelf2.sprite.rect.x = oc.shelf2_x
#     shelf3.sprite.rect.x = oc.shelf3_x
#     desk4.sprite.rect.x = oc.desk4_x
#     shelf4.sprite.rect.x = oc.shelf4_x
#     desk5.sprite.rect.x = oc.desk5_x
#     shelf5.sprite.rect.x = oc.shelf5_x
#     pot.sprite.rect.x = oc.pot_x
#     pot2.sprite.rect.x = oc.pot2_x
#     table.sprite.rect.x = oc.table_x
#     table2.sprite.rect.x = oc.table2_x
#     table3.sprite.rect.x = oc.table3_x
#     box.sprite.rect.x = oc.box_x
#     box2.sprite.rect.x = oc.box2_x
#     box3.sprite.rect.x = oc.box3_x
#     telescope.sprite.rect.x = oc.telescope_x
#     box4.sprite.rect.x = oc.box4_x
#     hologram.sprite.rect.x = oc.hologram_x
#     wall_ud.sprite.rect.x = oc.wall_ud_x
#     wall_lr.sprite.rect.x = oc.wall_lr_x
#     wall_ud2.sprite.rect.x = oc.wall_ud2_x
#     wall_lr3.sprite.rect.x = oc.wall_lr3_x
#     wall_ud3.sprite.rect.x = oc.wall_ud3_x
#     wall_lr2.sprite.rect.x = oc.wall_lr2_x
#     wall_ud4.sprite.rect.x = oc.wall_ud4_x
#     wall_lr4.sprite.rect.x = oc.wall_lr4_x
#     device.sprite.rect.x = oc.device_x
#     desklvl2.sprite.rect.x = oc.desklvl2_x
#     shelflvl2.sprite.rect.x = oc.shelflvl2_x
#     tablelvl2.sprite.rect.x = oc.tablelvl2_x
#     chairlvl2.sprite.rect.x = oc.chairlvl2_x
#     chairlvl23.sprite.rect.x = oc.chairlvl23_x
#     tree.sprite.rect.x = oc.tree_x
#     tree2.sprite.rect.x = oc.tree2_x
#     tree3.sprite.rect.x = oc.tree3_x
#     hologramlvl2.sprite.rect.x = oc.hologramlvl2_x
#     tree4.sprite.rect.x = oc.tree4_x
#     tree5.sprite.rect.x = oc.tree5_x

#     wall_right2.sprite.rect.y = oc.wall_right2_y
#     wall_up.sprite.rect.y = oc.wall_up_y
#     wall_down.sprite.rect.y = oc.wall_down_y
#     wall_left.sprite.rect.y = oc.wall_left_y
#     wall_right.sprite.rect.y = oc.wall_right_y
#     wall_up2.sprite.rect.y = oc.wall_up2_y
#     desk.sprite.rect.y = oc.desk_y
#     chair.sprite.rect.y = oc.chair_y
#     shelf.sprite.rect.y = oc.shelf_y
#     desk2.sprite.rect.y = oc.desk2_y
#     chair2.sprite.rect.y = oc.chair2_y
#     wall_down2.sprite.rect.y = oc.wall_down2_y
#     desk3.sprite.rect.y = oc.desk3_y
#     chair3.sprite.rect.y = oc.chair3_y
#     wall_left2.sprite.rect.y = oc.wall_left2_y
#     wall_right3.sprite.rect.y = oc.wall_right3_y
#     shelf2.sprite.rect.y = oc.shelf2_y
#     shelf3.sprite.rect.y = oc.shelf3_y
#     desk4.sprite.rect.y = oc.desk4_y
#     shelf4.sprite.rect.y = oc.shelf4_y
#     desk5.sprite.rect.y = oc.desk5_y
#     shelf5.sprite.rect.y = oc.shelf5_y
#     pot.sprite.rect.y = oc.pot_y
#     pot2.sprite.rect.y = oc.pot2_y
#     table.sprite.rect.y = oc.table_y
#     table2.sprite.rect.y = oc.table2_y
#     table3.sprite.rect.y = oc.table3_y
#     box.sprite.rect.y = oc.box_y
#     box2.sprite.rect.y = oc.box2_y
#     box3.sprite.rect.y = oc.box3_y
#     telescope.sprite.rect.y = oc.telescope_y
#     box4.sprite.rect.y = oc.box4_y
#     hologram.sprite.rect.y = oc.hologram_y
#     wall_ud.sprite.rect.y = oc.wall_ud_y
#     wall_lr.sprite.rect.y = oc.wall_lr_y
#     wall_ud2.sprite.rect.y = oc.wall_ud2_y
#     wall_lr3.sprite.rect.y = oc.wall_lr3_y
#     wall_ud3.sprite.rect.y = oc.wall_ud3_y
#     wall_lr2.sprite.rect.y = oc.wall_lr2_y
#     wall_ud4.sprite.rect.y = oc.wall_ud4_y
#     wall_lr4.sprite.rect.y = oc.wall_lr4_y
#     device.sprite.rect.y = oc.device_y
#     desklvl2.sprite.rect.y = oc.desklvl2_y
#     shelflvl2.sprite.rect.y = oc.shelflvl2_y
#     tablelvl2.sprite.rect.y = oc.tablelvl2_y
#     chairlvl2.sprite.rect.y = oc.chairlvl2_y
#     chairlvl23.sprite.rect.y = oc.chairlvl23_y
#     tree.sprite.rect.y = oc.tree_y
#     tree2.sprite.rect.y = oc.tree2_y
#     tree3.sprite.rect.y = oc.tree3_y
#     hologramlvl2.sprite.rect.y = oc.hologramlvl2_y
#     tree4.sprite.rect.y = oc.tree4_y
#     tree5.sprite.rect.y = oc.tree5_y

#call main function
if __name__ == "__main__":
    main()