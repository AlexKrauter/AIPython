import pygame

# pygame setup
pygame.init()
screen = pygame.display
screen = screen.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    #check if player is quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                print(pygame.display.is_fullscreen())
                if pygame.display.is_fullscreen() == True:
                    pygame.display.set_mode((1280, 720))
                else:
                    pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    
    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()