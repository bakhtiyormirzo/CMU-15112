##########################
# Version 4.0

# Name: Bakhtiyorjon Mirzajonov
# Andrew ID: bmirzajo

##########################

##########################
# importing necessary libraries

import pygame
from pygame import mixer
import os
import random

##########################


pygame.init()


# declaring the screen height and width
screenWidth = 1000
screenHeight = 700


# creating the Game Window (Canvas)
canvas = pygame.display.set_mode( (screenWidth, screenHeight) )


# Name of the Window
pygame.display.set_caption("Car Game")

# loading the background image
# these background images are used to change the genre
# of the game to keep the player interested
bgs = [ pygame.image.load(os.path.join("Images", "bg0.png")),
        pygame.image.load(os.path.join("Images", "bg1.png")),
        pygame.image.load(os.path.join("Images", "bg2.png"))
        ]


# a variable used to keep track of beckground
# images of the beginning of the game
bg = 0


# these background images are used to change the genre
# of the game to keep the player interested
genres = [ pygame.image.load(os.path.join("Images", "bg3.png"))
        ]


# this variable is used to keep track of the sequence of
# the display that should be shown to a user at a certain time
genre = 0


# loading the car image
cars = [pygame.image.load(os.path.join("Images","yellowCar.png")),
        pygame.image.load(os.path.join("Images","blackCar.png")),
        pygame.image.load(os.path.join("Images","whiteCar.png"))
        ]

car = 0


# loading enemies pics
enemies = [pygame.image.load(os.path.join("Images","enemy1.png")),
           pygame.image.load(os.path.join("Images","enemy2.png"))
           ]

# loading obstacle cars on the road
obsCars = [pygame.image.load(os.path.join("Images", "obsCar1.png")),
           pygame.image.load(os.path.join("Images", "obsCar2.png"))]


# Starting the mixer
mixer.init()

# importing and playing the music
mixer.music.load( os.path.join("Sounds", "soundtrack.mp3") )
mixer.music.play(-1)


# this class is used for the initialization of the game
# it handles the introduction part of the game
class Beginning(object):
    
    def __init__(self, x, y, width, height):
        
        # x and y values are both 0 since these coordinates
        # are used to place the background image properly
        # the (0,0) is the starting position
        self.x = x
        self.y = y
        
        # width and height is the whole width and height of the canvas
        # again,the image has to cavor the game window fully
        self.width = width
        self.height = height
        
        # this variable is used to check if the player choose a car
        # and wants to start the game
        self.begun = False
        
    
    # this function draws the first background picture of the game
    def draw(self, canvas):
        canvas.blit(bgs[bg], (self.x, self.y))
        
        

# a class for genres of the game
class GenresForTheGame(object):
    def __init__(self, x, y, width, height):
        
        # the coordinates for the genres are the same
        # as the background images because they
        # will replace the background images
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    # a function to draw the genre of the game
    # it changes in every level of the game
    def draw(self, canvas):
        canvas.blit(genres[genre], (self.x, self.y))
        

# Player class, it takes the parameters of:
# x and y positions
# width and height of the object
class Player(object):
    def __init__(self, x, y, width, height):
        
        # these variables define the starting
        # position of the player 1
        self.x = x
        self.y = y
        
        # the scale of the player 1
        self.width = width
        self.height = height
        
        # variables for the forward velocity
        # and the backward velocity
        self.vel = 1.5
        self.brk = 1
    
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
        self.leftBorder = screenWidth // 4.2
        self.rightBorder = screenWidth // 4.5 * 3 + 35
    
# a class for enemy N1
class Enemy1(object):
    def __init__(self, x, y, width, height):
        
        # coordinates and scales of the enemy 1
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # variables for its bullets
        self.color = (255,0,0)
        self.radius = 10
    
    # a function to draw the enemy
    def draw(self, canvas):
        canvas.blit(enemies[0], (self.x, self.y))
    
# a class for enemy N2
class Enemy2(object):
    def __init__(self, x, y, width, height):
        
        # coordinates and scales of the enemy 2
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # variables for its bullets
        self.color = (255,0,0)
        self.radius = 10
    
    # a function to draw the enemy
    def draw(self, canvas):
        canvas.blit(enemies[0], (self.x, self.y))
    
# a class for enemy N3
class Enemy3(object):
    def __init__(self, x, y, width, height):
        
        # coordinates and scales of the enemy 3
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # variables for its bullets
        self.color = (255,0,0)
        self.radius = 10
    
    # a function to draw the enemy
    def draw(self, canvas):
        canvas.blit(enemies[0], (self.x, self.y))
    
# a class for enemy N4
class Enemy4(object):
    def __init__(self, x, y, width, height):
        
        # coordinates and scales of the enemy 4
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # variables for its bullets
        self.color = (255,0,0)
        self.radius = 10
    
    # a function to draw the enemy
    def draw(self, canvas):
        canvas.blit(enemies[1], (self.x, self.y))
    
# a class for enemy N5
class Enemy5(object):
    def __init__(self, x, y, width, height):
        
        # coordinates and scales of the enemy 5
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # variables for its bullets
        self.color = (255,0,0)
        self.radius = 10
    
    # a function to draw the enemy
    def draw(self, canvas):
        canvas.blit(enemies[1], (self.x, self.y))
    
    
# a class for obstacle car
class Obstable1(object):
    def __init__(self, x, y, width, height, leftBorder, rightBorder):
        
        # coordinates and scales of the obstacle car 1
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # border of the road
        self.rightBorder = rightBorder
        self.leftBorder = leftBorder
        
        # the speed at which the obstacle car moves
        self.speed = 2
    
    # a function to draw the obstacle car
    def draw(self, canvas):
        # adding the speed int to the y coordinate of the picture
        self.y = self.y + self.speed
         
        # when the obstacle car reaches the bottom of the screen
        # we randomly select a new x position between the borders
        # of the road and we set the y position to a negative number
        # so that it does not pop up on the screen,
        # rather it smoothly appears on the scree
        if self.y > screenHeight:
            self.x = random.randrange(self.leftBorder, self.rightBorder)
            self.y = -50
            
        canvas.blit(obsCars[0], [self.x, self.y])
    
    
# a class for obstacle car
class Obstable2(object):
    def __init__(self, x, y, width, height, leftBorder, rightBorder):
        
        # coordinates and scales of the obstacle car 2
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # border of the road
        self.rightBorder = rightBorder
        self.leftBorder = leftBorder
        
        # the speed at which the obstacle car moves
        self.speed = 2
    
    # a function to draw the obstacle car
    def draw(self, canvas):
        # adding the speed int to the y coordinate of the picture
        self.y = self.y + self.speed
         
        # when the obstacle car reaches the bottom of the screen
        # we randomly select a new x position between the borders
        # of the road and we set the y position to a negative number
        # so that it does not pop up on the screen,
        # rather it smoothly appears on the scree
        if self.y > screenHeight:
            self.x = random.randrange(self.leftBorder, self.rightBorder)
            self.y = -50
            
        canvas.blit(obsCars[1], [self.x, self.y])
        
        
        
# a class to make the enemy1 shot bullets
class Bullet1(object):
    def __init__(self, x, y, radius, color):
        
        # coordinates and radius of bullet1
        self.x = x
        self.y = y
        self.radius = radius
        
        # color of the bullet
        self.color = color
        
    def draw(self, canvas):
        pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
        
        
# a class to make the enemy2 shot bullets
class Bullet2(object):
    def __init__(self, x, y, radius, color):
        
        # coordinates and radius of bullet2
        self.x = x
        self.y = y
        self.radius = radius
        
        # color of the bullet
        self.color = color
        
    def draw(self, canvas):
        pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
        
        
# a class to make the enemy3 shot bullets
class Bullet3(object):
    def __init__(self, x, y, radius, color):
        
        # coordinates and radius of bullet 3
        self.x = x
        self.y = y
        self.radius = radius
        
        # color of the bullet
        self.color = color
        
    def draw(self, canvas):
        pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
        
# a class to make the enemy4 shot bullets
class Bullet4(object):
    def __init__(self, x, y, radius, color):
        
        # coordinates and radius of bullet 4
        self.x = x
        self.y = y
        self.radius = radius
        
        # color of the bullet
        self.color = color
        
    def draw(self, canvas):
        pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
        
# a class to make the enemy5 shot bullets
class Bullet5(object):
    def __init__(self, x, y, radius, color):
        
        # coordinates and radius of bullet 5
        self.x = x
        self.y = y
        self.radius = radius
        
        # color of the bullet
        self.color = color
        
    def draw(self, canvas):
        pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
        
        
        
# a class to make the road moving
class MovingRoad(object):
    def __init__(self, x, y, width, height):
        
        # coordinates of the background picture
        self.x = x
        self.y = y
        
        # the width and height of the picture
        # this is basically the width and height of the screen
        self.width = width
        self.height = height
        
        # the speed at which the picture is moving
        self.speed = 10
        
    def draw(self, canvas):
        
        # adding the speed int to the y coordinate of the picture
        self.y = self.y + self.speed
         
        # when the y coordinate reaches the height of the screen
        # we reset the y to 0 to start over
        # this way, our y variable will keep changing all the time
        if self.y == self.height:
            self.y = 0
        
        
        # these two lines of code will draw one image in two different
        # scales
        # this way the cars will seem like they are moving
        # but actually, the road is moving
        canvas.blit(genres[genre], [self.x, self.y - self.height])
        canvas.blit(genres[genre], [self.x, self.y])
        
            
# a class for enemy1 positions
# and bullet starting points
class PositionE1(object):
    def __init__(self):
        self.x = 40
        self.y = 10
        self.width = 270
        self.height = 240
        
        
# a class for enemy2 positions
# and bullet starting points
class PositionE2(object):
    def __init__(self):
        self.x = 40
        self.y = 300
        self.width = 270
        self.height = 240
        
        
# a class for enemy3 positions
# and bullet starting points
class PositionE3(object):
    def __init__(self):
        self.x = 40
        self.y = 600
        self.width = 270
        self.height = 240
        
        
# a class for enemy4 positions
# and bullet starting points
class PositionE4(object):
    def __init__(self):
        self.x = 850
        self.y = 25
        self.width = 270
        self.height = 240
        
        
# a class for enemy5 positions
# and bullet starting points
class PositionE5(object):
    def __init__(self):
        self.x = 850
        self.y = 400
        self.width = 270
        self.height = 240
        
        
# a class for the positions of the obstacle cars
# they change their positions throughout the game
# so that these classes keep track of their positions
# each obstacle car requires seperate class

# obstacle car 1
class PositionO1(object):
    def __init__(self):
        self.x = 700
        self.y = 200
        self.width = 120
        self.height = 120
        
        
# obstacle car 1
class PositionO2(object):
    def __init__(self):
        self.x = 400
        self.y = 0
        self.width = 120
        self.height = 120


# class for beginning page
beginning = Beginning(0, 0, screenWidth, screenHeight)


# making instance of Genres class
genresClass = GenresForTheGame(0, 0, screenWidth, screenHeight)


# moving road
movingRoad = MovingRoad(0, 0, screenWidth, screenHeight)


# making instances of the classes 
player = Player(500, 500, 120, 120)
highway = Highway(screenWidth, screenHeight)



# making instances of Position classes
# these are mainly used for positions of
# the eneies and the starting points
# of the bullets they will be shooting
positionE1 = PositionE1()
positionE2 = PositionE2()
positionE3 = PositionE3()
positionE4 = PositionE4()
positionE5 = PositionE5()



# making instances of enemies
enemy1 = Enemy1(positionE1.x, positionE1.y,
                positionE1.width, positionE1.height)

enemy2 = Enemy2(positionE2.x, positionE2.y,
                positionE2.width, positionE2.height)

enemy3 = Enemy3(positionE3.x, positionE3.y,
                positionE3.width, positionE3.height)

enemy4 = Enemy4(positionE4.x, positionE4.y,
                positionE4.width, positionE4.height)

enemy5 = Enemy5(positionE5.x, positionE5.y,
                positionE5.width, positionE5.height)


# making instances of obstacle cars positions
positionO1 = PositionO1()
positionO2 = PositionO2()

# making instances of obstable cars
obsCar1 = Obstable1( positionO1.x, positionO1.y,
                     positionO1.width, positionO1.height,
                     highway.leftBorder, highway.rightBorder
                     )

obsCar2 = Obstable2( positionO2.x, positionO2.y,
                     positionO2.width, positionO2.height,
                     highway.leftBorder, highway.rightBorder
                     )


# making instances of bullet classes to draw shots
bullet1 = Bullet1( positionE1.x + (positionE1.width // 4),
                   positionE1.y + (positionE1.height // 4),
                   enemy1.radius, enemy1.color
                   )

bullet2 = Bullet1( positionE2.x + (positionE2.width // 4),
                   positionE2.y + (positionE2.height // 4),
                   enemy2.radius, enemy2.color
                   )

bullet3 = Bullet1( positionE3.x + (positionE3.width // 4),
                   positionE3.y + (positionE3.height // 4),
                   enemy3.radius, enemy3.color
                   )

bullet4 = Bullet1( positionE4.x + (positionE4.width // 4),
                   positionE4.y + (positionE4.height // 4),
                   enemy4.radius, enemy4.color
                   )

bullet5 = Bullet1( positionE5.x + (positionE5.width // 4),
                   positionE5.y + (positionE5.height // 4),
                   enemy5.radius, enemy5.color
                   )


# a function to redraw the Game Window 
def redrawCanvas():
    
    
    # this draws the background of the game
    # when you run the program
    if beginning.begun == False:
        beginning.draw(canvas)
        

    # when a player chooses a car and starts the game
    # this will run and draws everything needed 
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
        
        # drawing the bullets
        bullet1.draw(canvas)
        bullet2.draw(canvas)
        bullet3.draw(canvas)
        bullet4.draw(canvas)
        bullet5.draw(canvas)
    
    
    # updating the display
    pygame.display.update()
        


# main loop
running = True
while running:
    
    # handles when the player presses quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # gets all the keys pressed into a list
    keys = pygame.key.get_pressed()
    
    
    
    if keys[pygame.K_KP_ENTER]:
        bg = 2
            
    # pressing space shows the car selection window to the player
    if keys[pygame.key.key_code("space")]:
        bg = 2
    
    
    # this is how a player chooses the car he wants to play with
    if keys[pygame.key.key_code("y")]:
        
        # starting the game
        beginning.begun = True
        
        # selecting the car from a list of loaded images of cars
        car = 0
        
    if keys[pygame.key.key_code("b")]:
        
        # starting the game
        beginning.begun = True
        
        # selecting the car from a list of loaded images of cars
        car = 1
        
    if keys[pygame.key.key_code("w")]:
        
        # starting the game
        beginning.begun = True
        
        # selecting the car from a list of loaded images of cars
        car = 2
        
        
    # by pressing Excape, a player is given an option to restart the game
    # it directs the user to a car selection window
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












