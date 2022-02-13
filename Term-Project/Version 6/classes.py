# this file is a secondary file used as a starter file
# the file contains the images used in the game
# it also has all the classes created for the game



import pygame
import os
import random




pygame.init()




# declaring the screen height and width
screenWidth = 1000
screenHeight = 700





# loading the background image
# these background images are used to change the genre
# of the game to keep the player interested
bgs = [ pygame.image.load(os.path.join("Images", "bg0.png")),
        pygame.image.load(os.path.join("Images", "bg1.png")),
        pygame.image.load(os.path.join("Images", "bg2.png")),
        pygame.image.load(os.path.join("Images", "bg3.png"))
        ]

# bg3 is the loser background
# bg4 is the winner background

# a variable used to keep track of beckground
# images of the beginning of the game
bg = 0




# these background images are used to change the genre
# of the game to keep the player interested
genres = [ pygame.image.load(os.path.join("Images", "genre0.png")),
           pygame.image.load(os.path.join("Images", "genre1.png")),
         ]



# loading the car image
cars = [pygame.image.load(os.path.join("Images","yellowCar.png")),
        pygame.image.load(os.path.join("Images","blackCar.png")),
        pygame.image.load(os.path.join("Images","whiteCar.png"))
        ]

car = 0


# loading enemies pics
enemies = [pygame.image.load(os.path.join("Images","enemy0.png")),
           pygame.image.load(os.path.join("Images","enemy1.png")),
           pygame.image.load(os.path.join("Images","enemy2.png")),
           pygame.image.load(os.path.join("Images","enemy3.png"))
           ]




# loading obstacle cars on the road
obsCars = [pygame.image.load(os.path.join("Images", "obsCar1.png")),
           pygame.image.load(os.path.join("Images", "obsCar2.png"))]




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
        
        

class Ending(object):
    
    def __init__(self, x, y, width, height, player):
        
        
        self.player = player
        
        
        # x and y values are both 0 since these coordinates
        # are used to place the background image properly
        # the (0,0) is the starting position
        self.x = x
        self.y = y
        
        # width and height is the whole width and height of the canvas
        # again,the image has to cavor the game window fully
        self.width = width
        self.height = height
        
        
    
    # this function draws the first background picture of the game
    def draw(self, canvas):
        
        if self.player.won:
            canvas.blit(bgs[3], (self.x, self.y))
        
        elif self.player.alreadyLost:
            canvas.blit(bgs[2], (self.x, self.y))
        

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
        
        
        self.genre = 0
        
        
    # a function to draw the genre of the game
    # it changes in every level of the game
    def draw(self, canvas):
        canvas.blit(genres[self.genre], (self.x, self.y))
        



# Player class, it takes the parameters of:
# x and y positions
# width and height of the object
class Player(object):
    def __init__(self, x, y, width, height, beginning, genresClass,
        coin, obsCar1, obsCar2, bullet1, bullet2, bullet3, bullet4, bullet5):
        
        self.bullet1 = bullet1
        self.bullet2 = bullet2
        self.bullet3 = bullet3
        self.bullet4 = bullet4
        self.bullet5 = bullet5
        
        
        self.coin  = coin
        
        self.obscar1 = obsCar1
        self.obscar2 = obsCar2
        
        self.beginning = beginning
        self.genresClass = genresClass
        
        # these variables define the starting
        # position of the player 1
        self.x = x
        self.y = y
        
        # the scale of the player 1
        self.width = width
        self.height = height
        
        # variables for the forward velocity
        # and the backward velocity
        self.vel = 3
        self.brk = 1.5
        
        # defining the borders of the player as a rectangle
        # to detect if the player of hit by an enemy or
        # if there is a collision with cars
        self.border = self.x + self.vel, self.y, self.width-70, self.height-15
        self.green = (0, 255, 0)
        
        # colors for the text
        self.white = (0,0,0)
        
        # health points
        self.health = 10
        
        # score points
        self.score = 0
        
        
        # defining the font used to display the text
        self.font = pygame.font.Font("freesansbold.ttf", 36)
        
        # used to check if player has no health left
        self.alreadyLost = False
        
        self.won = False
        

    
    # a function to draw everything related to the player Car
    def draw(self, canvas):
        canvas.blit(cars[car], (self.x, self.y))
        
        self.border = (self.x + self.vel, self.y, self.width-70, self.height-15)
        
        
        
        healthText = self.font.render(f"Health: {self.health}", True, self.white)
        canvas.blit(healthText, (screenWidth//4, 50))
        
        scoreText = self.font.render(f"Score: {self.score}", True, self.white)
        canvas.blit(scoreText, (screenWidth//2, 50))
    
    
    
    def accident(self):
        
        if self.health > 0:
            
            self.health -= 1
            
            # resetting positions
            self.x = 500
            self.y = 500
            self.width = 120
            self.heaight =  120
                           
                           
            self.obscar1.hit1 = True
            self.obscar2.hit2 = True
            
        else:
            self.alreadyLost = True
            
            
            
    def gotCoin(self):
        
        self.coin.touch = True
        
        
        self.score += 1
        
        if self.score > 20:
            self.genresClass.genre = 1
            
        if self.score > 30:
            self.won = True
            
            
    def gotHit(self):
        
        self.bullet1.touch = True
        self.bullet2.touch = True
        self.bullet3.touch = True
        self.bullet4.touch = True
        self.bullet5.touch = True
        
        if self.health > 0:
            self.health -= 1
            
        else:
            self.alreadyLost = True
            
    def reset(self):
        self.alreadyLost = False
        self.won = False
        
        self.health = 10
        self.score = 0
        
    
    
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
    def __init__(self, x, y, width, height, genresClass):
        
        
        self.genresClass = genresClass
        
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
        if self.genresClass.genre == 0:
            canvas.blit(enemies[0], (self.x, self.y))
        else:
            canvas.blit(enemies[2], (self.x, self.y))
        
        
        
        
    
# a class for enemy N2
class Enemy2(object):
    def __init__(self, x, y, width, height, genresClass):
        
        
        self.genresClass = genresClass
        
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
        if self.genresClass.genre == 0:
            canvas.blit(enemies[0], (self.x, self.y))
        else:
            canvas.blit(enemies[3], (self.x, self.y))
    
    
    
    
# a class for enemy N3
class Enemy3(object):
    def __init__(self, x, y, width, height, genresClass):
        
        
        self.genresClass = genresClass
        
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
        if self.genresClass.genre == 0:
            canvas.blit(enemies[0], (self.x, self.y))
        else:
            canvas.blit(enemies[2], (self.x, self.y))
    
    
    
# a class for enemy N4
class Enemy4(object):
    def __init__(self, x, y, width, height, genresClass):
        
        self.genresClass = genresClass
        
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
        if self.genresClass.genre == 0:
            canvas.blit(enemies[1], (self.x, self.y))
        else:
            canvas.blit(enemies[3], (self.x, self.y))
    
    
    
# a class for enemy N5
class Enemy5(object):
    def __init__(self, x, y, width, height, genresClass):
        
        
        self.genresClass = genresClass
        
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
        if self.genresClass.genre == 0:
            canvas.blit(enemies[1], (self.x, self.y))
        else:
            canvas.blit(enemies[2], (self.x, self.y))
    
    
    
    
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
        
        
        # defining the borders of the player as a rectangle
        # to detect if the player of hit by an enemy or
        # if there is a collision with cars
        self.border = (self.x + self.speed, self.y, self.width-70, self.height-15)
        self.green = (0, 255, 0)
        
        self.hit1 = False
    
    
    
    # a function to draw the obstacle car
    def draw(self, canvas):
        
        if self.hit1:
            
            self.hit1 = False
            
            self.y = -50
            self.x = random.randrange(self.leftBorder, self.rightBorder)
            
            canvas.blit(obsCars[0], [self.x, self.y])
        
        else:
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
            
            
            self.border = self.x + self.speed, self.y, self.width-70, self.height-15
    
    
    
    
    
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
        self.speed = 3
        
        
        # defining the borders of the player as a rectangle
        # to detect if the player of hit by an enemy or
        # if there is a collision with cars
        self.border = self.x + self.speed, self.y, self.width-70, self.height-15
        self.green = (0, 255, 0)
        
        self.hit2 = False
        
    
    
    
    # a function to draw the obstacle car
    def draw(self, canvas):
        
        if self.hit2:
            
            self.hit2 = False
            
            self.y = -50
            self.x = random.randrange(self.leftBorder, self.rightBorder)
            
            canvas.blit(obsCars[1], [self.x, self.y])
            
        else:
            
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
            
            
            self.border = self.x + self.speed, self.y, self.width-70, self.height-15
            




class Coin(object):
    def __init__(self,x, y, radius, color, positionC, leftBorder, rightBorder):
        
        
        self.positionC = positionC
        
        # border of the road
        self.rightBorder = rightBorder
        self.leftBorder = leftBorder
        
        
        # coordinates and radius of bullet1
        self.x = x
        self.y = y
        self.radius = radius
        
        
        # color of the bullet
        self.color = color
        
        # speed of the bullet
        self.speed = 2
        
        
        self.touch = False
        
        
    def draw(self, canvas):
        
        if self.touch:
            
            self.x = random.randrange(self.leftBorder, self.rightBorder)
            self.y = self.positionC.y
            pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
            
            self.touch = False
            
        else:
            # changing the x and y coordinates of the bullet so that it goes dioganally
            self.y = self.y + self.speed
            
            
            
            # when the bullet goes off the screen
            # the enemy will shoot again
            # int the following line I am resetting the coordinates
            # for the bullets
            if self.y > screenHeight:
                self.x = random.randrange(self.leftBorder, self.rightBorder)
                self.y = self.positionC.y
                
            pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
        




        
# a class to make the enemy1 shot bullets
class Bullet1(object):
    def __init__(self, x, y, radius, color, positionE1):
        
        
        self.positionE1 = positionE1
        
        
        # coordinates and radius of bullet1
        self.x = x
        self.y = y
        self.radius = radius
        
        
        # color of the bullet
        self.color = color
        
        # speed of the bullet
        self.speed = 4
        
        
        self.touch = False
        
        
    def draw(self, canvas):
        
        if self.touch:
            
            self.x = self.positionE1.x
            self.y = self.positionE1.y
            pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
            
            self.touch = False
        else:
            # changing the x and y coordinates of the bullet so that it goes dioganally
            self.x = self.x + self.speed
            self.y = self.y + self.speed
            
            
            # when the bullet goes off the screen
            # the enemy will shoot again
            # int the following line I am resetting the coordinates
            # for the bullets
            if self.x > screenWidth:
                self.x = self.positionE1.x
                self.y = self.positionE1.y
                
            pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
        
        
        
        
# a class to make the enemy2 shot bullets
class Bullet2(object):
    def __init__(self, x, y, radius, color, positionE2):
        
        
        self.positionE2 = positionE2
        
        # coordinates and radius of bullet2
        self.x = x
        self.y = y
        self.radius = radius
        
        # color of the bullet
        self.color = color
        
        # speed of the bullet
        self.speedx = 4
        self.speedy = 1
        
        self.touch = False
        
        
        
    def draw(self, canvas):
        if self.touch:
            
            self.x = self.positionE2.x
            self.y = self.positionE2.y
            pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
            
            self.touch = False
            
        else:
            # changing the x and y coordinates of the bullet so that it goes dioganally
            self.x = self.x + self.speedx
            self.y = self.y + self.speedy
            
            
            # when the bullet goes off the screen
            # the enemy will shoot again
            # int the following line I am resetting the coordinates
            # for the bullets
            if self.y > 700:
                self.x = self.positionE2.x
                self.y = self.positionE2.y
                
            pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
        
        
        
        
        
# a class to make the enemy3 shot bullets
class Bullet3(object):
    def __init__(self, x, y, radius, color, positionE3):
        
        self.positionE3 = positionE3
        
        # coordinates and radius of bullet 3
        self.x = x
        self.y = y
        self.radius = radius
        
        # color of the bullet
        self.color = color
        
        # speed of the bullet
        self.speed = 1
        
        
        self.touch = False
        
    def draw(self, canvas):
        
        if self.touch:
            self.x = self.positionE3.x
            self.y = self.positionE3.y
            
            pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
            
            self.touch = False
            
        else:
            # changing the x and y coordinates of the bullet so that it goes dioganally
            self.x = self.x + self.speed
            self.y = self.y - self.speed
            
            
            # when the bullet goes off the screen
            # the enemy will shoot again
            # int the following line I am resetting the coordinates
            # for the bullets
            if self.y < 0:
                self.x = self.positionE3.x
                self.y = self.positionE3.y
                
            pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
            
        
        
        
# a class to make the enemy4 shot bullets
class Bullet4(object):
    def __init__(self, x, y, radius, color, positionE4):
        
        self.positionE4 = positionE4
        
        # coordinates and radius of bullet 4
        self.x = x
        self.y = y
        self.radius = radius
        
        # color of the bullet
        self.color = color
        
        # speed of the bullet
        self.speed = 4
        
        
        self.touch = False
        
        
    def draw(self, canvas):
        
        if self.touch:
            self.x = self.positionE4.x
            self.y = self.positionE4.y
            
            pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
            
            self.touch = False
            
        else:
            # changing the x and y coordinates of the bullet so that it goes dioganally
            self.x = self.x - self.speed
            self.y = self.y + self.speed
            
            
            # when the bullet goes off the screen
            # the enemy will shoot again
            # int the following line I am resetting the coordinates
            # for the bullets
            if self.x < 0:
                self.x = self.positionE4.x
                self.y = self.positionE4.y
                
            pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
            
        
        
        
        
        
# a class to make the enemy5 shot bullets
class Bullet5(object):
    def __init__(self, x, y, radius, color, positionE5):
        
        
        # accessing position coordinates of enemies
        # for the purpose of defining starting position of bullets
        self.positionE5 = positionE5
        
        
        # coordinates and radius of bullet 5
        self.x = x
        self.y = y
        self.radius = radius
        
        # color of the bullet
        self.color = color
        
        # speed of the bullet
        self.speedx = 4
        self.speedy = 1
        
        self.touch = False
        
    def draw(self, canvas):
        
        if self.touch:
            self.x = self.positionE5.x
            self.y = self.positionE5.y
            
            pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
            
            self.touch = False
    
        else:
            # changing the x and y coordinates of the bullet so that it goes dioganally
            self.x = self.x - self.speedx
            self.y = self.y - self.speedy
            
            
            # when the bullet goes off the screen
            # the enemy will shoot again
            # int the following line I am resetting the coordinates
            # for the bullets
            if self.x < 0:
                self.x = self.positionE5.x
                self.y = self.positionE5.y
                
            pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
            
        
        
        
        
        
        
# a class to make the road moving
class MovingRoad(object):
    def __init__(self, x, y, width, height, GenresForTheGame):
        
        
        self.GenresForTheGame = GenresForTheGame
        
        
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
        canvas.blit(genres[self.GenresForTheGame.genre], [self.x, self.y - self.height])
        canvas.blit(genres[self.GenresForTheGame.genre], [self.x, self.y])
        
            
            
            
            
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
        
        
class PositionC(object):
    def __init__(self):
        self.x = 400
        self.y = -50
        self.radius = 20
        self.color = (245, 242, 66)
        
        
        
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
        
        
        
# making instances of Position classes
# these are mainly used for positions of
# the eneies and the starting points
# of the bullets they will be shooting
positionE1 = PositionE1()
positionE2 = PositionE2()
positionE3 = PositionE3()
positionE4 = PositionE4()
positionE5 = PositionE5()

positionC = PositionC()



