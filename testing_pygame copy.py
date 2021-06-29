import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
pygame.display.set_caption("Creation")
background = pygame.image.load("/Users/kunal/python/class_pygame/Bull-5-01.jpg") #background
icon = pygame.image.load("/Users/kunal/python/class_pygame/neptune.png") #The icon for the application
pygame.display.set_icon(icon)
myanimation = pygame.image.load("/Users/kunal/python/class_pygame/dove.png") #The first character (Use a icon for this)
anix = 350
aniy = 250
playerx_change = 0
playery_change = 0
myanimation_2 = pygame.image.load("/Users/kunal/python/class_pygame/dove_2.png") #The second character (Use another icon for this)
anix_2 = random.randint(80, 400)
aniy_2 = random.randint(80, 400)
playerx_change_2 = 0.3
playery_change_2 = 0
score = 0

def animation(x, y):
    screen.blit(myanimation, (x, y))


def animation_2(x, y):
    screen.blit(myanimation_2, (x, y))


def iscollision(x, y, a, b):
    root = math.sqrt(abs((math.pow(y - b, 2))-(math.pow(x - a, 2))))
    if root < 15:
        return True
    else:
        return False


while True:
    screen.fill((75, 100, 100))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: #player 1
                playery_change = -0.75
            if event.key == pygame.K_a:
                playerx_change = -0.75
            if event.key == pygame.K_s:
                playery_change = 0.75
            if event.key == pygame.K_d:
                playerx_change = 0.75
    if anix_2 < 0: #player 2
        playerx_change_2 = 0.75
        anix_2 += playerx_change_2
    if anix_2 >= 800:
        playerx_change_2 = -0.75
        anix_2 += playerx_change_2
                                 #=====IGNORE EVERYTHING WHICH HAS BEEN COMMENTED BELOW (Commenting is aninthing that has this "#" symbol before it  )=====
            #if event.key == pygame.K_UP: #player 2
                #playery_change_2 = -0.75
            #if event.key == pygame.K_LEFT:
                #playerx_change_2 = -0.75
            #if event.key == pygame.K_DOWN:
                #playery_change_2 = 0.75
            #if event.key == pygame.K_RIGHT:
                #playerx_change_2 = 0.75
    anix += playerx_change #player 1
    aniy += playery_change
    if anix <= 0:
        anix = 0
    if anix >= 735:
        anix = 735
    if aniy <= 0:
        aniy = 0
    if aniy >= 535:
        aniy = 535
    anix_2 += playerx_change_2 #player 2
    aniy_2 += playery_change_2
    if anix_2 <= 0:
        anix_2 = 0
    if anix_2 >= 735:
        anix_2 = 735
    if aniy_2 <= 0:
        aniy_2 = 0
    if aniy_2 >= 535:
        aniy_2 = 535
    animation(anix, aniy)
    animation_2(anix_2, aniy_2)
    print(anix, aniy, anix_2, aniy_2)
    collision = iscollision(anix, aniy, anix_2, aniy_2)
    print(collision)
    if collision:
        score = score + 1
        print(score)
        anix_2 = random.randint(80, 400)
        aniy_2 = random.randint(80, 400)
    pygame.display.update()
