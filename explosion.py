import pygame
import sys

pygame.init()
pygame.mixer.init()

white = (255, 255, 255)

width, height = 600, 450

window = pygame.display.set_mode((width, height))

pygame.display.set_caption('Explosion')

fps = 60

clock = pygame.time.Clock()

fire_width = 300
fire_height = 300

fire_x = 150
fire_y = 80

fire = []
fire_index = 0
fire_counter = 0
fire_cooldown = 5

for i in range(1, 25):
	fire_img = pygame.image.load(f'sprites/fire_{i}.png')
	fire_img = pygame.transform.scale(fire_img, (fire_width, fire_height))
	fire.append(fire_img)

def explode():
	pygame.mixer.music.load('audio/explosion.wav')
	pygame.mixer.music.play()


def draw_fire():
	window.blit(fire[fire_index], (fire_x, fire_y))

explode()
while True:
	clock.tick(fps)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	window.fill(white)
	draw_fire()

	if fire_counter > fire_cooldown:
		if fire_index >= len(fire) - 1:
			explode()
			fire_index = 0

		fire_index += 1
		fire_counter = 0

	fire_counter += 1
	pygame.display.update()