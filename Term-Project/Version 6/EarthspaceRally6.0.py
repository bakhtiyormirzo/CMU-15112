##########################
# Version 6.0

# Name: Bakhtiyorjon Mirzajonov
# Andrew ID: bmirzajo

##########################

##########################
# importing necessary libraries

import pygame
from pygame import mixer
import os
import random
import classes

##########################



pygame.init()


# declaring the screen height and width
screenWidth = 1000
screenHeight = 700


# creating the Game Window (Canvas)
canvas = pygame.display.set_mode( (screenWidth, screenHeight) )



# Name of the Window
pygame.display.set_caption("Car Game")



# Starting the mixer
mixer.init()

# importing and playing the music
mixer.music.load( os.path.join("Sounds", "soundtrack.mp3") )
mixer.music.play(-1)




# class for beginning page
beginning = classes.Beginning(0, 0, screenWidth, screenHeight)

highway = classes.Highway(screenWidth, screenHeight)



# making instance of Genres class
genresClass = classes.GenresForTheGame(0, 0, screenWidth, screenHeight)


# moving road
movingRoad = classes.MovingRoad(0, 0, screenWidth, screenHeight, genresClass)







# making instances of Position classes
# these are mainly used for positions of
# the eneies and the starting points
# of the bullets they will be shooting
positionE1 = classes.PositionE1()
positionE2 = classes.PositionE2()
positionE3 = classes.PositionE3()
positionE4 = classes.PositionE4()
positionE5 = classes.PositionE5()

positionC = classes.PositionC()


coin = classes.Coin(positionC.x, positionC.y, positionC.radius, positionC.color,
                    positionC, highway.leftBorder, highway.rightBorder)

# making instances of enemies
enemy1 = classes.Enemy1(positionE1.x, positionE1.y,
                        positionE1.width, positionE1.height, genresClass)

enemy2 = classes.Enemy2(positionE2.x, positionE2.y,
                        positionE2.width, positionE2.height, genresClass)

enemy3 = classes.Enemy3(positionE3.x, positionE3.y,
                        positionE3.width, positionE3.height, genresClass)

enemy4 = classes.Enemy4(positionE4.x, positionE4.y,
                        positionE4.width, positionE4.height, genresClass)

enemy5 = classes.Enemy5(positionE5.x, positionE5.y,
                        positionE5.width, positionE5.height, genresClass)


# making instances of obstacle cars positions
positionO1 = classes.PositionO1()
positionO2 = classes.PositionO2()

# making instances of obstable cars
obsCar1 = classes.Obstable1( positionO1.x, positionO1.y,
                     positionO1.width, positionO1.height,
                     highway.leftBorder, highway.rightBorder
                     )

obsCar2 = classes.Obstable2( positionO2.x, positionO2.y,
                     positionO2.width, positionO2.height,
                     highway.leftBorder, highway.rightBorder
                     )


# making instances of bullet classes to draw shots
bullet1 = classes.Bullet1( positionE1.x + (positionE1.width // 4),
                           positionE1.y + (positionE1.height // 4),
                           enemy1.radius, enemy1.color, positionE1
                           )

bullet2 = classes.Bullet2( positionE2.x + (positionE2.width // 4),
                           positionE2.y + (positionE2.height // 4),
                           enemy2.radius, enemy2.color, positionE2
                           )

bullet3 = classes.Bullet3( positionE3.x + (positionE3.width // 4),
                           positionE3.y + (positionE3.height // 4),
                           enemy3.radius, enemy3.color, positionE3
                           )

bullet4 = classes.Bullet4( positionE4.x + (positionE4.width // 4),
                           positionE4.y + (positionE4.height // 4),
                           enemy4.radius, enemy4.color, positionE4
                           )

bullet5 = classes.Bullet5( positionE5.x + (positionE5.width // 4),
                           positionE5.y + (positionE5.height // 4),
                           enemy5.radius, enemy5.color, positionE5
                           )


# making instances of the classes 
player = classes.Player(500, 500, 120, 120, beginning, genresClass,
            coin, obsCar1, obsCar2, bullet1, bullet2, bullet3, bullet4, bullet5)

# class for ending page
ending = classes.Ending(0, 0, screenWidth, screenHeight, player)


# a function to redraw the Game Window 
def redrawCanvas():
    
    
    # this draws the background of the game
    # when you run the program
    if beginning.begun == False:
        beginning.draw(canvas)
        

    # when a player chooses a car and starts the game
    # this will run and draws everything needed 
    if beginning.begun:
        
        
        if player.alreadyLost == False:
            
            #canvas.blit(bgs[genre], (0,0))
            movingRoad.draw(canvas)
            
           
            
            #canvas.blit(hPic, (highway.leftBorder, 0))
            player.draw(canvas)
            
            
            # difficulty level 1
            enemy1.draw(canvas)
            bullet1.draw(canvas)
            
            
            # difficulty level 2
            if player.score > 5:
                enemy2.draw(canvas)
                bullet2.draw(canvas)
                
                
            # difficulty level 3
            if player.score > 10:
                enemy3.draw(canvas)
                bullet3.draw(canvas)
                
                
            # difficulty level 4
            if player.score > 15:
                enemy4.draw(canvas)
                bullet4.draw(canvas)
                
                
            # difficulty level 5
            if player.score > 20:
                enemy5.draw(canvas)
                bullet5.draw(canvas)
                
                
            # drawing obstacles
            obsCar1.draw(canvas)
            obsCar2.draw(canvas)
            
            
            # drawing the rewarding coins
            coin.draw(canvas)
            
        
        if player.alreadyLost or player.won:
            
            ending.draw(canvas)
    
    
    
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
    
    
    # pressing space shows the car selection window to the player
    if keys[pygame.key.key_code("space")]:
        classes.bg = 1
        
        player.alreadyLost = False
        player.won = False
    
    
    # this is how a player chooses the car he wants to play with
    if keys[pygame.key.key_code("y")] and beginning.begun == False:
        
        # starting the game
        beginning.begun = True
        
        # selecting the car from a list of loaded images of cars
        classes.car = 0
        
        player.alreadyLost = False
        player.won = False
        
    if keys[pygame.key.key_code("b")] and beginning.begun == False:
        
        # starting the game
        beginning.begun = True
        
        # selecting the car from a list of loaded images of cars
        classes.car = 1
        
        player.alreadyLost = False
        player.won = False
        
        
    if keys[pygame.key.key_code("w")] and beginning.begun == False:
        
        # starting the game
        beginning.begun = True
        
        # selecting the car from a list of loaded images of cars
        classes.car = 2
        
        player.alreadyLost = False
        player.won = False
        
        
    # by pressing Excape, a player is given an option to restart the game
    # it directs the user to a car selection window
    if keys[pygame.K_ESCAPE]:
        
        # stopping the game and going back to car selction page
        beginning.begun = False
        
        # resetting the genre 
        genresClass.genre = 0
        
        
        # resetting the player to the starting position
        player = classes.Player(500, 500, 120, 120, beginning, genresClass,
                coin, obsCar1, obsCar2, bullet1, bullet2, bullet3, bullet4, bullet5)
        
        
        # restarting
        player.reset()
        
        
    
        
        
    # limiting the car to the borders of the road
    # while it is moving
    if (keys[pygame.K_LEFT] and player.x > highway.leftBorder):
        
        player.x -= player.vel
        
    if keys[pygame.K_RIGHT] and player.x < highway.rightBorder:
        
        player.x += player.vel
        
    if keys[pygame.K_UP] and player.y > player.vel:
        
        player.y -= player.vel
        
    if keys[pygame.K_DOWN] and player.y < (screenHeight -
                               player.height - player.vel - 30):
        
        player.y += player.vel
        
        
    # collision with obstacle car 1    
    if player.x > obsCar1.border[0] and player.x < obsCar1.border[0] + obsCar1.border[2]:
        if player.y > obsCar1.border[1] and player.y < obsCar1.border[1] + obsCar1.border[3]:
            
            player.accident()
            
    
    # checks if cars get into car accident
    if player.x > obsCar1.border[0] and player.x + player.width < obsCar1.border[0] + obsCar1.border[2]:
        if player.y > obsCar1.border[1] and player.y < obsCar1.border[1] + obsCar1.border[3]:
            
            player.accident() 
    
            
    # collision with obstacle car 2   
    if player.x > obsCar2.border[0] and player.x < obsCar2.border[0] + obsCar2.border[2]:
        if player.y > obsCar2.border[1] and player.y < obsCar2.border[1] + obsCar2.border[3]:
            
            player.accident()
            
        
    # checks if coin is collected
    if player.x < coin.x + coin.radius and player.x + player.width > coin.x - coin.radius:
        if player.y < coin.y + coin.radius and player.y + player.height > coin.y - coin.radius:
            
            player.gotCoin()
            
            
    # checks if car is hit by a bullet
    if player.x < bullet1.x + bullet1.radius and player.x + player.width > bullet1.x - bullet1.radius:
        if player.y < bullet1.y + bullet1.radius and player.y + player.height > bullet1.y - bullet1.radius:
            
            player.gotHit()
            
    
    # checks if car is hit by a bullet 
    if player.x < bullet2.x + bullet2.radius and player.x + player.width > bullet2.x - bullet2.radius:
        if player.y < bullet2.y + bullet2.radius and player.y + player.height > bullet2.y - bullet2.radius:
            
            player.gotHit()
            
     
    # checks if car is hit by a bullet
    if player.x < bullet3.x + bullet3.radius and player.x + player.width > bullet3.x - bullet3.radius:
        if player.y < bullet3.y + bullet3.radius and player.y + player.height > bullet3.y - bullet3.radius:
            
            player.gotHit()
            
            
    # checks if car is hit by a bullet       
    if player.x < bullet4.x + bullet4.radius and player.x + player.width > bullet4.x - bullet4.radius:
        if player.y < bullet4.y + bullet4.radius and player.y + player.height > bullet4.y - bullet4.radius:
            
            player.gotHit()
            
            
    # checks if car is hit by a bullet
    if player.x < bullet5.x + bullet5.radius and player.x + player.width > bullet5.x - bullet5.radius:
        if player.y < bullet5.y + bullet5.radius and player.y + player.height > bullet5.y - bullet5.radius:
            
            player.gotHit()
    
    
    # calling a function to draw everything
    redrawCanvas()
    
            
pygame.quit()


