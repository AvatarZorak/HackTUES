import pygame
from constants import screen_width, screen_height, object_scale
from class_player import Player, player
from class_background import Background, floor


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
            dontmove()
        col = False
        try_move = []


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

hologram = pygame.sprite.GroupSingle()
hologram.add(Object("Assets/Images/objects/hologram.png", -90, -580, 125, 75))

#level2  ###################################################################
desklvl2 = pygame.sprite.GroupSingle()
desklvl2.add(Object("Assets/Images/objects/desk.png", 900, 350, 80, 110)) 

wall_ud = pygame.sprite.GroupSingle()
wall_ud.add(Object("Assets/Images/objects/1wall_ud.png", 1070, 270, 60, 845))

wall_ud2 = pygame.sprite.GroupSingle()
wall_ud2.add(Object("Assets/Images/objects/1wall_ud.png", 1060, 1370, 60, 860))

wall_ud3 = pygame.sprite.GroupSingle()
wall_ud3.add(Object("Assets/Images/objects/1wall_ud.png", 2320, 570, 60, 820))

wall_ud4 = pygame.sprite.GroupSingle()
wall_ud4.add(Object("Assets/Images/objects/1wall_ud.png", 2320, 1310, 60, 820))

wall_lr = pygame.sprite.GroupSingle()
wall_lr.add(Object("Assets/Images/objects/1wall_lr.png", 460, 350, 1410, 60))

wall_lr2 = pygame.sprite.GroupSingle()
wall_lr2.add(Object("Assets/Images/objects/1wall_lr.png", 1660, 50, 910, 60))

wall_lr3 = pygame.sprite.GroupSingle()
wall_lr3.add(Object("Assets/Images/objects/1wall_lr.png", 2890, 950, 525, 60))

wall_lr4 = pygame.sprite.GroupSingle()
wall_lr4.add(Object("Assets/Images/objects/1wall_lr.png", 1660, 1310, 140, 60))

shelflvl2 = pygame.sprite.GroupSingle()
shelflvl2.add(Object("Assets/Images/objects/shelf_variant2.png", 750 ,700, 90, 300))

device = pygame.sprite.GroupSingle()
device.add(Object("Assets/Images/objects/device.png", 1420 ,450, 80, 250))

tablelvl2 = pygame.sprite.GroupSingle()
tablelvl2.add(Object("Assets/Images/objects/table_variant2.png", 850 ,1200, 80, 80))

tree = pygame.sprite.GroupSingle()
tree.add(Object("Assets/Images/objects/1tree.png", -500, -200, 70, 70))

chairlvl2 = pygame.sprite.GroupSingle()
chairlvl2.add(Object("Assets/Images/objects/1chair.png", 870, 1100, 90, 60))

chairlvl23 = pygame.sprite.GroupSingle()
chairlvl23.add(Object("Assets/Images/objects/1chair.png", 900, 400, 90, 60))

tree = pygame.sprite.GroupSingle()
tree.add(Object("Assets/Images/objects/1tree.png", 600, 1200, 100, 70))

tree2 = pygame.sprite.GroupSingle()
tree2.add(Object("Assets/Images/objects/1tree2.png", 2000, 600, 100, 70))

tree3 = pygame.sprite.GroupSingle()
tree3.add(Object("Assets/Images/objects/1tree2.png", 1500, 1250, 100, 70))

tree4 = pygame.sprite.GroupSingle()
tree4.add(Object("Assets/Images/objects/1tree3.png", 2550, 860, 100, 70))

tree5 = pygame.sprite.GroupSingle()
tree5.add(Object("Assets/Images/objects/1tree3.png", 2550, 970, 100, 70))

hologramlvl2 = pygame.sprite.GroupSingle()
hologramlvl2.add(Object("Assets/Images/objects/hologram.png", 2500, 880, 125, 75))
hologramlvl2.sprite.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Assets/Images/objects/hologram.png').convert_alpha(), (125, 205 )), True, False)

def reversemove(sprite): #rollback if collide
    for i in try_move:
        if i == "+x": sprite.rect.x -= 4
        elif i == "+y": sprite.rect.y -= 4
        elif i == "-x": sprite.rect.x += 4
        elif i == "-y": sprite.rect.y += 4

def dontmove(): #initiate rollback #####################################################
    #global level
    #if level == 1:
        
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
#elif level == 2:
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
    
    #reversemove(paper1.sprite)
    #reversemove(paper2.sprite)
    #reversemove(paper3.sprite)
