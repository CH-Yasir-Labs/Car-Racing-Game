#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     07/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame
import time
import random


pygame.init()
pygame.mixer.init()

pygame.init()

# Colors
gray = (119, 118, 110)
black=(0,0,0)
red=(255,0,0)

# Screen dimensions
display_width = 800
display_height = 600

# Initialize game display
gamedisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Car Game")

# Set clock
clock = pygame.time.Clock()

crash_sound = pygame.mixer.Sound("Car-crash.mp3")

# Load images (Ensure correct file paths and extensions)
carimg = pygame.image.load("Car.png")
backgroundpic = pygame.image.load("background.png")
yellow_strip = pygame.image.load("yellow_strip.png")
strip = pygame.image.load("strip.png")

car_width=56

def obstacle(obs_startx, obs_starty, obs):
    obs_images = ["Car.png", "Car1.png", "Car2.png", "Car3.png", "Car4.png", "Car5.png"]

    if 0 <= obs < len(obs_images):  # ✅ Ensure obs is in the correct range
        obs_pic = pygame.image.load(obs_images[obs])
        gamedisplay.blit(obs_pic, (obs_startx, obs_starty))
    else:
        print(f"Invalid obstacle index: {obs}")  # ✅ Debugging output (Optional)


def score_system(passed,score):
    font=pygame.font.SysFont(None,25)
    text=font.render("passed :"+str(passed),True,red)
    score=font.render("score :"+str(score),True,black)
    gamedisplay.blit(text,(0,50))
    gamedisplay.blit(score,(0,30))



def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()


def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplay.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash():
    pygame.mixer.Sound.play(crash_sound)  # Play sound
    message_display("YOU CRASHED")

def draw_background():  # ✅ Renamed function
    # Left side
    gamedisplay.blit(backgroundpic, (0, 0))
    gamedisplay.blit(backgroundpic, (0, 200))
    gamedisplay.blit(backgroundpic, (0, 400))
    gamedisplay.blit(backgroundpic, (710, 0))
    gamedisplay.blit(backgroundpic, (710, 200))
    gamedisplay.blit(backgroundpic, (710, 400))



    gamedisplay.blit(yellow_strip, (400,0))
    gamedisplay.blit(yellow_strip, (400,100))
    gamedisplay.blit(yellow_strip, (400,200))
    gamedisplay.blit(yellow_strip, (400,300))
    gamedisplay.blit(yellow_strip, (400,400))
    gamedisplay.blit(yellow_strip, (400,500))
    gamedisplay.blit(yellow_strip, (400,600))

    gamedisplay.blit(strip, (120,0))
    gamedisplay.blit(strip, (120,70))
    gamedisplay.blit(strip, (120,140))
    gamedisplay.blit(strip, (120,210))
    gamedisplay.blit(strip, (120,280))
    gamedisplay.blit(strip, (120,350))
    gamedisplay.blit(strip, (120,420))
    gamedisplay.blit(strip, (120,490))
    gamedisplay.blit(strip, (120,560))
    gamedisplay.blit(strip, (680,0))
    gamedisplay.blit(strip, (680,70))
    gamedisplay.blit(strip, (680,140))
    gamedisplay.blit(strip, (680,210))
    gamedisplay.blit(strip, (680,280))
    gamedisplay.blit(strip, (680,350))
    gamedisplay.blit(strip, (680,420))
    gamedisplay.blit(strip, (680,490))
    gamedisplay.blit(strip, (680,560))




# Function to draw car
def car(x, y):
    gamedisplay.blit(carimg, (x, y))

# Game loop
def game_loop():
    x = display_width * 0.45
    y = display_height * 0.8
    x_change = 0
    obstacle_speed=9
    obs=0
    y_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=56
    obs_height=125
    passed=0
    lvl=0
    score=0



    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        # Update car position
        x += x_change

        # ✅ Move these inside the loop so the screen updates every frame
        gamedisplay.fill(gray)
        draw_background()
        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x, y)
        score_system(passed,score)
        if x>680-car_width or x<110:
            crash()

        if x> display_width-(car_width+110) or x<110:
            crash()

        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,6)
            passed=passed+1
            score=passed*10
            if int(passed)%10==0:
                 lvl=lvl+1
                 obstacle_speed+2
                 largetext=pygame.font.Font("freesansbold.ttf",80)
                 textsurf,textrect=text_objects("Level"+str(lvl),largetext)
                 textrect.center=((display_width/2),(display_height/2))
                 gamedisplay.blit(textsurf,textrect)
                 pygame.display.update()
                 time.sleep(3)



        if y < obs_starty + obs_height:  # If my car is at the same vertical level as obstacle
           if x + car_width > obs_startx and x < obs_startx + obs_width:
        # ✅ Collision detected (my car is inside the obstacle’s width)
               crash()















        pygame.display.update()
        clock.tick(60)

# Run the game
game_loop()
pygame.quit()
quit()