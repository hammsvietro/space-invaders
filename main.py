import pygame

#Initialize pygame module
pygame.init()

#Create screen with 800x600 size
width = 800
height = 600

screen = pygame.display.set_mode((width,height))

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("images/spaceship.png")
playerX = width/2 - 32
playerY = 480
playerX_changer = 0
playerY_changer = 0

def player(x,y):
    screen.blit(playerImg, (x, y))


# Game Loop
running = True
while running:

    # RGB Background
    screen.fill((0,0,0))


    for event in pygame.event.get():

        # Keyboard Listener
        if event.type == pygame.QUIT:
            running = False

        # When Any Key is Pressed
        if event.type == pygame.KEYDOWN:

            # When Left Arrow is pressed
            if event.key == pygame.K_LEFT:
                playerX_changer = -0.2

            # When Right Arrow is pressed
            if event.key == pygame.K_RIGHT:
                playerX_changer = 0.2

            # When Up Arrow is Pressed
            if event.key == pygame.K_UP:
                playerY_changer = -0.2

            if event.key == pygame.K_DOWN:
                playerY_changer = 0.2

        # When Any Key is Unpressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_changer=0

            if event.key == pygame.K_UP or pygame.K_DOWN:
                playerY_changer = 0



    playerX += playerX_changer
    playerY += playerY_changer
    player(playerX,playerY)
    pygame.display.update()
