mport pygame, sys, random
pygame.init()

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

font = pygame.font.Font(None, 50)

player1_w_surf = font.render("Player 1 wins!", False, "White")
player1_w_rect = player1_w_surf.get_rect(midbottom=(500,240))

player2_w_surf = font.render("Player 2 wins!", False, "White")
player2_w_rect = player2_w_surf.get_rect(midbottom=(500,240))

play_again_surf = font.render("Play Again", False, "Blue")
play_again_rect = play_again_surf.get_rect(midtop=(500,260))

# in game control variables
game_active = True
player1_w = False
player2_w = False

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
    pygame.draw.line(screen, "white", (500,0), (500,500), 2)

    # game_active_state
    if game_active:

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
            game_active = False
            player1_w = True
        elif ball_rect.x < 10:
            game_active = False
            player2_w = True

    # player_1 win menu
    elif player1_w == True:
        screen.fill("black")
        screen.blit(player1_w_surf, player1_w_rect)
        screen.blit(play_again_surf, play_again_rect)
        mouse_pos = pygame.mouse.get_pos()
        if play_again_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed() != (False, False, False):
            player1_w = False
            game_active = True
            ball_rect.center=(500,250)

    
    # player_2 win menu
    elif player2_w == True:
        screen.fill("black")
        screen.blit(player2_w_surf, player2_w_rect)
        screen.blit(play_again_surf, play_again_rect)
        mouse_pos = pygame.mouse.get_pos()
        if play_again_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed() != (False, False, False):
            player2_w = False
            game_active = True
            ball_rect.center=(500,250)

    # update the screen 60fps
    pygame.display.update()
    clock.tick(60)
