import pygame, sys, random

# display screen set up
screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
screen_surf = pygame.Surface((1000,500))
screen_rect = screen_surf.get_rect(center=(500,250))

# sprite generation
player1 = pygame.Surface((10,80))
player1.fill("White")
player1_rect = player1.get_rect(center=(20,250))

player2 = pygame.Surface((10,80))
player2.fill("White")
player2_rect = player2.get_rect(center=(980,250))

ball = pygame.Surface((10,10))
ball.fill("White")
ball_rect = ball.get_rect(center=(500,250))
x_speed, y_speed = random.choice([1,(-1)]), random.choice([1,(-1)])

# game loop
while True:

    # for event in events
    for event in pygame.event.get():
        # close if event == "x" 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # blits
    screen.blit(screen_surf,screen_rect)
    screen.blit(player1,player1_rect)
    screen.blit(player2,player2_rect)
    screen.blit(ball,ball_rect)

    # paddle movement logic
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_DOWN] and player2_rect.centery < 450:
        player2_rect.centery += 4
    elif keys_pressed[pygame.K_UP] and player2_rect.centery > 50:
        player2_rect.centery -= 4
    if keys_pressed[pygame.K_s] and player1_rect.centery < 450:
        player1_rect.centery += 4
    elif keys_pressed[pygame.K_w] and player1_rect.centery > 50:
        player1_rect.centery -= 4

    # ball movement logic
    if ball_rect.y > 490:
        y_speed = -1
    elif ball_rect.y < 10:
        y_speed = 1
    if ball_rect.colliderect(player2_rect):
        x_speed = -1
    elif ball_rect.colliderect(player1_rect):
        x_speed = 1
    ball_rect.x += x_speed * 5
    ball_rect.y += y_speed * 5

    # winner_logic
    if ball_rect.x > 990:
        print("player1 wins")
    elif ball_rect.x < 10:
        print("player2 wins")
        
    # update the screen 60fps
    pygame.display.update()
    clock.tick(60)
