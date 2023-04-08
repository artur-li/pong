import pygame, sys

# display screen set up
pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()


# game loop
while True:

    # for event in events
    for event in pygame.event.get():
        # close if event == "x" 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

