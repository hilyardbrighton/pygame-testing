import sys, pygame

# initialize pygame's modules
pygame.init()

# create Surface object which represents
# the monitor itself.
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

# set the speed in coordinates
speed = [2,2]

# set the color in rgb value
black = 0,0,0

# create another Surface object representing
# the pixels in the ball image.
ball = pygame.image.load("./media/intro_ball.gif")


# create a rectangular area representing
# the ball's image (Rect object).
# as far as i can tell, this is used to make
# coordinates easier.
ballrect = ball.get_rect()


# event loop
running = True
while running:
    
    # check for pygame-related event switches
    for event in pygame.event.get():
        
        # if quit is called through alt f4 or similar
        # exit the loop
        if event.type == pygame.QUIT:
            running = False
            
    #print(f"Left: {ballrect.left} Right: {ballrect.right} All: {ballrect}")
    
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
            
    # move ballrect by defined speed
    ballrect = ballrect.move(speed)
    
    # resets the Surface by filling it completely
    # so that the ball is not displayed with a trail
    screen.fill(black)
    
    # places the ball onto the screen
    # arguments: Surface object, position to place
    # the item
    screen.blit(ball, ballrect)
    
    
    pygame.display.flip()
    
            
            
# quit pygame
pygame.quit()


