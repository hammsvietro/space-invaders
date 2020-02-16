import pygame
import random

# Initialize pygame module
pygame.init()

# Create screen with 800x600 size
width = 800
height = 600

screen = pygame.display.set_mode((width,height))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("images/spaceship.png")
playerX = width/2 - 32
playerY = (3*height)/4-32
playerX_changer = 0
playerY_changer = 0

# Enemy
enemyImg = pygame.image.load("images/alien.png")
enemyX = random.randint(32,width-32)
enemyY = random.randint(32,height/2-32)
enemyX_changer = 0.18
enemyY_changer = 30

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))

# Game Loop
running = True
while running:

    # RGB Background
    screen.fill((255,255,255))


    for event in pygame.event.get():

        # Keyboard Listener
        if event.type == pygame.QUIT:
            running = False

        # When Any Key is Pressed
        if event.type == pygame.KEYDOWN:

            # When Left Arrow is Pressed
            if event.key == pygame.K_LEFT:
                playerX_changer += -0.2

            # When Right Arrow is Pressed
            if event.key == pygame.K_RIGHT:
                playerX_changer += 0.2

            # When Up Arrow is Pressed
            if event.key == pygame.K_UP:
                playerY_changer += -0.2
            # When  Down Arrow is Pressed
            if event.key == pygame.K_DOWN:
                playerY_changer += 0.2

        # When Any Key is Unpressed
        if event.type == pygame.KEYUP:
            # When Left Arrow is Unpressed
            if event.key == pygame.K_LEFT:
                playerX_changer += 0.2

            # When Right Arrow is Unpressed
            if event.key == pygame.K_RIGHT:
                playerX_changer += -0.2

            # When Up Arrow is Unpressed
            if event.key == pygame.K_UP:
                playerY_changer += 0.2
            # When  Down Arrow is Unpressed
            if event.key == pygame.K_DOWN:
                playerY_changer += -0.2
#

# Movement Control:

    playerX += playerX_changer

    # X Boundary Control
    if playerX <= 0:
        playerX = 0
    elif playerX > width-64:
        playerX = width-64

    playerY += playerY_changer

    # Y Boundary Control
    if playerY <= 0:
        playerY = 0
    elif playerY > height-64:
        playerY = height-64

    enemyX += enemyX_changer

    if enemyX <= 0:
        enemyX_changer = 0.18
        enemyX=0
        enemyY+=enemyY_changer

    elif enemyX > width - 64:
        enemyX_changer = -0.18
        enemyX = width-64
        enemyY+=enemyY_changer

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
