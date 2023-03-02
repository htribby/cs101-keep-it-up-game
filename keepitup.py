#import and initialize pygame and sys
import pygame, sys
pygame.init()

#set up clock to limit how many times loop is run per second
clock = pygame.time.Clock()
#colors used in game
black = (0,0,0)
white = (255, 255, 255)

#create window for game
window = pygame.display.set_mode((800,800))
pygame.display.set_caption('Pong')

#create ball
ball = pygame.Rect(385, 385, 30, 30)


#create player
player = pygame.Rect(300, 750, 200, 20)

ball_speed_x = 5
ball_speed_y = 5
#create loop for game
while True:
    #handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #make the ball move
    ball.x += ball_speed_x
    ball.y += ball_speed_y 
    
    #create boundaries for ball and make it "bounce" off walls
    if ball.top <= 0 or ball.bottom >= 800:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= 800:
        ball_speed_x *= -1

    #draw visuals
    window.fill(black)
    pygame.draw.ellipse(window, white, ball)
    pygame.draw.rect(window, white, player)

    #update window
    pygame.display.flip()
    #loop runs 60 times per second
    clock.tick(60)