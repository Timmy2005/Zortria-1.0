import pygame, sys
import math
from pygame.locals import *

SCREEN_HIGHT	  = 420
SCREEN_WIDTH	  = 640
SCREEN_COLOR	  = (0,0,0)
SHAPE_COLOR  	  = (200,72,72)
FPS          	  = 30
MOVE         	  = 20
PADDLE_WIDTH      = 64
PADDLE_HIGHT   	  = 8
PADDLE_Y_AXIS     = 377
BRICK_HIGHT       = 12
BRICK_WIDTH       = 32
BRICK_X_AXIS      = [32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448, 480, 512, 544, 576]
BRICK_Y_AXIS      = [126, 138, 150, 162, 174, 186]
BALL_HIGHT        = 8
BALL_WIDTH        = 8
NUM_BRICKS_PER_ROW= 18 
NUM_COLUMS        = 6
UP                = -1
DOWN              = 1
LEFT              = -1
RIGHT             = 1
#BALL_RADIUS       = 5
BALL_THICKNESS    = 2
APP_NAME          = "Breakout"
DISPLAY           = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT),0,32)
BRICK_COLOR       = [(200, 72, 72), (198, 108, 58), (180, 122, 48), (162, 162, 42), (72, 160, 72), (66, 72, 200)]
FRAME_COLOR       = (142, 142, 142)
FRAME_HEIGHT      = 314
BOTTOM_COLOR      = [(66, 158, 130), (200, 72, 72)]
BOTTOM_X_AXIS     = 0
BOTTOM_Y_AXIS     = 377
BOTTOM_WIDTH      = 32
BOTTOM_HEIGHT     = 14
FRAME_WIDTH       = 32
FRAME_X_AXIS      = 0
FRAME_Y_AXIS      = 63
FRAME2_X_AXIS     = 608
BOTTOM2_X_AXIS    = 608
TOP_FRAME_Y_AXIS  = 30
TOP_FRAME_X_AXIS  = 0
TOP_FRAME_WIDTH   = 640
TOP_FRAME_HEIGHT  = 34

rectx = 283
circley = 260
circlex = 245
ballMove = 7
running = True
direction2 = LEFT
ballRadian = .9235
direction = UP
#brick_x = (BRICK_X_AXIS[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18] / 32)
#brick_y = (BICK_Y_AXIS[1],[2],[3],[4],[5],[6] - 114 / 12)

#BRICK + BALL

is_brick_visible = [[0 for x in xrange(NUM_BRICKS_PER_ROW)] for x in xrange(NUM_COLUMS)] 
for j in range(NUM_BRICKS_PER_ROW):
	for i in range(NUM_COLUMS):
		is_brick_visible[i][j] = True

def brick():
	for j in range(NUM_BRICKS_PER_ROW):
		for i in range(NUM_COLUMS):
			if is_brick_visible[i][j]:
				pygame.draw.rect(DISPLAY, BRICK_COLOR[i],(BRICK_X_AXIS[j], BRICK_Y_AXIS[i], BRICK_WIDTH, BRICK_HIGHT))

def detect_collision(circlex, circley):
	global is_brick_visible
	for i in range(0, NUM_BRICKS_PER_ROW):
		if circlex >= BRICK_X_AXIS[i] and circlex <= BRICK_X_AXIS[i] + BRICK_WIDTH:
			for j in range(0, NUM_COLUMS):
				if circley >= BRICK_Y_AXIS[j] and circley <= BRICK_Y_AXIS[j] + BRICK_HIGHT:
					direction = DOWN				
					
					
		if circley > BRICK_Y_AXIS[5] + BRICK_HIGHT-100:
			return True
		if circley > BRICK_Y_AXIS[0] + BRICK_HIGHT-100:
			return False
	else:
		if circley > BRICK_Y_AXIS[0] + BRICK_HIGHT-100:
			return False
		
		if circley > BRICK_Y_AXIS[5] + BRICK_HIGHT-100:
			return True
			
pygame.display.set_caption(APP_NAME)

fpsTime = pygame.time.Clock()
	
#PADDLE + BALL
	
while running:
	
	keys = pygame.key.get_pressed()
   	if keys[pygame.K_RIGHT]:
 		rectx += MOVE
	if keys[pygame.K_LEFT]:
		rectx -= MOVE
	if rectx > SCREEN_WIDTH - FRAME_WIDTH - PADDLE_WIDTH:
		rectx = SCREEN_WIDTH - FRAME_WIDTH - PADDLE_WIDTH
	if rectx < FRAME_WIDTH:
		rectx = FRAME_WIDTH
	if direction == DOWN:
		circlex = circlex - ballMove*math.cos(.100)
		circley = circley + direction*ballMove*math.sin(.9235)
	if direction == UP:
		circlex = circlex - ballMove*math.cos(.9235)
		circley = circley - direction*ballMove*math.sin(.9235)
	if direction2 == RIGHT:
		circlex = circlex + direction2*ballMove*math.cos(.1235)
		circley = circley - math.sin(.1235)
	if circley >= PADDLE_Y_AXIS and circley <= PADDLE_Y_AXIS + BALL_HIGHT:
		print"Hi"
		#if circlex + BALL_WIDTH >= rectx and circlex + PADDLE_WIDTH <= rectx + PADDLE_WIDTH:
		direction = DOWN
		#else:
		#	running = False

#BALL

	if circlex <= FRAME_WIDTH:
		if direction2 == LEFT:
			direction2 = RIGHT
			circlex = circlex + direction2*ballMove*math.cos(ballRadian)
			circley = circley - math.sin(ballRadian) 
	if circlex >= SCREEN_WIDTH - FRAME_WIDTH:
		if direction2 == RIGHT:
			direction2 = LEFT 
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

#BRICK + BALL
		
	DISPLAY.fill(SCREEN_COLOR)
	pygame.draw.rect(DISPLAY, BRICK_COLOR[0],(rectx, PADDLE_Y_AXIS, PADDLE_WIDTH, PADDLE_HIGHT))
	
	#if detect_collision(circlex, circley):	
	#	if direction == DOWN:
	#		direction = UP
	#		#is_brick_visible[brick_x][brick_y] = False
	#	if direction == UP:
	#		direction = DOWN
			#is_brick_visible[brick_x][brick_y] = False
		
	brick()		
	pygame.draw.rect(DISPLAY, SHAPE_COLOR,(circlex, circley, BALL_WIDTH, BALL_HIGHT))
	pygame.draw.rect(DISPLAY, FRAME_COLOR,(FRAME2_X_AXIS, FRAME_Y_AXIS, FRAME_WIDTH, FRAME_HEIGHT))
	pygame.draw.rect(DISPLAY, FRAME_COLOR,(FRAME_X_AXIS, FRAME_Y_AXIS, FRAME_WIDTH, FRAME_HEIGHT))
	pygame.draw.rect(DISPLAY, BOTTOM_COLOR[0],(BOTTOM_X_AXIS, BOTTOM_Y_AXIS, BOTTOM_WIDTH, BOTTOM_HEIGHT))
	pygame.draw.rect(DISPLAY, BOTTOM_COLOR[1],(BOTTOM2_X_AXIS, BOTTOM_Y_AXIS, BOTTOM_WIDTH, BOTTOM_HEIGHT))
	pygame.draw.rect(DISPLAY, FRAME_COLOR,(TOP_FRAME_X_AXIS, TOP_FRAME_Y_AXIS, TOP_FRAME_WIDTH, TOP_FRAME_HEIGHT))
	
	
	pygame.display.update()
	fpsTime.tick(FPS)