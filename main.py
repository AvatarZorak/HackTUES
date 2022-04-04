#libraries
from turtle import width
import pygame
from menu import Button, menu
from sys import exit
import datetime
import random
from class_player import Player
from class_background import Background
import class_object as o
from class_paper import Paper
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
paper_complete, book_complete, computer_complete = True, True, True
R, Y, G = False, False, False
device_complete = True

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

paper_positions = [[0, 0], [100, 100], [200, 200], [500, 600], [372, 536], [1123, -888], [100, -500], [-100, 860], [1300, 860], [1700, 860]]

#definition of objects
#level 1

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

is_level_3_screen = False

#functions
def main():
    global level
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



# def dontmove(self): #initiate rollback #####################################################
#     global level
#     if level == 1:
        
#         reversemove(desk.sprite)
#         reversemove(chair.sprite)
#         reversemove(shelf.sprite)
#         reversemove(desk2.sprite)
#         reversemove(chair2.sprite)
#         reversemove(wall_up.sprite)
#         reversemove(wall_down.sprite)
#         reversemove(wall_left.sprite)
#         reversemove(wall_right.sprite)
#         reversemove(wall_up2.sprite)
#         reversemove(wall_right2.sprite)
#         reversemove(wall_down2.sprite)
#         reversemove(desk3.sprite)
#         reversemove(desk4.sprite)
#         reversemove(chair3.sprite)
#         reversemove(wall_left2.sprite)
#         reversemove(wall_right3.sprite)
#         reversemove(shelf2.sprite)
#         reversemove(shelf3.sprite)
#         reversemove(shelf4.sprite)
#         reversemove(desk5.sprite)
#         reversemove(shelf5.sprite)
#         reversemove(pot.sprite)
#         reversemove(pot2.sprite)
#         reversemove(table.sprite)
#         reversemove(table2.sprite)
#         reversemove(table3.sprite)
#         reversemove(box.sprite)
#         reversemove(box2.sprite)
#         reversemove(box3.sprite)
#         reversemove(box4.sprite)
#         reversemove(telescope.sprite)
#         reversemove(hologram.sprite)
#     elif level == 2:
#         reversemove(wall_ud.sprite)
#         reversemove(wall_lr.sprite)
#         reversemove(wall_ud2.sprite)
#         reversemove(wall_ud3.sprite)
#         reversemove(wall_lr3.sprite)
#         reversemove(wall_lr2.sprite)
#         reversemove(wall_ud4.sprite)
#         reversemove(wall_lr4.sprite)
#         reversemove(device.sprite)
#         reversemove(desklvl2.sprite)
#         reversemove(shelflvl2.sprite)
#         reversemove(tablelvl2.sprite)
#         reversemove(chairlvl2.sprite)
#         reversemove(chairlvl23.sprite)
#         reversemove(tree.sprite)
#         reversemove(tree2.sprite)
#         reversemove(tree3.sprite)
#         reversemove(hologramlvl2.sprite)
#         reversemove(tree4.sprite)
#         reversemove(tree5.sprite)
        
#     reversemove(floor.sprite)
    
#     reversemove(paper1.sprite)
#     reversemove(paper2.sprite)
#     reversemove(paper3.sprite)

def is_open():
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_ESCAPE]:
        return False
    return True

#display
def draw_game():
    global paper_complete, book_complete, computer_complete, level
    global R, Y, G
    
    
    screen.fill((0, 0, 0))
    
    o.floor.draw(screen)

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

    o.player.draw(screen)
    
    if level == 1: ########################################################################
        o.wall_left2.draw(screen)
        o.wall_right2.draw(screen)
        o.wall_up.draw(screen)
        o.wall_right.draw(screen)
        o.shelf.draw(screen)
        o.wall_down.draw(screen)
        o.wall_down2.draw(screen)
        o.shelf2.draw(screen)
        o.shelf3.draw(screen)
        o.shelf4.draw(screen)
        o.wall_up2.draw(screen)
        o.wall_left.draw(screen)
        o.desk.draw(screen)
        o.chair.draw(screen)
        o.desk2.draw(screen)
        o.chair2.draw(screen)
        o.desk3.draw(screen)
        o.chair3.draw(screen)
        o.desk4.draw(screen)
        o.desk5.draw(screen)
        o.wall_right3.draw(screen)
        o.shelf5.draw(screen)
        o.pot.draw(screen)
        o.pot2.draw(screen)
        o.table.draw(screen)
        o.table2.draw(screen)
        o.table3.draw(screen)
        o.box2.draw(screen)
        o.box.draw(screen)
        o.box3.draw(screen)
        o.box4.draw(screen)
        o.telescope.draw(screen)
        o.hologram.draw(screen)
    elif level == 2:
        o.wall_ud.draw(screen)
        o.wall_lr.draw(screen)
        o.wall_ud2.draw(screen)
        o.wall_lr3.draw(screen)
        o.wall_ud3.draw(screen)
        o.wall_lr2.draw(screen)
        o.wall_ud4.draw(screen)
        o.wall_lr4.draw(screen)
        o.device.draw(screen)
        o.desklvl2.draw(screen)
        o.shelflvl2.draw(screen)
        o.chairlvl2.draw(screen)
        o.tablelvl2.draw(screen)
        o.chairlvl23.draw(screen)
        o.tree.draw(screen)
        o.tree2.draw(screen)
        o.tree3.draw(screen)
        o.tree4.draw(screen)
        o.hologramlvl2.draw(screen)
        o.tree5.draw(screen)
    
    for i in range(counter):
        image = pygame.image.load("assets/images/papers/paper.png")
        screen.blit(pygame.transform.scale(image, (50, 50)), (i * 50, 0))

    global is_quest_1_screen
    global is_quest_2_screen

    key_pressed = pygame.key.get_pressed()
    if len(list) == 0 and key_pressed[pygame.K_q]:
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
            o.floor.sprite.rect.x = -900
            o.floor.sprite.rect.y = -600
            o.floor.sprite.image = pygame.image.load('Assets/Images/backgrounds/Floor1.png').convert_alpha()
            o.floor.sprite.image = pygame.transform.scale(o.floor.sprite.image, (screen_width*4, screen_height*4))


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


    global is_level_3_screen

    if hologram2_col():
        is_level_3_screen = True
    
    if is_level_3_screen:
        is_level_3_screen = is_open()
        image = pygame.image.load("assets/images/backgrounds/mars_last.png")
        screen.blit(pygame.transform.scale(image, (screen_width, screen_height)), (0, 0))
        print("maikati smurdi")
    ########################################################################
    paper1.update()
    paper2.update()
    paper3.update()

    o.player.update()
    
    if level == 1:
        o.wall_right2.update()
        o.wall_up.update()
        o.wall_down.update()
        o.wall_left.update()
        o.wall_right.update()
        o.wall_up2.update()
        o.desk.update()
        o.chair.update()
        o.shelf.update()
        o.desk2.update()
        o.chair2.update()
        o.wall_down2.update()
        o.desk3.update()
        o.chair3.update()
        o.wall_left2.update()
        o.wall_right3.update()
        o.shelf2.update()
        o.shelf3.update()
        o.desk4.update()
        o.shelf4.update()
        o.desk5.update()
        o.shelf5.update()
        o.pot.update()
        o.pot2.update()
        o.table.update()
        o.table2.update()
        o.table3.update()
        o.box.update()
        o.box2.update()
        o.box3.update()
        o.telescope.update()
        o.box4.update()
        o.hologram.update()
    elif level == 2:
        o.wall_ud.update()
        o.wall_lr.update()
        o.wall_ud2.update()
        o.wall_lr3.update()
        o.wall_ud3.update()
        o.wall_lr2.update()
        o.wall_ud4.update()
        o.wall_lr4.update()
        o.device.update()
        o.desklvl2.update()
        o.shelflvl2.update()
        o.tablelvl2.update()
        o.chairlvl2.update()
        o.chairlvl23.update()
        o.tree.update()
        o.tree2.update()
        o.tree3.update()
        o.hologramlvl2.update()
        o.tree4.update()
        o.tree5.update()
    
    o.floor.update()
    #print(floor.sprite.rect.x, floor.sprite.rect.y)    
    
def desk_col():
    key_pressed = pygame.key.get_pressed()
    deskcol = o.floor.sprite.rect.x < -2150 and o.floor.sprite.rect.x > -2350 and o.floor.sprite.rect.y == -408 and key_pressed[pygame.K_p]
    return deskcol

def shelf_col():
    shelfcol = o.floor.sprite.rect.x < -1300 and o.floor.sprite.rect.x > -1730 and o.floor.sprite.rect.y == -1412
    return shelfcol 

def hologram1_col():
    global paper_complete, book_complete, computer_complete
    if paper_complete == book_complete == computer_complete == True:
        key_pressed = pygame.key.get_pressed()
        holocol = o.floor.sprite.rect.x < -800 and o.floor.sprite.rect.x > -1000 and (o.floor.sprite.rect.y == -100 or o.floor.sprite.rect.y == -20) and key_pressed[pygame.K_e]
        return holocol

def hologram2_col():
    global device_complete
    if device_complete == True:
        key_pressed = pygame.key.get_pressed()
        holocol = o.floor.sprite.rect.y < -1128 and o.floor.sprite.rect.y > -1224 and o.floor.sprite.rect.x == -2676 and key_pressed == pygame.K_e
        return holocol

def board_col():
    key_pressed = pygame.key.get_pressed()
    boardcol = o.floor.sprite.rect.x < -1508 and o.floor.sprite.rect.x > -1848 and o.floor.sprite.rect.y == -796 and key_pressed[pygame.K_p]
    return boardcol

#call main function
if __name__ == "__main__":
    main()