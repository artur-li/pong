import pygame, sys

# display screen set up
screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()

# sprite generation
player1 = pygame.Surface((20,100))
player1.fill("White")
player1_rect = player1.get_rect(center=(20,250))

player2 = pygame.Surface((20,100))
player2.fill("White")
player2_rect = player2.get_rect(center=(980,250))

ball = pygame.Surface((20,20))
ball.fill("White")
ball_rect = ball.get_rect(center=(500,250))

# game loop
while True:

    # for event in events
    for event in pygame.event.get():
        # close if event == "x" 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # display sprites to screen
    screen.blit(player1,player1_rect)
    screen.blit(player2,player2_rect)
    screen.blit(ball,ball_rect)

    # update the screen 60fps
    pygame.display.update()
    clock.tick(60)