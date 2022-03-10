import pygame

#constants
background_colour = (0, 0, 0)
(screen_width, screen_height) = (1000, 600)

FPS = 60
clock = pygame.time.Clock()

#screen_prperties
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('HackTues')

#classes
class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height):
		img = pygame.image.load("assets/images/player.png")
		self.image = pygame.transform.scale(img, (width, height))
		self.rect = pygame.Rect(x, y, width, height)
		self.direction = "R"

	def walk(self, player_stages : list)

	def animation(self, moving_left, moving_right, moving_up, moving_down):
		do_walk = 0

		if moving_left:
			self.direction = "L"
			do_walk = 1

		if moving_right:
			self.direction = "R"
			do_walk = 1

		if moving_up:
			self.dircetion = "U"
			do_walk = 1

		if moving_down:
			self.direction = "D"
			do_walk = 1

		if do_walk:
			self.walk()
	def draw(self):
		
		if self.direction == "L":
			self.image = pygame.transform.flip(self.image, True, False)
			screen.blit(self.image, (self.rect.x, self.rect.y))

#definition of player
player = Player(100, 100, 50, 50)

#functions
def main():
	running = True

	while running:
		clock.tick(FPS)
		draw()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		key_pressed = pygame.key.get_pressed()

		if key_pressed[pygame.K_a]:
			moving_left = True
		else:
			moving_left = False

		if key_pressed[pygame.K_d]:
			moving_right = True
		else:
			moving_right = False

		player.move(moving_left, moving_right)

		pygame.display.update()

	pygame.quit()

def draw():
	screen.fill(background_colour)
	player.draw() 

#random_shit
if __name__ == "__main__":
  	main()