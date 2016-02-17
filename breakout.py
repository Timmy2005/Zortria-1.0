import pygame, sys
from pygame.locals import *

pygame.init()

APP_NAME         = 'Breakout 2014'
SCREEN_WIDTH     = 640
SCREEN_HEIGHT    = 420
BACKGROUND_COLOR = (0, 0, 0)
UP               = 1
DOWN             = -1
PADDLE_TOP       = 378               # Verified from wikipedia image
PADDLE_WIDTH     = 63                # Verified from wikipedia image
PADDLE_HEIGHT    = 8
PADDLE_COLOR     = (200, 72, 72)
PADDLE_SPEED     = 14
BALL_COLOR       = (200, 72, 72)
BALL_SIZE        = 10
INIT_BALL_SPEED  = 10
BRICK_HEIGHT       = 10
BRICK_WIDTH        = 40
NUM_ROWS           = 5
NUM_BRICKS_PER_ROW = 20
BRICK_ROW_COLORS   = [(200, 72, 72), (198, 108, 58), (180, 122, 48), (162, 162, 42), (72, 160, 72), (66, 72, 200)]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(APP_NAME)

# Initialize starting position of paddle to center of screen
xPaddle = SCREEN_WIDTH/2 - PADDLE_WIDTH/2
xBall = SCREEN_WIDTH/2 - BALL_SIZE/2
yBall = PADDLE_TOP - BALL_SIZE

while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        xPaddle -= PADDLE_SPEED
        if xPaddle < 0:
            xPaddle = 0
    if keys[pygame.K_RIGHT]:
        xPaddle += PADDLE_SPEED
        if xPaddle + PADDLE_WIDTH > SCREEN_WIDTH:
            xPaddle = SCREEN_WIDTH - PADDLE_WIDTH
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    
    screen.fill(BACKGROUND_COLOR)      
    pygame.draw.rect(screen, PADDLE_COLOR, (xPaddle, PADDLE_TOP, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, PADDLE_COLOR, (xBall, yBall), BALL_SIZE)
    pygame.draw.rect(screen, BRICK_ROW_COLORS[0], (0, 200, 50, 20))
    pygame.display.update()
