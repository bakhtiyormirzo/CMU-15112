import pygame
pygame.init()

# declaring the screen height and width
screenWidth = 1500
screenHeight = 900

# creating the Game Window (Canvas)
canvas = pygame.display.set_mode( (screenWidth, screenHeight) )

# Name of the Window
pygame.display.set_caption("Car Game")

# Pictures used in the game
hPic = pygame.image.load("highway.png")
bg = pygame.image.load("bg-desert.png")
car = pygame.image.load("Car.png")


# Player class, it takes the parameters of:
# x and y positions
# width and height of the object
class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # variables for the forward velocity
        # and the backward velocity
        self.vel = 10
        self.brk = 5
    
    # a function to draw everything related to the player Car
    def drawAll(self, canvas):
        canvas.blit(car, (self.x, self.y))
    
    
# class for the Highway
# it takes the whole screenWidth and
# sceenHeight as a parameter
class Highway(object):
    def __init__(self, screenWidth, screenHeight):
        self.screenWidth = screenWidth
        self.ScreenHeight = screenHeight
        
        # left and right borders of the highway
        # they are used to declare to limit
        # the cra's movement on the canvas
        self.leftBorder = screenWidth // 4.5
        self.rightBorder = screenWidth // 4.5 * 3 + 50
    
    
    
# making instances of the classes 
player = Player(700, 700, 120, 120)
highway = Highway(screenWidth, screenHeight)


# a function to redraw the Game Window 
def redrawCanvas():
    canvas.blit(bg, (0,0))
    canvas.blit(hPic, (highway.leftBorder, 0))
    player.drawAll(canvas)
    
    pygame.display.update()
        



# main loop
run = True
while run:
    #pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player.x > highway.leftBorder:
        player.x -= player.vel
    if keys[pygame.K_RIGHT] and player.x < highway.rightBorder:
        player.x += player.vel
    if keys[pygame.K_UP] and player.y > player.vel:
        player.y -= player.vel
    if keys[pygame.K_DOWN] and player.y < (screenHeight - player.height - player.vel - 30):
        player.y += player.brk 
        
        
    
    redrawCanvas()
    
            
pygame.quit()












