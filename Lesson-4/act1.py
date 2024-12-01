import pygame
icon = pygame.image.load("C:\\Users\\Cliff Krauter\\AIPython\\Lesson-4\\icon.png")

# pygame setup
pygame.init()
screen = pygame.display
screen.set_caption("Tic-Tac-Toe")
screen.set_icon(icon)
screen = screen.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

Tiles = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

while running:
    # check if player is inputting something
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                # print(pygame.display.is_fullscreen())
                if pygame.display.is_fullscreen() == True:
                    screen = pygame.display.set_mode((1280, 720))
                else:
                    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    
    #pygame.mouse.set_pos((pygame.mouse.get_pos()[0]-1,pygame.mouse.get_pos()[1])) (something i figured out)
    # render game
    screen.fill("skyblue")
    ws = pygame.display.get_window_size()
    pygame.draw.rect(screen, "white", pygame.Rect(max(ws[0],ws[1])-min(ws[0],ws[1]),30,min(ws[0],ws[1]),min(ws[0],ws[1])-60))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()