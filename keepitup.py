#import and initialize pygame
import pygame
pygame.init()

#set up clock to limit how many times loop is run per second
clock = pygame.time.Clock()
#colors used in game
black = (0,0,0)
white = (255, 255, 255)

#create window for game
window = pygame.display.set_mode((700,700))
pygame.display.set_caption('Pong')
window.fill(black)

#create loop for game
while True:
    #handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #update window
    pygame.display.flip()
    #loop runs 60 times per second
    clock.tick(60)