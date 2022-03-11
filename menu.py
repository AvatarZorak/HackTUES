from sys import exit
import pygame

pygame.init()

screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/menu_background.png"), (screen_width, screen_height)), (0, 0))

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

play_button = Button(screen_width/2 - 50, screen_height/2, "assets/images/buttons/play_button")
quit_button = Button(screen_width/2 - 50, screen_height/2+100, "assets/images/buttons/quit_button")

def menu():
    mouse = pygame.mouse.get_pos()
    
    screen.blit(pygame.transform.scale(pygame.image.load("assets/images/backgrounds/menu_background.png"), (screen_width, screen_height)), (0, 0))
    screen.blit(pygame.transform.scale(pygame.image.load("assets/images/game_name.png"), (screen_width/2 - 180, screen_height/2 - 180)), (420, 180))
    play_button.change_button()
    quit_button.change_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.check_clicked():
                return False

            if quit_button.check_clicked():
                exit(0)
    pygame.display.update()
    return True