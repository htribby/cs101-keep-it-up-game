#import and initialize pygame
import pygame
pygame.init()

#set up clock to limit how many times loop is run per second
clock = pygame.time.Clock()
#colors used in game
black = (0,0,0)
white = (255, 255, 255)

#create window for game
window = pygame.display.set_mode((800,800))
pygame.display.set_caption('Pong')
window.fill(black)

#create ball
ball = pygame.Rect(385, 385, 30, 30)

#create player
player = pygame.Rect(300, 750, 200, 20)

#create loop for game
while True:
    #handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #draw visuals
    pygame.draw.ellipse(window, white, ball)
    pygame.draw.rect(window, white, player)
    #update window
    pygame.display.flip()
    #loop runs 60 times per second
    clock.tick(60)