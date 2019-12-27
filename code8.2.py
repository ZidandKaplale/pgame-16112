# Simpan dengan nama : code82.py
# Pemrograman Game Praktikum 8
# latihan code 8.2 : PyGame
import pygame

pygame.init()
screen = pygame.display.set_caption("640, 480")
clock = pygame.time.Clock()
done = False

warna_font = (233, 225, 0)
warna_bg_font = (0, 2, 225)
warna_bg = (255, 55, 255)

font = pygame.font.SysFont("comicsansms", 72)

text = font.render("Hello, World", True,warna_font, warna_bg_font)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			done = True

	screen.fill(warna_bg)
	screen.blit(text, (220 - text.get_width() //2, 200))
	screen.blit(textx, (220 - text.get_width() //2, 150))
	screen.blit(text1, (220 - text.get_width() //2, 50))
	pygame.display.flip()
	clock.tick(60)