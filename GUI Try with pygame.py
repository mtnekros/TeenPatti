import pygame

def update(dt):
	global x, y, vel, run

	pygame.time.delay(dt)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		x -= vel
	if keys[pygame.K_RIGHT]:
		x += vel
	if keys[pygame.K_UP]:
		y -= vel
	if keys[pygame.K_DOWN]:
		y += vel	

def drawScreen():
	win.fill((100, 100, 100))
	pygame.draw.rect(win, (255, 0 ,0), (x, y, width, height))
	pygame.display.update() 


# main execution starts here

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

# variables
x = 50
y = 50
width = 40
height = 60
vel = 2

run = True
while run:
	update(30)
	drawScreen()
pygame.quit()