import pygame
import os

pygame.init()

# declaring the screen height and width
screenWidth = 1000
screenHeight = 700

# creating the Game Window (Canvas)
canvas = pygame.display.set_mode( (screenWidth, screenHeight) )


# Name of the Window
pygame.display.set_caption("Car Game")

# loading the background image
bgs = [pygame.image.load(os.path.join("Images", "bg0.png")),
       pygame.image.load(os.path.join("Images", "bg5.png"))]
genre = 0

# loading the car image
cars = [pygame.image.load(os.path.join("Images","yellowCar.png")),
        pygame.image.load(os.path.join("Images","blackCar.png")),
        pygame.image.load(os.path.join("Images","whiteCar.png"))
        ]

car = 0

# loading enemies pics
enemies = [pygame.image.load(os.path.join("Images","enemy1.png"))]

# loading obstacle cars on the road
obsCars = [pygame.image.load(os.path.join("Images", "obsCar1.png")),
           pygame.image.load(os.path.join("Images", "obsCar2.png"))]


class Beginning(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.begun = False
        
        
    
    def draw(self, canvas):
        canvas.blit(bgs[genre], (self.x, self.y))
        
        

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
        self.vel = 8
        self.brk = 5
    
    # a function to draw everything related to the player Car
    def draw(self, canvas):
        canvas.blit(cars[car], (self.x, self.y))
    
    
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
        self.rightBorder = screenWidth // 4.5 * 3 + 100
    
# a class for enemy N1
class Enemy1(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    # a function to draw the enemy
    def draw(self, canvas):
        canvas.blit(enemies[0], (self.x, self.y))
    
# a class for enemy N2
class Enemy2(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    # a function to draw the enemy
    def draw(self, canvas):
        canvas.blit(enemies[0], (self.x, self.y))
    
# a class for enemy N3
class Enemy3(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    # a function to draw the enemy
    def draw(self, canvas):
        canvas.blit(enemies[0], (self.x, self.y))
    
# a class for enemy N4
class Enemy4(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    # a function to draw the enemy
    def draw(self, canvas):
        canvas.blit(enemies[0], (self.x, self.y))
    
# a class for enemy N5
class Enemy5(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    # a function to draw the enemy
    def draw(self, canvas):
        canvas.blit(enemies[0], (self.x, self.y))
    
# a class for obstacle car
class Obstable1(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    # a function to draw the obstacle car
    def draw(self, canvas):
        canvas.blit(obsCars[0], (self.x, self.y))
    
# a class for obstacle car
class Obstable2(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    # a function to draw the obstacle car
    def draw(self, canvas):
        canvas.blit(obsCars[1], (self.x, self.y))
        
# a class to make the enemies shot bullets
class Bullets(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        
# a class to make the road moving
class MovingRoad(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 30
        
    def draw(self, canvas):
        self.y = self.y + self.speed

        if self.y == self.height:
            self.y = 0
        
        canvas.blit(bgs[genre], [self.x, self.y - self.height])
        canvas.blit(bgs[genre], [self.x, self.y])
            
        
# class for beginning page
beginning = Beginning(0, 0, screenWidth, screenHeight)

# moving road
movingRoad = MovingRoad(0, 0, 1500, 900)

# making instances of the classes 
player = Player(700, 700, 120, 120)
highway = Highway(screenWidth, screenHeight)

# making instances of enemies
enemy1 = Enemy1(40, 10, 270, 240)
enemy2 = Enemy2(40, 300, 270, 240)
enemy3 = Enemy3(40, 600, 270, 240)
enemy4 = Enemy4(1200, 25, 270, 240)
enemy5 = Enemy5(1200, 400, 270, 240)

# making instances of obstable cars
obsCar1 = Obstable1(700, 350, 120, 120)
obsCar2 = Obstable2(400, 200, 120, 120)


# a function to redraw the Game Window 
def redrawCanvas():
    
    if beginning.begun == False:
        beginning.draw(canvas)
    
    if beginning.begun:
        #canvas.blit(bgs[genre], (0,0))
        movingRoad.draw(canvas)
        
        #canvas.blit(hPic, (highway.leftBorder, 0))
        player.draw(canvas)
        
        # drawing enemies
        enemy1.draw(canvas)
        enemy2.draw(canvas)
        enemy3.draw(canvas)
        enemy4.draw(canvas)
        enemy5.draw(canvas)
        
        # drawing obstacles
        obsCar1.draw(canvas)
        obsCar2.draw(canvas)
    
    
    # updating the display
    pygame.display.update()
        


# main loop
run = True
while run:
    #pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.key.key_code("y")]:
        beginning.begun = True
        car = 0
        genre = 1
    if keys[pygame.key.key_code("b")]:
        beginning.begun = True
        car = 1
        genre = 1
    if keys[pygame.key.key_code("w")]:
        beginning.begun = True
        car = 2
        genre = 1
        
    if keys[pygame.K_ESCAPE]:
        beginning.begun = False
        genre = 0
    
        
    if keys[pygame.K_LEFT] and player.x > highway.leftBorder:
        player.x -= player.vel
    if keys[pygame.K_RIGHT] and player.x < highway.rightBorder:
        player.x += player.vel
    if keys[pygame.K_UP] and player.y > player.vel:
        player.y -= player.vel
    if keys[pygame.K_DOWN] and player.y < (screenHeight -
                               player.height - player.vel - 30):
        player.y += player.brk 
        
        
    # calling a function to draw everything
    redrawCanvas()
    
            
pygame.quit()












