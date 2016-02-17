import pygame, sys
from pygame.locals import *

DISPLAY=pygame.display.set_mode((500,400),0,32)
WHITE=(255,255,255)
blue=(225,255,0)
#FPS = 30				
move = 10
rectx = 10
#fpsTime = pygame.time.Clock() 
while True:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				rectx += move
			#if (event.key == K_RIGHT):
			#	rectx += move
			#if rectx < 0:
			#	rectx = 0
			#if rectx > 421:
			#	rectx = 421		 	
				
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		DISPLAY.fill(WHITE)
		pygame.draw.rect(DISPLAY,blue,(rectx,350,79,18))
		pygame.display.update()
		#fpsTime.tick(FPS)